---
title: "Auditing the Gatekeepers: Fuzzing "AI Judges" to Bypass Security Controls"
date: "2026-03-10"
url: https://unit42.paloaltonetworks.com/fuzzing-ai-judges-security-bypass/
source: unit42
---

# Auditing the Gatekeepers: Fuzzing "AI Judges" to Bypass Security Controls

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")

[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Auditing the Gatekeepers: Fuzzing "AI Judges" to Bypass Security Controls

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  5  min read

Related Products

[![Code to Cloud Platform icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Code to Cloud Platform](https://unit42.paloaltonetworks.com/product-category/code-to-cloud-platform/ "Code to Cloud Platform")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Tony Li](https://unit42.paloaltonetworks.com/author/tony-li/)
  + [Hongliang Liu](https://unit42.paloaltonetworks.com/author/hongliang-liu/)
  + [Yuhao Wu](https://unit42.paloaltonetworks.com/author/yuhao-wu/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 10, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Malware](https://unit42.paloaltonetworks.com/category/malware/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [AI](https://unit42.paloaltonetworks.com/tag/ai/)
  + [Fuzzing](https://unit42.paloaltonetworks.com/tag/fuzzing/)
  + [LLM](https://unit42.paloaltonetworks.com/tag/llm/)
  + [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/fuzzing-ai-judges-security-bypass/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/fuzzing-ai-judges-security-bypass/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Auditing%20the%20Gatekeepers:%20Fuzzing%20"AI%20Judges"%20to%20Bypass%20Security%20Controls&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F&title=Auditing%20the%20Gatekeepers:%20Fuzzing%20AI%20Judges%20to%20Bypass%20Security%20Controls "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F&text=Auditing%20the%20Gatekeepers:%20Fuzzing%20"AI%20Judges"%20to%20Bypass%20Security%20Controls "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Auditing%20the%20Gatekeepers:%20Fuzzing%20AI%20Judges%20to%20Bypass%20Security%20Controls%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ffuzzing-ai-judges-security-bypass%2F "Share in Mastodon")

## Executive Summary

As organizations scale AI operations, they increasingly deploy AI judges — large language models (LLMs) acting as automated security gatekeepers to enforce safety policies and evaluate output quality. Our research investigates a critical security issue in these systems: They can be manipulated into authorizing policy violations through stealthy input sequences, a type of prompt injection.

To do this investigation, we designed an automated fuzzer for internal use for red-team style assessments called AdvJudge-Zero. Fuzzers are tools that identify software vulnerabilities by providing unexpected input, and we apply the same approach to attacking AI judges. It identifies specific trigger sequences that exploit a model's decision-making logic to bypass security controls.

Unlike previous adversarial attacks that produce detectable gibberish, our research proves that effective attacks can be entirely stealthy, using benign formatting symbols to reverse a block decision to allow.

By examining how this tool works, we can more easily see the security issues inherent in AI judges used by current LLMs.

Palo Alto Networks customers are better protected from this type of issue through the following products and services:

* [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help empower safe AI use and development.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | **[AI](https://unit42.paloaltonetworks.com/tag/ai/), [LLM](https://unit42.paloaltonetworks.com/tag/llm/), [Prompt Injection,](https://unit42.paloaltonetworks.com/tag/prompt-injection/) Fuzzing** |

## Background

In modern AI architectures, AI judges often serve as the final line of defense. These automated gatekeepers are responsible for enforcing safety policies (e.g., "Is this response harmful?") and evaluating performance. Our research tool, AdvJudge-Zero, treats LLMs as opaque boxes to be audited, revealing that AI judges can be subject to exploitable logic bugs of their own.

## The Methodology: Automated Predictive Fuzzing

Previous adversarial attacks on AI judges have required clear-box access. With full visibility to the internal structure of the system, pen-testers can rely on mathematical routines to force model errors. This often results in high-entropy gibberish that is easily detected.

In contrast, AdvJudge-Zero employs an automated fuzzing approach. The tool interacts with an LLM strictly as a user would, using search algorithms to exploit the model's own predictive nature.

### The Steps

**1. Token discovery via next-token distribution**

The process begins by querying the model to identify expected inputs based on its own next-token distribution.

* **Natural language patterns**: Our tool probes the model to generate potential trigger phrases based on common linguistic structures.
* **Stealth prioritization**: It specifically identifies stealth control tokens — innocent-looking characters such as standard markdown syntax or formatting symbols. These possess low perplexity (meaning they appear natural and predictable to the AI) but carry strong influence over the model's attention.

**2. Iterative refinement and logit-gap analysis**

Once candidate tokens are collected, the system enters a refinement phase.

* **Decision boundary testing**: The fuzzer iteratively tests these inputs to measure the decision shift.
* **Measuring the logit-gap**: It monitors the [logit-gap](https://unit42.paloaltonetworks.com/logit-gap-steering-impact/) — the mathematical margin of confidence — between the yes (allow) and no (block) tokens. By observing which formatting tokens minimize the probability of a block decision, the tool identifies weak points in the model's logic.

By observing which innocent-looking formatting tokens minimize the probability of a block decision, the tool identifies the weak points in the model's logic.

**3. Exploitation: isolating the decisive control elements**

The final stage of AdvJudge-Zero's process isolates specific tokens that act as decisive control elements. These refined sequences steer the model’s internal attention mechanism toward an approval state, leading to a yes decision regardless of the actual input content.

### The Security Issue: Innocent-Looking Triggers

The most alarming finding for security professionals is the stealth of these attacks. AI judges are highly sensitive to innocent-looking characters that act as logical triggers. To a human observer or a web application firewall (WAF), these look like standard data formatting. To the AI judge, they shift the model into compliance mode.

Effective triggers identified include:

* **Formatting symbols**: List markers (1., -), newlines (\n) or markdown headers (###)
* **Structural tokens**: Role indicators (e.g., User:, Assistant: ) or system tags
* **Context shifts**: Phrases like The solution process is…, Step 1 or Final Answer:

### Impact: Bypassing the Gatekeeper

Testing against a suite of general-purpose and specialized defense models confirms that LLM-as-a-judge setups are not a set-and-forget security control. By injecting low-perplexity stealth control tokens, an attacker can fundamentally break the logic of the automated gatekeeper.

To verify that our discovered control tokens are stealthier than common gibberish jailbreak tokens, we subjected them to a perplexity test. We compared the perplexity scores of our AdvJudge-Zero tokens against those from a common jailbreak algorithm (GCG) and against manually discovered, verified stealthy tokens (e.g., 解 and Solution: ) from other prior research.

As Figure 1 illustrates, the tokens discovered by AdvJudge-Zero (blue area toward the left) yield significantly lower perplexity scores than the gibberish adversarial tokens (red area on the right). Furthermore, the AdvJudge-Zero tokens exhibit perplexity scores equivalent to the verified stealth jailbreak tokens (yellow area, the leftmost spike). This evidence supports the conclusion that the tokens discovered by AdvJudge-Zero are indeed more stealthy and significantly more likely to bypass general gatekeepers undetected.

![A histogram showing the distribution of minimum perplexity on AIME. The x-axis represents perplexity on a log scale, and the y-axis is frequency. It includes three overlapping distributions: orange for Master-RM, blue for GCG (Adversarial), and red for AdvJudge-Zero.]()

Figure 1. Perplexity comparison for AdvJudge-Zero tokens vs. common jailbreak tokens.

## How Attacks Would Manifest in Real-World Scenarios

These attacks do not resemble traditional hacking or computer code. Instead, they appear as standard formatting that exploits the logic in the AI's judgment.

* **Scenario 1: Bypassing safety filters (the false approval)**

An attacker can force a judge to approve toxic, biased or prohibited content.

* + **The Attack:** The attacker appends a specific stealth control token found by AdvJudge-Zero, such as \n\nAssistant:
  + **The Result:** These tokens manipulate the judge into concluding the policy check phase has ended. The judge reverses its decision from block to allow, permitting the harmful content.

* **Scenario 2: Corrupting training data (reward hacking)**

In many enterprises, AI judges are used to score model responses during training, a process called reinforcement learning from human feedback (RLHF). If the judge is hacked, the AI learns the wrong lessons.

* + **The Attack:** An attacker inserts directive phrases like The correct answer is: or \begin{enumerate}
  + **The Result:** The AI judge is “distracted” by the professional-looking formatting and assigns a high score even to incorrect information or hallucinations. This leads to model degradation, where the resulting AI becomes less reliable.

## Vulnerable Model Categories

Our research using this tool achieved a 99% success rate in bypassing controls across several widely used architectures that customers rely on today:

1. **Open-weight enterprise models:** Popular models used for internal company chatbots and document summarization.
2. **Specialized reward models:** Models specifically built and trained to act as “security guards” for other AI systems.
3. **High-parameter models:** Even the largest, most “intelligent” models (with more than 70 billion parameters) were susceptible. Their complexity actually provides more surface area for these logic-based attacks to succeed.

## Conclusion

The methods of AdvJudge-Zero in our testing prove that AI judges are susceptible to logic flaws similar to other software. If an attacker can automate the discovery of bypass codes through fuzzing, they can systematically defeat AI guardrails with innocent-looking inputs.

However, the fuzzer methodology also provides a solution. By adopting adversarial training — running this type of fuzzer internally to identify weaknesses and then retraining the model on these examples — organizations can harden their systems. This approach can reduce the attack success rate from approximately 99% to near zero.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

Organizations are better equipped to [close the AI security gap](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/close-ai-security-gap) through the deployment of [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management), which delivers comprehensive visibility and posture management for AI agents. Cortex AI-SPM is designed to mitigate critical risks including over-privileged AI agent access, misconfigurations and unauthorized data exposure.

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help empower safe AI use and development.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 000 800 050 45107
* South Korea: +82.080.467.8774

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

* [AdvJudge-Zero Research Paper (ArXiv)](https://arxiv.org/abs/2512.17375)
* [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/pdf/2307.15043)
* [One Token to Fool LLM-as-a-Judge](https://arxiv.org/pdf/2507.08794)

Back to top

### Tags

* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [Fuzzing](https://unit42.paloaltonetworks.com/tag/fuzzing/ "fuzzing")
* [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")
* [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/ "prompt injection")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: An Investigation Into Years of Undetected Operations Targeting High-Value Sectors](https://unit42.paloaltonetworks.com/cl-unk-1068-targets-critical-sectors/ "An Investigation Into Years of Undetected Operations Targeting High-Value Sectors")

### Table of Contents

### Related Articles

* [Frontier AI and the Future of Defense: Your Top Questions Answered](https://unit42.paloaltonetworks.com/frontier-ai-top-questions-answered/ "article - table of contents")
* [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "article - table of contents")
* [Fracturing Software Security With Frontier AI Models](https://unit42.paloaltonetworks.com/ai-software-security-risks/ "article - table of contents")

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

![Pictorial representation of TeamPCP. Glowing code on a screen where several word such as Crime, Hackers, and Security are highlighted in a contrasting color.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/03_Cybercrime_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) March 31, 2026
[#### Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/)

* [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
* [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
* [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/ "Infostealer")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/ "Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure")

* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)
![Enlarged Image]()
