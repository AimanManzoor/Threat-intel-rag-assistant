---
title: "Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure"
date: "2026-03-31"
url: https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/
source: unit42
---

# Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/ "High Profile Threats")
* [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")

[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  14  min read

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex Xpanse icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Xpanse](https://unit42.paloaltonetworks.com/product-category/cortex-xpanse/ "Cortex Xpanse")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Unit 42](https://unit42.paloaltonetworks.com/author/unit42/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 31, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)
  + [Malware](https://unit42.paloaltonetworks.com/category/malware/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/)
  + [GitHub](https://unit42.paloaltonetworks.com/tag/github/)
  + [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/)
  + [Python](https://unit42.paloaltonetworks.com/tag/python/)
  + [Supply chain](https://unit42.paloaltonetworks.com/tag/supply-chain/)
  + [Wiper](https://unit42.paloaltonetworks.com/tag/wiper/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Weaponizing%20the%20Protectors:%20TeamPCP’s%20Multi-Stage%20Supply%20Chain%20Attack%20on%20Security%20Infrastructure&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F&title=Weaponizing%20the%20Protectors:%20TeamPCP’s%20Multi-Stage%20Supply%20Chain%20Attack%20on%20Security%20Infrastructure "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F&text=Weaponizing%20the%20Protectors:%20TeamPCP’s%20Multi-Stage%20Supply%20Chain%20Attack%20on%20Security%20Infrastructure "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Weaponizing%20the%20Protectors:%20TeamPCP’s%20Multi-Stage%20Supply%20Chain%20Attack%20on%20Security%20Infrastructure%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fteampcp-supply-chain-attacks%2F "Share in Mastodon")

## Executive Summary

Between late February and March 2026, threat group TeamPCP conducted a highly calculated, escalating sequence of supply chain threats. It systematically compromised widely trusted open-source security tools, including the vulnerability scanners [Trivy](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) and [KICS](https://checkmarx.com/blog/checkmarx-security-update/) and the popular AI gateway [LiteLLM](https://docs.litellm.ai/blog/security-update-march-2026). The affected software also includes the official Python SDK of Telnyx.

These ongoing supply chain attacks injected malicious infostealer payloads directly into GitHub Actions and Python Package Index (PyPI) registries. Once executed during routine automated workflows, the malware silently extracts highly sensitive data, such as:

* Cloud access tokens
* SSH keys
* Kubernetes secrets

These attacks also establish persistent backdoors for lateral movement across clusters.

The affected software includes:

* BerriAI [LiteLLM](https://www.litellm.ai/), an open-source library used to route requests across LLM providers (its documentation states it has over 95 million monthly downloads)
* Aqua Security [Trivy](https://www.aquasec.com/products/trivy/) and Checkmarx [KICS](https://checkmarx.com/product/kics/) (Keeping Infrastructure as Code Secure), which are embedded in millions of enterprise CI/CD pipelines
* The widely used official Python SDK of [Telnyx,](https://telnyx.com/) a global communications platform providing programmable APIs for voice and messaging

Attackers are believed by sources such as [vx-underground](https://x.com/vxunderground/status/2036532168084672816?s=20) to have already exfiltrated data from 500,000 infected machines over 300 GB of data and secrets from 500,000 machines, exposing major organizations across all business verticals to severe follow-on attacks.

Unlike past supply chain attacks, this operation explicitly weaponizes security and developer infrastructure that inherently require elevated privileges. This allows attackers unimpeded access to production secrets. They then have the ability to hold compromised organizations for ransom, demanding extortion payments.

The current scope of the attack is significant:

* **Scale of impact**: The actor may have exfiltrated over 300 GB of data and 500,000 credentials, including cloud tokens and Kubernetes secrets.
* **Breadth of compromise**: Beyond the primary targets, TeamPCP leveraged harvested tokens to infect 48 additional packages. It identified and published at least 16 victim organizations via public leak sites.
* **Sophistication**: The attackers introduced CanisterWorm, which includes both a decentralized command-and-control (C2) architecture and targeted wiper components. This demonstrates an evolving technique pattern focused on cloud-native operations.

As of March 27, Palo Alto Networks [Cortex Xpanse](https://docs-cortex.paloaltonetworks.com/p/XPANSE) has identified the presence of three unique self-signed certificates associated with the three waves of operations.

Palo Alto Networks customers are better protected from the threats described in this article through the following products and services:

* [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration)
* [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)
* [Cortex Cloud](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection)
* [Cortex Xpanse](https://docs-cortex.paloaltonetworks.com/p/XPANSE)
* [Cortex Agentix](https://www.paloaltonetworks.com/cortex/agentix) Threat Intel Agent

Palo Alto Networks also recommends taking steps to identify vulnerable packages and harden CI/CD policies, as described in the [Interim Guidance](#post-176426-_zg1rezlvhwuy) section.

The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

The [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk.

## Current Scope of the Supply Chain Attack

TeamPCP (aka PCPcat, ShellForce, DeadCatx3) has conducted operations dating back to at least September 2025. The group gained notoriety in December 2025, in the wake of the massive React2Shell campaign that targeted cloud environments.

That campaign exploited the [React2Shell](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/) vulnerability (CVE-2025-55182), allowing the group to leverage remote code execution (RCE) within vulnerable cloud endpoints. During these operations, the group's most notable detection artifact, alongside the more well known React2Shell exploit indicators, was using the port number 666 for nearly all of its exploitation operations.

The group’s trajectory has rapidly evolved. While the group initially focused on [ransomware](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware), it also has roots in cryptocurrency mining and cryptocurrency theft. The group has more recently shifted toward smash and grab supply chain compromise operations starting in mid March 2026.

Recently, the group's rate of activity has increased. It’s increased posting on its Telegram channel as well as on its dark web leak site.

Its more recent announcements state that the group is combining forces with [CipherForce](https://www.ransomlook.io/group/cipherforce), another ransomware group, to publish information on breaches. Additionally, it was announced on BreachForums — a forum for cybercriminals to discuss hacking topics and data breaches — that the group is partnering with [Vect](https://www.ransomware.live/group/vect) ransomware group, as shown in Figure 1.

![A screenshot of a forum post announcing a partnership with BreachForums and TeamPCP. The post highlights a collaboration to enhance their operations. The post is hosted on a dark-themed webpage, with bold red and white text.]()

Figure 1. Screenshot of BreachForums announcement.

This partnership is likely to allow TeamPCP to concentrate on supply chain operations. As of late March, TeamPCP announced the compromise of at least 16 organizations, as shown in Figure 2.

![The image is a screenshot of a dark-themed website titled "CIPHERFORCE". It features a large message in white text: "Secure your data" with a subheading: "Companies that refused to pay are published here. Countdowns are until data release." Below are three boxes with numbers: "16" for total victims, "1" for active countdowns, and "11" for companies published. A navigation menu on the right includes "Home," "Victims," and "News".]()

Figure 2. Screenshot of the CipherForce ransomware data leak site.

### Aqua Security Trivy

This latest campaign started on March 19, 2026, when TeamPCP leveraged an incomplete credential rotation following a minor breach in late February within the Aqua Security Trivy GitHub repository.

TeamPCP compromised the aqua-bot service account and executed an imposter commit attack. This resulted in the force-push of malicious code to 76 of 77 version tags in the aquasecurity/trivy-action repository and all tags in aquasecurity/setup-trivy.

This initial wave introduced the TeamPCP primary payload, called TeamPCP cloud stealer. It performed its actions through the kamikaze.sh script, which evolved into three distinct versions:

* **Version 1 -** **Monolithic Architecture**: A 150-line bash script focused on environment fingerprinting and immediate credential harvesting from AWS/GCP/Azure credentials using the compromised endpoint’s instance metadata service (IMDS). It bypassed GitHub’s secret masking by reading the runner.worker process memory directly via /proc/<pid>/mem to extract plaintext tokens.
* **Version 2 -** **Modular Architecture**: Two hours after the first release of v1, TeamPCP replaced the first script with a slim 15-line loader script. This version used a pull method to download a second-stage payload called kube.py. This allowed the actors to update the payload without having to re-poison the GitHub tags. Version 2 also introduced a self-deletion command rm – “$0” to remove itself after execution.
* **Version 3 -** **The Worm and Wiper**: In this final known version, the script evolved into malware with self-replication capabilities in a campaign called CanisterWorm. We will cover CanisterWorm in more detail [below](#post-176426-_enri5yvj3xop). Version 3 enabled the scanning of exposed Docker APIs, port 2375 and the local subnet. It also enabled harvesting SSH keys.

This operation was uniquely deceptive. For example, the malicious code ran before the legitimate Trivy scan logic could execute, while simultaneously allowing the legitimate scanner to continue operations. This allowed scanning operations to return a normal operational status, while behind the scenes, the malware was silently exfiltrating data to the typosquatted domain scan.aquasecurtiy[.]org. If the primary C2 server failed, the payload used the backup domain tdtqy-oyaaa-aaaae-af2dq-cai.raw.icp0[.]io.

Additionally, using npm publishing tokens harvested during the initial Trivy wave of compromises, TeamPCP actors initiated an automated script that identified and infected 47 additional packages across the @emilgroup, @opengov and @v7 namespaces. All reports indicate that these operations took place in under 60 seconds.

The infection was achieved by injecting a malicious pre-install or post-install script within the package.json file of each library. This ensured that the TeamPCP cloud stealer payload executed immediately upon a developer or continuous integration/continuous delivery (CI/CD) runner performing an npm install containing any of these poisoned npm packages. A CI/CD runner is a lightweight agent or application that executes software pipeline jobs.

This wave focused heavily on a technique called software development kit (SDK)-squatting, targeting internal development kits for billing, insurance and accounting services. This maximized the likelihood of the malware landing in high-privilege corporate environments.

Each infected package acted as a new telemetry node, performing environment fingerprinting and attempting to exfiltrate data from local .env files and AWS/Azure configuration directories back to the group's C2 infrastructure. This effectively turned a single vendor breach into a systemic and potentially widespread supply chain risk for any downstream consumers of these private and public SDKs.

### Checkmarx KICS

Following the initial compromise of Aqua Security Trivy, on March 21, 2026, TeamPCP used stolen GitHub Personal Access Tokens (PATs) to target Checkmarx KICS. KICS is an open-source infrastructure-as-code (IaC) scanner.

The attackers force-pushed malicious commits to all 35 version tags of the checkmarx/kics-github-action repository and poisoned version 2.3.28 of checkmarx/ast-github-action. Technically, the operation subverted the official container entrypoint setup.sh and instead injected a three-stage payload called TeamPCP cloud stealer.

This payload has similar functionality to the Trivy wave payload. To avoid manual detection, the malware exfiltrated stolen data to the vendor-themed typosquat domain checkmarx[.]zone. It featured a secondary fallback mechanism, where if the primary C2 communications failed, the payload used the victim's own GITHUB\_TOKEN to create a hidden repository named docs-tpcp located within the victim's GitHub organization.

### LiteLLM

On March 23, 2026, TeamPCP moved away from GitHub PATs by targeting PyPI publishing tokens using BerriAI LiteLLM. The group likely harvested these tokens from an earlier compromise of the Trivy vulnerability scanner. Attackers poisoned the LiteLLM CI/CD pipeline to enable uploading malicious versions (v1.82.7 and v1.82.8) to the PyPI.

This wave introduced a highly evasive execution method via a .pth file named litellm\_init.pth in version 1.82.8. Due to the Python interpreter automatically processing .pth files during startup, the malware executed every time any Python process was initialized on a host regardless of whether LiteLLM was ever imported. This allowed for TeamPCP to increase the scope for potential victims.

The multi-stage payload consisted of a double Base64-encoded script, designed to bypass static analysis. The script functioned as a comprehensive secret-sweeper where it harvested:

* SSH keys
* Cloud credentials (AWS, Google Cloud, Azure)
* Kubernetes configuration files
* Critically, the high-density environment variables containing LLM API keys (e.g., OPENAI\_API\_KEY, ANTHROPIC\_API\_KEY)

Figure 3 below shows an example of this in a code snippet.

![Command line interface screenshot. The command executed is a Python 3 script involving importing the `base64` module and executing a base64 encoded script. ]()

Figure 3. A code snippet representing the double Base64-encoded script.

Inside of this Base64 encoding was a second Base64-encoded block, which provided the C2 endpoint for C2 commands. Figure 4 shows code written to the filepath /host/root/.config/sysmon/sysmon.py.

![A code snippet in Python is displayed. It defines a function which sends a request to a URL specified by the variable `C_URL`. The request includes a user-agent header.]()

Figure 4. The code written to /host/root/.config/sysmon/sysmon.py.

The exfiltrated data was handled in the same fashion as the Checkmarx wave, encrypted using an AES-256-CBC session key, which was further secured with a hard-coded 4096-bit RSA public key. For the LiteLLM exfiltration C2 endpoint, the attackers used the typosquatted domain models.litellm[.]cloud. The code shown in Figure 5 is an example for the subprocess that handled the exfiltration of collected data.

![A snippet of Python code using the `subprocess` module. It sends a POST request to a URL using `curl`. ]()

Figure 5. Subprocess to handle exfiltration of collected data.

The following lists all known C2 exfiltration domains up to March 27, 2026:

* scan.aquasecurtiy[.]org
* checkmarx[.]zone
* models.litellm[.]cloud
* tdtqy-oyaaa-aaaae-af2dq-cai.raw.icp0[.]io

### Telnyx

On March 27, 2026, TeamPCP compromised the Telnyx Python SDK. This followed a pattern similar to LiteLLM where the threat actor hijacked PyPI publishing credentials to publish malicious versions 4.87.1 and 4.87.2 of the telnyx package.

These versions contain a silent injector in the client library that executes immediately upon import to exfiltrate cloud credentials and system secrets. The attack uses WAV steganography to hide encrypted second-stage payloads within valid audio files, allowing the malware to bypass network filters while establishing persistence on Windows, Linux and macOS systems.

The Windows audio file had the hard-coded name hangup.wav, and the Linux audio file had the hard-coded name ringtone.wav. This campaign specifically targets infrastructure and communication tools to harvest high-value access tokens and service account keys for broader cluster exploitation.

### CanisterWorm

CanisterWorm uses a decentralized [Internet Computer Protocol](https://internetcomputer.org/) (ICP) canister for C2, providing a tamper-proof dead-drop for payload delivery that is resistant to typical worm takedown operations. Beyond stealing credentials and achieving persistence, the threat actors also masqueraded their activity as legitimate services like [systemd](https://systemd.io/) and disguised the threat as a PostgreSQL utility called [pgmon](https://lib.rs/crates/pgmon).

The campaign recently integrated a destructive wiper component, which was [observed](https://krebsonsecurity.com/2026/03/canisterworm-springs-wiper-attack-targeting-iran/) on March 23, 2026, targeting Iran. This is visible within the code blocks from the file kube.py shown in Figures 6 and 7.

![Code snippet showing a main function structure with conditional logic. The script exits with an error code if certain conditions are met.]()

Figure 6. Code block from kube.py (1 of 2).

![The image shows a Python code snippet checking if the timezone is set to Iran. ]()

Figure 7. Code block from kube.py (2 of 2).

This secondary payload performs environment fingerprinting to identify Kubernetes clusters, deploying privileged DaemonSets to brick entire clusters or executing recursive file deletions on non-containerized hosts. This blend of automated propagation, decentralized infrastructure and targeted destruction marks CanisterWorm as one of the more complex cloud-native threats identified to date, even with its loud and short-lived operational history.

## Interim Guidance

### Hardening Cloud Assets Against Supply Chain Attacks

Cortex Cloud offers extensive application security posture management (ASPM) and supply chain security capabilities to help identify the vulnerabilities and misconfigurations that TeamPCP relies upon. The guidance below includes some instructions specific to Palo Alto Networks products. We recommend that all organizations find an appropriate mechanism to harden cloud assets as described.

(Note: Prisma Cloud customers who haven’t yet migrated to Cortex Cloud should take the same precautions.)

**1. Identifying vulnerable packages: software composition analysis (SCA) and software bill of materials (SBOM)**

Since CVEs for these malicious packages may lag behind the attack, organizations must rely on real-time visibility into their SBOM.

* Operational risk model: For packages without published CVEs, Palo Alto Networks’ proprietary Operational Risk model provides additional protection. It evaluates open-source packages based on factors such as maintainer activity, deprecation status and community adoption, allowing us to identify risky components even in the absence of known vulnerabilities.
* SBOM Querying: Cortex Cloud allows you to query your organization's SBOM against the list of known malicious packages to immediately identify impact.

**2. Hardening CI/CD policies: out-of-the-box rules**

TeamPCP thrives in insecure and exposed environments. Palo Alto Networks customers can leverage the following Cortex Cloud out-of-the-box (OotB) CI/CD rules designed to prevent similar attacks. These rules map to industry standards like the [OWASP Top 10 CI/CD Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) and [CIS Software Supply Chain Security Guide](https://www.cisecurity.org/insights/white-papers/cis-software-supply-chain-security-guide).

* **Packages insecurely installed:** In common configurations, both GitHub and npm can deliver updated package versions without checking package integrity. This allows attackers who control a given repository to upload a malicious version of a package that’s enabled for automatic download. It is critical that organizations trust but verify every package. It is vital for modern CI/CD pipelines to scan all packages prior to implementation.
* **An npm package downloaded from git without a commit hash reference:** Without a specific commit hash, the integrity of a package downloaded from a git URL can’t be guaranteed, which potentially allows a build server to download a malicious version.
* **An npm project contains unused dependencies:** Unused dependencies widen the attack surface without justification. If an unused dependency is compromised by TeamPCP, it exposes the project to risk even if the code isn't actively used.

## Unit 42 Managed Threat Hunting Queries

The Unit 42 Managed Threat Hunting team suggests the following XQL queries. Cortex XDR and XSIAM customers can use these XQL queries to search for signs of exploitation.

// Title: TeamPCP Process Execution Artifacts
// Description: Identifies hardcoded components in the deployed payloads - relies on the fact that the python process is being used to execute sub processes with hardcoded command parameters
// MITRE ATT&CK TTP ID: T1059
config case\_sensitive = false
| dataset = xdr\_data
| fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, actor\_process\_image\_name, action\_process\_image\_command\_line, action\_process\_image\_sha256, action\_process\_image\_name, action\_process\_image\_path, agent\_hostname, agent\_id
| filter event\_type = ENUM.PROCESS and event\_sub\_type in (ENUM.PROCESS\_START) and action\_process\_image\_name in ("openssl", "tar", "curl", "systemctl", "python") and action\_process\_image\_command\_line ~= "(?:tpcp\.tar\.gz|\-inkey p \-in session\.key|models\.litellm\.cloud|payload\.enc|session\.key\.enc| sysmon\.service|openssl rand -out .+session\.key|import base64; exec\(base64.b64decode\(\')"

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | // Title: TeamPCP Process Execution Artifacts    // Description: Identifies hardcoded components in the deployed payloads - relies on the fact that the python process is being used to execute sub processes with hardcoded command parameters    // MITRE ATT&CK TTP ID: T1059    config case\_sensitive = false  | dataset = xdr\_data  | fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, actor\_process\_image\_name, action\_process\_image\_command\_line, action\_process\_image\_sha256, action\_process\_image\_name, action\_process\_image\_path, agent\_hostname, agent\_id  | filter event\_type = ENUM.PROCESS and event\_sub\_type in (ENUM.PROCESS\_START) and action\_process\_image\_name in ("openssl", "tar", "curl", "systemctl", "python") and action\_process\_image\_command\_line ~= "(?:tpcp\.tar\.gz|\-inkey p \-in session\.key|models\.litellm\.cloud|payload\.enc|session\.key\.enc| sysmon\.service|openssl rand -out .+session\.key|import base64; exec\(base64.b64decode\(\')" |

// Title: TeamPCP File Creation Artifacts
// Description: Identifies file artifacts related to the TeamPCP enumeration, persistence and exfiltration activity
// MITRE ATT&CK TTP ID: T1074
dataset = xdr\_data
| fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, action\_file\_path, action\_file\_name, action\_file\_sha256, actor\_process\_image\_name, agent\_hostname, agent\_id
| filter event\_type = ENUM.FILE and event\_sub\_type in (ENUM.FILE\_CREATE\_NEW, ENUM.FILE\_WRITE) and (action\_file\_name in ("session.key", "payload.enc", "session.key.enc", "tpcp.tar.gz", "sysmon.service", "pglog", ".pg\_state") and actor\_process\_image\_name in ("python\*", "openssl"))

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | // Title: TeamPCP File Creation Artifacts  // Description: Identifies file artifacts related to the TeamPCP enumeration, persistence and exfiltration activity  // MITRE ATT&CK TTP ID: T1074  dataset = xdr\_data  | fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, action\_file\_path, action\_file\_name, action\_file\_sha256, actor\_process\_image\_name, agent\_hostname, agent\_id  | filter event\_type = ENUM.FILE and event\_sub\_type in (ENUM.FILE\_CREATE\_NEW, ENUM.FILE\_WRITE) and (action\_file\_name in ("session.key", "payload.enc", "session.key.enc", "tpcp.tar.gz", "sysmon.service", "pglog", ".pg\_state") and actor\_process\_image\_name in ("python\*", "openssl")) |

// Title: TeamPCP Network Artifacts
// Description: AWS and Kube API interaction from a single python process indicative of the enumeration and lateral movement observed by TeamPCP
// MITRE ATT&CK TTP ID: T1021.007
dataset = xdr\_data
| fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, actor\_process\_image\_name, uri, actor\_process\_instance\_id, agent\_hostname, agent\_id
| filter event\_type in (ENUM.STORY, ENUM.NETWORK) and uri ~= "(?:/api/v1/namespaces/.+/secrets|/api/v1/secrets|/api/v1/namespaces|/api/v1/nodes|/api/v1/namespaces/kube-system/pods|/latest/meta-data/iam/security-credentials/|/latest/api/token)" and actor\_process\_image\_name contains "python"
| comp values(agent\_hostname) as agent\_hostname, values(actor\_process\_command\_line) as actor\_process\_command\_line, values(uri) as uri, count\_distinct(uri) as uri\_cnt by actor\_process\_image\_name, actor\_process\_instance\_id
| filter uri\_cnt > 3

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | // Title: TeamPCP Network Artifacts    // Description: AWS and Kube API interaction from a single python process indicative of the enumeration and lateral movement observed by TeamPCP    // MITRE ATT&CK TTP ID: T1021.007    dataset = xdr\_data  | fields event\_type, event\_id, event\_sub\_type, actor\_process\_image\_path, actor\_process\_command\_line, actor\_process\_image\_name, uri, actor\_process\_instance\_id, agent\_hostname, agent\_id  | filter event\_type in (ENUM.STORY, ENUM.NETWORK) and uri ~= "(?:/api/v1/namespaces/.+/secrets|/api/v1/secrets|/api/v1/namespaces|/api/v1/nodes|/api/v1/namespaces/kube-system/pods|/latest/meta-data/iam/security-credentials/|/latest/api/token)" and actor\_process\_image\_name contains "python"  | comp values(agent\_hostname) as agent\_hostname, values(actor\_process\_command\_line) as actor\_process\_command\_line, values(uri) as uri, count\_distinct(uri) as uri\_cnt by actor\_process\_image\_name, actor\_process\_instance\_id  | filter uri\_cnt > 3 |

## Conclusion

Based on the rapid escalation of TeamPCP’s supply chain operations, Palo Alto Networks highly recommends that organizations immediately audit the following within their development and production environments:

* CI/CD pipelines
* GitHub PATs
* Cloud provider credentials
* Kubernetes service account tokens (SATs)
* Container-based SSH keys

Between February and March 2026, this actor moved from ransomware and cryptomining to a focused supply chain compromise model. This operation has successfully compromised trusted security tools like Aqua Security Trivy and Checkmarx KICS as well as the BerriAI LiteLLM gateway.

Organizations should prioritize the implementation of the interim guidance provided in this brief, specifically regarding SBOM visibility and CI/CD policy hardening, to mitigate the risk of lateral movement and data exfiltration.

Palo Alto Networks customers are better protected by our products, as listed below. We will update this threat brief as more relevant information becomes available.

## Palo Alto Networks Product Protections for TeamPCP’s Multi-Stage Supply Chain Attack

Palo Alto Networks customers can leverage a variety of product protections and updates to identify and defend against this threat.

[Cortex Cloud’s](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) OotB supply chain best practices are designed to recognize the use of unpinned Trivy and LiteLLM owned CI/CD pipelines within an environment and provide alerting. We encourage organizations to pin specific and known package versions for their supply chain applications.

Figure 8 shows what Cortex Cloud’s platform will display when viewing Supply Chain Catalogs for Trivy, Checkmarx and LiteLLM. Figure 9 shows what it will display for the Application Security coverage for assets in an environment. Figure 10 shows notable findings of secrets contained within potentially vulnerable cloud resources.

![Screenshot of a Supply Chain Catalog search results from Cortex Cloud. The query includes trivy, checkmarx, and litellm.]()

Figure 8. Cortex Cloud Application Security Module: Supply Chain Packages catalog.

![Dashboard in Cortex Cloud displaying ASPM Coverage statistics: 20% of assets are scanned. Sections include data on vulnerabilities, code weaknesses, secrets, misconfigurations, and malware, all at 0%. Two assets are listed with details like asset type and last scan status, both marked as completed using GitHub Actions.]()

Figure 9. Cortex Cloud Application Security Module: Coverage display.

![Dashboard in Cortex Cloud displaying a list of security issues labeled as "Secrets." It shows several entries with varying severity levels, including high and low.The entries show associated assets and have options for additional actions.]()

Figure 10. Cortex Cloud Application Security Module: Detected Secrets display.

The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you might have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 000 800 050 45107
* South Korea: +82.080.467.8774

### Cloud-Delivered Security Services for the Next-Generation Firewall

[Advanced URL Filtering](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-new-features/url-filtering-features/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.

### Cortex AgentiX

Security analysts can use natural language to prompt the [Cortex AgentiX](https://www.paloaltonetworks.com/cortex/agentix) Threat Intel agent to extract file indicators of compromise (IoCs) from this threat brief. Organizations will then need to enrich the case and maintain awareness in their Cortex tenant for related alerts. The AgentiX agent will provide a quick summary of the impact to the organization. Analysts can also leverage the Case Investigation agent for more details on cases and artifacts associated with this campaign and/or build a response plan of action.

### Cortex XDR and XSIAM

[Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) provide a multi-layer defense — including Behavioral Threat Protection (BTP), Advanced WildFire and Cortex Analytics — to help protect against the initial access, C2 and potential lateral movement described in this article.

### Cortex Xpanse

[Cortex Xpanse](https://docs-cortex.paloaltonetworks.com/p/XPANSE) has the ability to identify exposed LiteLLM devices on the public internet and escalate these findings to defenders. Customers can enable alerting on this risk by ensuring that the LiteLLM Attack Surface Rule is enabled. Identified findings can either be viewed in the Threat Response Center or in the incident view of Expander. These findings are also available for Cortex XSIAM customers who have purchased the ASM module.

### Cortex Cloud

* [Cortex Cloud](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) customers are better protected from the topics discussed within this article through the proper placement of Cortex Cloud [XDR endpoint agent](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) and [serverless agents](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Premium-Documentation/Use-cases) within a cloud environment. Designed to protect a cloud’s posture and runtime operations against these threats, Cortex Cloud helps detect and prevent the malicious operations or configuration alterations or exploitations discussed within this article.
* Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG), as well as Identity Threat Detection and Response (ITDR), providing clients with the necessary capabilities to improve their identity-related security requirements. The Identity Security modules provides visibility into identities and their permissions within cloud environments to accurately detect misconfigurations and unwanted access to sensitive data. Providing real-time analysis surrounding usage and access patterns designed to maintain security monitoring.
* Cortex Cloud’s Application Security Module ([ASPM](https://www.paloaltonetworks.com/cortex/cloud/application-security-posture-management)) supports ingesting security audit logs and findings from third-party SaaS vendors discussed within this article, as well as prioritizing alerts, issues, policies and assets based on ingested applications. This allows security teams to maintain better security awareness across their on-prem and cloud environment and alert upon the threats discussed within this article.

|  |  |
| --- | --- |
| **Alert Name** | **MITRE ATT&CK Tactic** |
| [Unusual Kubernetes service account file read](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Unusual-Kubernetes-service-account-file-read) | Credential Access (TA0006) |
| [Unusual cloud Instance Metadata Service (IMDS) access](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Unusual-cloud-Instance-Metadata-Service-IMDS-access) | Credential Access (TA0006) |
| [Suspicious access to cloud credential files](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Suspicious-access-to-cloud-credential-files) | Credential Access (TA0006) |
| [Kubernetes secret value extraction activity](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Kubernetes-secret-enumeration-activity) | Credential Access (TA0006) |

### Next-Generation Firewalls With Advanced Threat Prevention

[Next-Generation Firewall](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-new-features/url-filtering-features/advanced-url-filtering) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/dns-security) security subscription can help block the attack via the following Threat Prevention signature: [87120](https://threatvault.paloaltonetworks.com/?q=87120).

## Indicators of Compromise

### IP Addresses

* 23.142.184[.]129
* 45.148.10[.]212
* 63.251.162[.]11
* 83.142.209[.]11
* 83.142.209[.]203
* 195.5.171[.]242
* 209.34.235[.]18
* 212.71.124[.]188

### Domains

* checkmarx[.]zone
* models.litellm[.]cloud
* scan.aquasecurtiy[.]org
* tdtqy-oyaaa-aaaae-af2dq-cai.raw.icp0[.]io

### Tunneling URLs

* championships-peoples-point-cassette.trycloudflare[.]com
* create-sensitivity-grad-sequence.trycloudflare[.]com
* investigation-launches-hearings-copying.trycloudflare[.]com
* plug-tab-protective-relay.trycloudflare[.]com
* souls-entire-defined-routes.trycloudflare[.]com

### SHA256 Hashes for Self-signed Certificates Used in the Malware

* 30015DD1E2CF4DBD49FFF9DDEF2AD4622DA2E60E5C0B6228595325532E948F14
* 41C4F2F37C0B257D1E20FE167F2098DA9D2E0A939B09ED3F63BC4FE010F8365C
* D8CAF4581C9F0000C7568D78FB7D2E595AB36134E2346297D78615942CBBD727

### Filenames

* kamikaze[.]sh
* kube[.]py
* prop[.]py
* proxy\_server[.]py
* tpcp.tar[.]gz

### SHA256 Hashes for the Malicious Files

* 0880819ef821cff918960a39c1c1aada55a5593c61c608ea9215da858a86e349
* 0c0d206d5e68c0cf64d57ffa8bc5b1dad54f2dda52f24e96e02e237498cb9c3a
* 0c6a3555c4eb49f240d7e0e3edbfbb3c900f123033b4f6e99ac3724b9b76278f
* 18a24f83e807479438dcab7a1804c51a00dafc1d526698a66e0640d1e5dd671a
* 1e559c51f19972e96fcc5a92d710732159cdae72f407864607a513b20729decb
* 5e2ba7c4c53fa6e0cef58011acdd50682cf83fb7b989712d2fcf1b5173bad956
* 61ff00a81b19624adaad425b9129ba2f312f4ab76fb5ddc2c628a5037d31a4ba
* 6328a34b26a63423b555a61f89a6a0525a534e9c88584c815d937910f1ddd538
* 7321caa303fe96ded0492c747d2f353c4f7d17185656fe292ab0a59e2bd0b8d9
* 7b5cc85e82249b0c452c66563edca498ce9d0c70badef04ab2c52acef4d629ca
* 7df6cef7ab9aae2ea08f2f872f6456b5d51d896ddda907a238cd6668ccdc4bb7
* 822dd269ec10459572dfaaefe163dae693c344249a0161953f0d5cdd110bd2a0
* 887e1f5b5b50162a60bd03b66269e0ae545d0aef0583c1c5b00972152ad7e073
* bef7e2c5a92c4fa4af17791efc1e46311c0f304796f1172fce192f5efc40f5d7
* c37c0ae9641d2e5329fcdee847a756bf1140fdb7f0b7c78a40fdc39055e7d926
* cd08115806662469bbedec4b03f8427b97c8a4b3bc1442dc18b72b4e19395fe3
* d5edd791021b966fb6af0ace09319ace7b97d6642363ef27b3d5056ca654a94c
* e4edd126e139493d2721d50c3a8c49d3a23ad7766d0b90bc45979ba675f35fea
* e6310d8a003d7ac101a6b1cd39ff6c6a88ee454b767c1bdce143e04bc1113243
* e64e152afe2c722d750f10259626f357cdea40420c5eedae37969fbf13abbecf
* e87a55d3ba1c47e84207678b88cacb631a32d0cb3798610e7ef2d15307303c49
* e9b1e069efc778c1e77fb3f5fcc3bd3580bbc810604cbf4347897ddb4b8c163b
* ecce7ae5ffc9f57bb70efd3ea136a2923f701334a8cd47d4fbf01a97fd22859c
* f398f06eefcd3558c38820a397e3193856e4e6e7c67f81ecc8e533275284b152
* f7084b0229dce605ccc5506b14acd4d954a496da4b6134a294844ca8d601970d

*Updated April 9, 2026, at 8:00 a.m. PT to add Advanced Threat Prevention coverage.*

Back to top

### Tags

* [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
* [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
* [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/ "Infostealer")
* [Python](https://unit42.paloaltonetworks.com/tag/python/ "Python")
* [Supply chain](https://unit42.paloaltonetworks.com/tag/supply-chain/ "supply chain")
* [Wiper](https://unit42.paloaltonetworks.com/tag/wiper/ "wiper")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Double Agents: Exposing Security Blind Spots in GCP Vertex AI](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/ "Double Agents: Exposing Security Blind Spots in GCP Vertex AI")

### Table of Contents

### Related Articles

* [The npm Threat Landscape: Attack Surface and Mitigations (Updated May 1)](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "article - table of contents")
* [That AI Extension Helping You Write Emails? It’s Reading Them First](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "article - table of contents")
* [Threat Brief: Escalation of Cyber Risk Related to Iran (Updated April 17)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/ "article - table of contents")

## Related Malware Resources

![Pictorial representation of the npm packages supply chain attack. Screen displaying code with a prominent alert symbol and the words 'VIRUS DETECTED' highlighted in red.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/05_Malware_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 1, 2026
[#### The npm Threat Landscape: Attack Surface and Mitigations (Updated May 1)](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)

* [Credential Harvesting](https://unit42.paloaltonetworks.com/tag/credential-harvesting/ "Credential Harvesting")
* [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
* [Npm packages](https://unit42.paloaltonetworks.com/tag/npm-packages/ "npm packages")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "The npm Threat Landscape: Attack Surface and Mitigations (Updated May 1)")

![Pictorial representation of high-risk GenAI and agentic browser extensions. A person interacts with a digital screen displaying an AI symbol, circuit patterns, and various technology icons.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/AdobeStock_739390615-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 30, 2026
[#### That AI Extension Helping You Write Emails? It’s Reading Them First](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/)

* [AI browser](https://unit42.paloaltonetworks.com/tag/ai-browser/ "AI browser")
* [Browser extension](https://unit42.paloaltonetworks.com/tag/browser-extension/ "browser extension")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "That AI Extension Helping You Write Emails? It’s Reading Them First")

![Pictorial representation of AirSnitch attacks on enterprise wireless infrastructure. A globe with the continents illuminated in blue lighting and scattered red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/11_Security-Technology_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 22, 2026
[#### When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/)

* [AirSnitch](https://unit42.paloaltonetworks.com/tag/airsnitch/ "AirSnitch")
* [MitM](https://unit42.paloaltonetworks.com/tag/mitm/ "MitM")
* [Network security](https://unit42.paloaltonetworks.com/tag/network-security/ "network security")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/ "When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks")

![Pictorial representation of Iran cyber attacks. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) April 17, 2026
[#### Threat Brief: Escalation of Cyber Risk Related to Iran (Updated April 17)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/)

* [APK](https://unit42.paloaltonetworks.com/tag/apk/ "APK")
* [DDoS attacks](https://unit42.paloaltonetworks.com/tag/ddos-attacks/ "DDoS attacks")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/ "Threat Brief: Escalation of Cyber Risk Related to Iran (Updated April 17)")

![Pictorial representation of "Agent God Mode" in Amazon Bedrock AgentCore. A futuristic digital landscape depicting cloud technology with glowing orange and blue circuits. Several cloud icons are connected by circuits, symbolizing a network.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/03_Cloud_cybersecurity_research_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 8, 2026
[#### Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/)

* [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
* [AI agents](https://unit42.paloaltonetworks.com/tag/ai-agents/ "AI agents")
* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "Cracks in the Bedrock: Agent God Mode")

![Pictorial representation of the AWS AgentCore Sandbox. Digital illustration of a 3D cloud made up of glowing lights and dots with a padlock on its front. It floats above a glowing network of dots and lines.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/05_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 7, 2026
[#### Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/)

* [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
* [Agentcore runtime](https://unit42.paloaltonetworks.com/tag/agentcore-runtime/ "agentcore runtime")
* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ "Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/03_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 6, 2026
[#### Understanding Current Threats to Kubernetes Environments](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/)

* [Audit logs](https://unit42.paloaltonetworks.com/tag/audit-logs/ "audit logs")
* [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
* [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/ "Understanding Current Threats to Kubernetes Environments")

![Pictorial representation of Amazon Bedrock's multi-agent applications. A digital illustration depicting complex data flow and connectivity. Numerous lines and nodes extend outward from a central point, resembling a neural network or digital web, against a dark background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/AdobeStock_260323351-2-660x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 3, 2026
[#### When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/)

* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [Amazon](https://unit42.paloaltonetworks.com/tag/amazon/ "Amazon")
* [Bedrock](https://unit42.paloaltonetworks.com/tag/bedrock/ "bedrock")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/ "When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications")

![Pictorial representation of the supply chain attack compromising Axios. A giant eye made of glowing binary code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/02_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) April 1, 2026
[#### Threat Brief: Widespread Impact of the Axios Supply Chain Attack](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/)

* [API attacks](https://unit42.paloaltonetworks.com/tag/api-attacks/ "API attacks")
* [JavaScript](https://unit42.paloaltonetworks.com/tag/javascript/ "JavaScript")
* [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/ "Threat Brief: Widespread Impact of the Axios Supply Chain Attack")

* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)
![Enlarged Image]()
