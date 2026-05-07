---
title: "Threat Brief: Salesloft Drift Integration Used To Compromise Salesforce Instances"
date: "2025-09-02"
url: https://unit42.paloaltonetworks.com/threat-brief-compromised-salesforce-instances/
source: unit42
---

# Threat Brief: Salesloft Drift Integration Used To Compromise Salesforce Instances

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/ "High Profile Threats")
* [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/ "Vulnerabilities")

[Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

# Threat Brief: Salesloft Drift Integration Used To Compromise Salesforce Instances

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  4  min read

Related Products

[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Unit 42](https://unit42.paloaltonetworks.com/author/unit42/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:September 2, 2025
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/)
  + [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Credential-based attacks](https://unit42.paloaltonetworks.com/tag/credential-based-attacks/)
  + [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/)
  + [Salesforce](https://unit42.paloaltonetworks.com/tag/salesforce/)
  + [Salesloft](https://unit42.paloaltonetworks.com/tag/salesloft/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/threat-brief-compromised-salesforce-instances/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/threat-brief-compromised-salesforce-instances/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Threat%20Brief:%20Salesloft%20Drift%20Integration%20Used%20To%20Compromise%20Salesforce%20Instances&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F&title=Threat%20Brief:%20Salesloft%20Drift%20Integration%20Used%20To%20Compromise%20Salesforce%20Instances "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F&text=Threat%20Brief:%20Salesloft%20Drift%20Integration%20Used%20To%20Compromise%20Salesforce%20Instances "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Threat%20Brief:%20Salesloft%20Drift%20Integration%20Used%20To%20Compromise%20Salesforce%20Instances%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fthreat-brief-compromised-salesforce-instances%2F "Share in Mastodon")

## Executive Summary

Unit 42 stopped monitoring this threat and updating the brief on Dec. 2, 2025. Please refer to the Salesloft website for the latest information.

Unit 42 has observed activity consistent with a specific threat actor campaign leveraging the Salesloft Drift integration to compromise customer Salesforce instances. This brief provides information about our observations and guidance for potentially affected organizations.

As detailed in a [recent notification from Salesloft](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Notification), from August 8-18, 2025, a threat actor utilized compromised OAuth credentials to exfiltrate data from affected customers’ Salesforce environments.

Our observations indicate that the threat actor performed mass exfiltration of sensitive data from various Salesforce objects, including Account, Contact, Case and Opportunity records. Following exfiltration, the actor appeared to be actively scanning the acquired data for credentials, likely with the intent to facilitate further attacks or expand their access. We have observed that the threat actor deleted queries to hide evidence of the jobs they run, likely as an anti-forensics technique.

Salesloft has confirmed that all impacted customers have been notified and took immediate action to secure its systems and contain and mitigate the incident, including proactively revoking all active access and refresh tokens for the Drift application, necessitating re-authentication for affected administrators.

Palo Alto Networks recommends that organizations continue to monitor Salesforce and Salesloft updates, in addition to following any recommendations shared below.

The [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) can also be engaged to help with a compromise or to provide a proactive assessment to lower your risk.

| **Related Unit 42 Topics** | [**High Profile Threats**](https://unit42.paloaltonetworks.com/category/top-cyberthreats/), **[Data Exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/)** |
| --- | --- |

## Recommendations for Organizations

Organizations that utilize the Salesloft Drift integration with Salesforce should treat this incident with immediate urgency. Beyond the proactive steps Salesloft took to secure its platform (such as token revocation), the following recommendations are critical to assess potential impact and mitigate further risk:

**Immediate Investigation and Log Review:**

* **Drift API Integrations:** Conduct a thorough review of all Drift integrations and review all authentication activity within third-party systems for signs of suspicious connections, credential harvesting and data exfiltration.
* **Salesforce Logs:** Conduct a thorough review of Salesforce login history, audit trails and API access logs for the period of August 8 to present. Specifically, examine Salesforce Event Monitoring logs, if enabled, for unusual activity associated with the Drift connection user and review authentication activity from the Drift Connected App. Look for suspicious login attempts, unusual data access patterns, and the indicators mentioned in the [Hunting Guidance](#post-155472-_c9700x6sm03h) section, such as the Python/3.11 aiohttp/3.12.15 user agent string and activity from known threat actor IP addresses. Also, review UniqueQuery events that log executed Salesforce Object Query Language (SOQL) queries to identify which Salesforce objects (e.g., Account, Contact, Opportunity, Case, etc.) and which fields within those objects the attacker queried. Consider opening a Salesforce support case to obtain specific queries used by the threat actor if needed.
* **Identity Provider Logs:** Review logs from your Identity Provider (IdP) for any unusual authentication attempts or successful logins to Salesforce or other integrated applications during the incident period.
* **Network Logs:** Analyze network flow logs and proxy logs for connections to Salesforce from suspicious IPs or unusual data transfer volumes.

**Review and Rotate Exposed Credentials:**

* **Automated Tools:** Leverage automated tools (e.g., Trufflehog, GitLeaks) to efficiently scan for secrets and hardcoded credentials within code repositories, configuration files or any potentially exfiltrated data.
* **Data Scrutiny:** If exfiltration is confirmed or suspected, review data for the presence of sensitive credentials. This includes searching for patterns like AWS access key identifiers (e.g., AKIA), Snowflake credentials (e.g., Snowflake or snowflakecomputing[.]com), generic keywords such as password, secret or key, and strings related to organization-specific login URLs (e.g., VPN or SSO login pages).
* **Immediate Rotation:** Promptly rotate all credentials identified as exposed within the exfiltrated data. This includes, but is not limited to, Salesforce API keys, connected app credentials and any other system credentials found within the compromised data.

## Hunting Guidance

Organizations concerned about potential compromise related to the Salesloft Drift integration incident should immediately initiate proactive threat hunting activities within their Salesforce environments. (As a starting point, Salesforce provides some resources for [investigating Salesforce security incidents](https://www.salesforce.com/blog/a-primer-on-forensic-investigation-of-salesforce-security-incidents/).) A critical first step involves a thorough review of Salesforce login and activity logs for specific indicators of compromise (IoCs) associated with the threat actor.

Defenders should look for logins originating from suspicious IP addresses, including but not limited to known threat actor IP addresses (for info and advice, please see the Indicators of Compromise section of this report).

Of particular interest is the presence of the user agent string Python/3.11 aiohttp/3.12.15 associated with these login events. While this specific string is a valid user agent that is not inherently malicious, it is also indicative of the automated, high-volume data exfiltration observed in this campaign.

The presence of this string is significant because threat actors can leverage asynchronous Python libraries like aiohttp in combination with Salesforce's Bulk API to perform rapid, high-throughput data exfiltration. This pairing allows them to efficiently extract significant volumes of data from Salesforce objects such as Account, Contact, Case and Opportunity, minimizing their time on target.

## Conclusion

Palo Alto Networks highly recommends rotating credentials and following the above guidance to validate authentication activity for Drift integrations. Vigilance and verification are key.

Organizations should be wary of social engineering attempts resulting from this or any other data exfiltration event.

Best practices include:

* Be Skeptical of Unsolicited Communications: Advise your teams to carefully scrutinize any unsolicited or unusual emails, calls or messages, even if they appear to be from a trusted source.
* Verify Requests: Always verify requests for sensitive data or credentials through a separate, official communication channel before taking any action. For instance, if you receive a suspicious email from a colleague, call them directly to confirm the request is legitimate. Only exchange information and files through our Customer Support Portal, not email.
* Implement Zero Trust Principles: Enforcing a Zero Trust posture with conditional access policies and the principle of least privilege can significantly limit an attacker's ability to move laterally within your network, even if they successfully trick an employee.

For more information about social engineering and how to mitigate it, please see our recent [2025 Unit 42 Global Incident Response Report: Social Engineering Edition](https://unit42.paloaltonetworks.com/2025-unit-42-global-incident-response-report-social-engineering-edition/).

Palo Alto Networks and Unit 42 will continue to monitor the situation for updated information, and we will update this threat brief with additional information if any becomes available.

Salesforce will be providing [updates and resources to customers](https://help.salesforce.com/s/articleView?id=005134951&type=1).

If you think you might have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 000 800 050 45107

## Indicators of Compromise

Salesloft made some [IoCs](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Notification) available for hunting. It is worth noting that many of the IP addresses listed in their notification are Tor exit nodes and may have a high false positive rate for organizations that allow Tor connections.

## Additional Resources

* [Salesforce-Connected Third-Party Drift Application Incident Response](https://www.paloaltonetworks.com/blog/2025/09/salesforce-third-party-application-incident-response/) – Palo Alto Networks

*Updated Sept. 2, 2025, at 1:50 p.m. PT to add Additional Resources section*

Back to top

### Tags

* [Credential-based attacks](https://unit42.paloaltonetworks.com/tag/credential-based-attacks/ "credential-based attacks")
* [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")
* [Salesforce](https://unit42.paloaltonetworks.com/tag/salesforce/ "Salesforce")
* [Salesloft](https://unit42.paloaltonetworks.com/tag/salesloft/ "Salesloft")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Data Is the New Diamond: Heists in the Digital Age](https://unit42.paloaltonetworks.com/retail-hospitality-heists-in-the-digital-age/ "Data Is the New Diamond: Heists in the Digital Age")

### Table of Contents

### Related Articles

* [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "article - table of contents")
* [Fracturing Software Security With Frontier AI Models](https://unit42.paloaltonetworks.com/ai-software-security-risks/ "article - table of contents")
* [Double Agents: Exposing Security Blind Spots in GCP Vertex AI](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/ "article - table of contents")

## Related Vulnerabilities Resources

![Pictorial representation of CVE-2026-30300. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/06_Vulnerabilities_1920x900-3-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 6, 2026
[#### Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution](https://unit42.paloaltonetworks.com/captive-portal-zero-day/)

* [CVE-2026-0300](https://unit42.paloaltonetworks.com/tag/cve-2026-0300/ "CVE-2026-0300")
* [EarthWorm](https://unit42.paloaltonetworks.com/tag/earthworm/ "EarthWorm")
* [PAN-OS](https://unit42.paloaltonetworks.com/tag/pan-os/ "PAN-OS")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution")

![Pictorial representation of a severe Linux vulnerability. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/05_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 5, 2026
[#### Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/)

* [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
* [CVE-2026-31431](https://unit42.paloaltonetworks.com/tag/cve-2026-31431/ "CVE-2026-31431")
* [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years")

![Pictorial representation of CVE-2023-33538. Abstract image of a glowing red Wi-Fi symbol on a circuit board, with intricate patterns and a futuristic appearance.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/04_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 16, 2026
[#### A Deep Dive Into Attempted Exploitation of CVE-2023-33538](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/)

* [Botnet](https://unit42.paloaltonetworks.com/tag/botnet/ "botnet")
* [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
* [CVE-2023-33538](https://unit42.paloaltonetworks.com/tag/cve-2023-33538/ "CVE-2023-33538")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/ "A Deep Dive Into Attempted Exploitation of CVE-2023-33538")

![Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 19, 2026
[#### VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)

* [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
* [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
* [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731)")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 17, 2026
[#### Critical Vulnerabilities in Ivanti EPMM Exploited](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)

* [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
* [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
* [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 30, 2026
[#### Privileged File System Vulnerability Present in a SCADA System](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)

* [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
* [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
* [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Pictorial representation of MongoBleed, CVE-2025-14847. Digital image featuring a glowing padlock icon superimposed on a background of streaming blue binary code, symbolizing cybersecurity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/AdobeStock_233494953-786x429.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) January 13, 2026
[#### Threat Brief: MongoDB Vulnerability (CVE-2025-14847)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/)

* [CVE-2025-14847](https://unit42.paloaltonetworks.com/tag/cve-2025-14847/ "CVE-2025-14847")
* [MongoDB](https://unit42.paloaltonetworks.com/tag/mongodb/ "MongoDB")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/mongobleed-cve-2025-14847/ "Threat Brief: MongoDB Vulnerability (CVE-2025-14847)")

![Pictorial representation of remote code execution in AI and machine learning libraries. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/05_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 13, 2026
[#### Remote Code Execution With Modern AI/ML Formats and Libraries](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)

* [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
* [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
* [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/ "Remote Code Execution With Modern AI/ML Formats and Libraries")

![Pictorial representation of CVE-2025-55182 (React) and CVE-2025-66478 (Next.js). Close-up of a digital display on electronic equipment with illuminated text reading "SYSTEM HACKED" in red, set against a blurred background of blue and red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/12/02_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) December 12, 2025
[#### Exploitation of Critical Vulnerability in React Server Components (Updated December 12)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/)

* [Cobalt Strike](https://unit42.paloaltonetworks.com/tag/cobalt-strike/ "Cobalt Strike")
* [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
* [CVE-2025-66478](https://unit42.paloaltonetworks.com/tag/cve-2025-66478/ "CVE-2025-66478")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/ "Exploitation of Critical Vulnerability in React Server Components (Updated December 12)")

![Pictorial representation of an authentication coercion attack. Panoramic view of a city skyline at night, featuring vibrant light beams from skyscrapers and a deep blue sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/07_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) November 10, 2025
[#### You Thought It Was Over? Authentication Coercion Keeps Evolving](https://unit42.paloaltonetworks.com/authentication-coercion/)

* [Mimikatz](https://unit42.paloaltonetworks.com/tag/mimikatz/ "Mimikatz")
* [PrintNightmare](https://unit42.paloaltonetworks.com/tag/printnightmare/ "PrintNightmare")
* [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/authentication-coercion/ "You Thought It Was Over? Authentication Coercion Keeps Evolving")

* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)
![Enlarged Image]()
