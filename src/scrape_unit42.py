"""Scrape Unit 42 threat intelligence posts via their sitemap.

Strategy:
1. Fetch the sitemap index XML
2. Pull individual post URLs from sub-sitemaps
3. For each post: fetch HTML, save raw copy, parse to markdown, save with frontmatter

Politeness:
- Identifies as a named bot via User-Agent
- 2-second delay between requests (configurable)
- Hard cap on max posts per run (MAX_POSTS)
- Skips posts that fail to parse instead of crashing
"""
import re
import time
import requests
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify

# ============================================================
# Config
# ============================================================
SITEMAP_INDEX_URL = "https://unit42.paloaltonetworks.com/sitemap_index.xml"
USER_AGENT = (
    "Mozilla/5.0 (compatible; ThreatIntelRAGBot/0.1; "
    "+https://github.com/AimanManzoor/Threat-intel-rag-assistant)"
)
REQUEST_DELAY_S = 2.0
MAX_POSTS = 50  # Start small for testing — bump up after first successful run
MIN_BODY_CHARS = 500  # Skip posts shorter than this (likely landing/index pages)

PROJECT_ROOT = Path(__file__).parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Polite HTTP layer
# ============================================================
def fetch(url):
    """GET a URL with our User-Agent and a polite delay after."""
    print(f"  GET {url}")
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    time.sleep(REQUEST_DELAY_S)
    return response


# ============================================================
# Sitemap parsing
# ============================================================
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def get_post_urls():
    """Walk the sitemap index → sub-sitemaps → post URLs."""
    print(f"Fetching sitemap index: {SITEMAP_INDEX_URL}")
    resp = fetch(SITEMAP_INDEX_URL)

    root = ET.fromstring(resp.text)
    sub_sitemaps = [loc.text for loc in root.findall(".//sm:loc", SITEMAP_NS)]
    print(f"Found {len(sub_sitemaps)} sub-sitemaps:")
    for s in sub_sitemaps:
        print(f"  - {s}")

    # Prefer post sitemaps if labeled, else fall back to all
    post_sitemaps = [s for s in sub_sitemaps if "post" in s.lower()]
    if not post_sitemaps:
        post_sitemaps = sub_sitemaps

    post_urls = []
    for sm_url in post_sitemaps[:3]:  # safety: limit to first 3 sub-sitemaps
        print(f"\nFetching sub-sitemap: {sm_url}")
        try:
            resp = fetch(sm_url)
            sub_root = ET.fromstring(resp.text)
            urls = [loc.text for loc in sub_root.findall(".//sm:loc", SITEMAP_NS)]
            post_urls.extend(urls)
        except Exception as e:
            print(f"  [skip sub-sitemap] {e}")

    # Filter out obvious non-content URLs
    excluded = ["/category/", "/tag/", "/author/", "/page/", "/about/", "/contact/"]
    filtered = [u for u in post_urls if not any(e in u.lower() for e in excluded)]
    # Also drop the bare homepage and short URLs
    filtered = [u for u in filtered if len(urlparse(u).path.strip("/")) > 5]

    print(f"\nCandidate post URLs after filtering: {len(filtered)}")
    return filtered


# ============================================================
# HTML → Markdown extraction
# ============================================================
def parse_post(html, url):
    """Extract title, date, and clean markdown body from a Unit 42 post."""
    soup = BeautifulSoup(html, "html.parser")

    # Title — prefer og:title meta, fall back to h1
    title = ""
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()
    elif soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)

    # Publish date — prefer article:published_time meta
    date = ""
    pub_meta = soup.find("meta", property="article:published_time")
    if pub_meta and pub_meta.get("content"):
        date = pub_meta["content"][:10]  # ISO date prefix
    else:
        time_tag = soup.find("time")
        if time_tag:
            date = time_tag.get("datetime", "")[:10] or time_tag.get_text(strip=True)

    # Article body — try several common containers
    article = (
        soup.find("article")
        or soup.find("main")
        or soup.find("div", class_=re.compile(r"(post-content|entry-content|article-body)"))
    )
    if not article:
        return None

    # Strip noise
    for tag in article.find_all(["nav", "footer", "aside", "script", "style", "form", "iframe"]):
        tag.decompose()

    body_md = markdownify(str(article), heading_style="ATX")
    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()

    if len(body_md) < MIN_BODY_CHARS:
        return None

    return {"title": title or "Untitled", "date": date, "url": url, "body_md": body_md}


# ============================================================
# Saving
# ============================================================
def slugify(text, max_len=60):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text[:max_len].strip("-") or "untitled"


def save_post(index, post):
    """Write the post as a markdown file with YAML-ish frontmatter."""
    slug = slugify(post["title"])
    filename = f"unit42_{index:03d}_{slug}.md"
    md = (
        f"---\n"
        f"title: \"{post['title']}\"\n"
        f"date: \"{post['date']}\"\n"
        f"url: {post['url']}\n"
        f"source: unit42\n"
        f"---\n\n"
        f"# {post['title']}\n\n"
        f"{post['body_md']}\n"
    )
    (PROCESSED_DIR / filename).write_text(md)
    print(f"  ✓ saved {filename}  ({len(post['body_md'])} chars)")


# ============================================================
# Main
# ============================================================
def main():
    post_urls = get_post_urls()
    if not post_urls:
        print("No post URLs found. Check the sitemap structure.")
        return

    saved = 0
    skipped = 0
    errored = 0

    for i, url in enumerate(post_urls, 1):
        if saved >= MAX_POSTS:
            print(f"\nReached MAX_POSTS limit ({MAX_POSTS}). Stopping.")
            break

        print(f"\n[{i}/{len(post_urls)}] {url}")
        try:
            resp = fetch(url)

            # Save raw HTML for resilience (re-parse later without re-fetching)
            url_slug = urlparse(url).path.strip("/").replace("/", "_")[:80]
            (RAW_DIR / f"{url_slug}.html").write_text(resp.text)

            post = parse_post(resp.text, url)
            if not post:
                print(f"  [skip] could not parse (no article body or too short)")
                skipped += 1
                continue

            save_post(saved + 1, post)
            saved += 1
        except Exception as e:
            print(f"  [error] {e}")
            errored += 1

    print(f"\n{'=' * 50}")
    print(f"Saved:   {saved}")
    print(f"Skipped: {skipped}")
    print(f"Errored: {errored}")
    print(f"\nProcessed markdown in: {PROCESSED_DIR}")
    print(f"Raw HTML in:           {RAW_DIR}")


if __name__ == "__main__":
    main()
