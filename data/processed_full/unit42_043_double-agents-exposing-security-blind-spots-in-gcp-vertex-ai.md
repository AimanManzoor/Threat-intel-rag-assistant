---
title: "Double Agents: Exposing Security Blind Spots in GCP Vertex AI"
date: "2026-03-31"
url: https://unit42.paloaltonetworks.com/double-agents-vertex-ai/
source: unit42
---

# Double Agents: Exposing Security Blind Spots in GCP Vertex AI

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")

[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Double Agents: Exposing Security Blind Spots in GCP Vertex AI

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  11  min read

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Ofir Shaty](https://unit42.paloaltonetworks.com/author/ofir-shaty/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 31, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Malware](https://unit42.paloaltonetworks.com/category/malware/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/)
  + [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/)
  + [GCP](https://unit42.paloaltonetworks.com/tag/gcp/)
  + [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/)
  + [Google cloud storage](https://unit42.paloaltonetworks.com/tag/google-cloud-storage/)
  + [JSON](https://unit42.paloaltonetworks.com/tag/json/)
  + [LLM](https://unit42.paloaltonetworks.com/tag/llm/)
  + [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)
  + [Vertex AI](https://unit42.paloaltonetworks.com/tag/vertex-ai/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/double-agents-vertex-ai/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Double%20Agents:%20Exposing%20Security%20Blind%20Spots%20in%20GCP%20Vertex%20AI&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F&title=Double%20Agents:%20Exposing%20Security%20Blind%20Spots%20in%20GCP%20Vertex%20AI "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F&text=Double%20Agents:%20Exposing%20Security%20Blind%20Spots%20in%20GCP%20Vertex%20AI "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Double%20Agents:%20Exposing%20Security%20Blind%20Spots%20in%20GCP%20Vertex%20AI%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fdouble-agents-vertex-ai%2F "Share in Mastodon")

## Executive Summary

Artificial intelligence (AI) agents are quickly advancing into powerful autonomous systems that can perform complex tasks. These agents can be integrated into enterprise workflows, interact with various services and make decisions with a degree of independence. Google Cloud Platform’s Vertex AI, with its Agent Engine and Application Development Kit (ADK), provides a comprehensive platform for developers to build and deploy these sophisticated agents.

But what if the AI agent you just deployed was secretly working against you? As we delegate more tasks and grant more permissions to AI agents, they become a prime target for attackers. A misconfigured or compromised agent can become a “[double agent](https://unit42.paloaltonetworks.com/agentic-ai-threats/)” that appears to serve its intended purpose, while secretly exfiltrating sensitive data, compromising infrastructure, and creating backdoors into an organization's most critical systems.

Our research examines how a deployed AI agent in the Google Cloud Platform (GCP) Vertex AI Agent Engine could potentially be weaponized by an attacker. By exploiting a significant risk in default permission scoping and compromising a single service agent, we reveal how the Vertex AI permission model can be misused, leading to unintended consequences.

We were able to achieve privileged access to data in a consumer project, and to restricted images and source code within a producer project that is part of Google’s [infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview). Following this discovery, we shared details of our research with Google and [collaborated](#post-176231-_p0bxcw2nztpq) with their security team. Google revised their official documentation to explicitly document how Vertex AI uses resources, accounts and agents.

Our findings provide valuable insights into the inner workings of the Vertex AI platform and demonstrate how an AI agent could be weaponized to compromise an entire GCP environment.

Palo Alto Networks customers are better protected from the threats described in this article through the following products and services:

* [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)
* Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)
* [Cortex AI-SPM](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)

The [Unit 42 AI Security Assessment](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) can help empower safe AI use and development.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | **[Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/), [Vertex AI](https://unit42.paloaltonetworks.com/tag/vertex-ai/), [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/), [Data Exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/), [Privilege Escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)** |

## From Agent to Storage Admin: Taking Over Consumer Resources

We started our investigation by deploying an AI agent that we built using [Google Cloud ADK](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview). We discovered that the Per-Project, Per-Product Service Agent ([P4SA](https://docs.cloud.google.com/integration-connectors/docs/service-account)) associated with the deployed AI agent had excessive permissions that were granted by default. A [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) is a Google-managed service account that allows a GCP service to access resources. Using the P4SA’s default permissions, we were able to extract the credentials of the following service agent and act on behalf of its identity:

service-<PROJECT-ID>@gcp-sa-aiplatform-re.iam.gserviceaccount[.]com

The following code shows how we prepared a Vertex AI agent in a controlled environment, using a tool that is configured to expose service‑agent credentials.

### Init ###
vertexai.init(
project=PROJECT\_ID,
location=LOCATION,
staging\_bucket=STAGING\_BUCKET,
)
### Functions and Tools definition ###
def get\_service\_agent\_credentials(test: str) -> dict:
<\*\*\* my malicious agent code \*\*\*>
### Agent definition ###
from google.adk.tools import google\_search
from google.adk.agents import Agent
root\_agent = Agent(
name="my\_double\_agent",
model="gemini-2.0-flash",
description=("Agent to takeover the account."),
instruction=("You are a helpful agent who can help the user exfiltrate data from storage buckets."),
tools=[get\_service\_agent\_credentials],
)
### Prepare your agent for Agent Engine ###
from vertexai.preview import reasoning\_engines
app = reasoning\_engines.AdkApp(
agent=root\_agent,
enable\_tracing=True,
)
### Deploy Agent ###
from vertexai import agent\_engines
remote\_app = agent\_engines.create(
agent\_engine=root\_agent,
requirements=[
"google-cloud-aiplatform[adk,agent\_engines,requests,socket,subprocess,os]"
],
display\_name="testing-with-reverese"
)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37 | ### Init ###  vertexai.init(  project=PROJECT\_ID,  location=LOCATION,  staging\_bucket=STAGING\_BUCKET,  )  ### Functions and Tools definition ###  def get\_service\_agent\_credentials(test: str) -> dict:  <\*\*\* my malicious agent code \*\*\*>    ### Agent definition ###  from google.adk.tools import google\_search  from google.adk.agents import Agent  root\_agent = Agent(  name="my\_double\_agent",  model="gemini-2.0-flash",  description=("Agent to takeover the account."),  instruction=("You are a helpful agent who can help the user exfiltrate data from storage buckets."),  tools=[get\_service\_agent\_credentials],  )    ### Prepare your agent for Agent Engine ###  from vertexai.preview import reasoning\_engines  app = reasoning\_engines.AdkApp(  agent=root\_agent,  enable\_tracing=True,  )    ### Deploy Agent ###  from vertexai import agent\_engines  remote\_app = agent\_engines.create(  agent\_engine=root\_agent,  requirements=[  "google-cloud-aiplatform[adk,agent\_engines,requests,socket,subprocess,os]"  ],  display\_name="testing-with-reverese"  ) |

Since this discovery, Google has modified the ADK deployment workflow. As a result, the code snippet above reflects the previous process and may not function correctly in the current version.

Running the preparation and deployment code generated a malicious AI agent packaged as a [pickle](https://docs.python.org/3/library/pickle.html) file, which was then deployed as an Agent Engine. The resulting deployment output is illustrated in Figure 1.

![A screenshot of output from the deployment of a malicious AI agent in Vertex AI Agent Engine. A black background with a block of white text. The text includes URLs and error messages.]()

Figure 1. Agent deployment output.

After deploying the malicious AI agent, any call to the agent results in our tool sending a request to Google’s metadata service:

* hxxp[:]//metadata.google[.]internal/computeMetadata/v1/instance/?recursive=true

This call prompts the double agent to extract the credentials of the GCP Service Agent. Figure 2 highlights the extracted credentials and service agent details, presented in JSON format.

![A screenshot of malicious AI agent response displaying extracted GCP Service Agent credentials, including an email-like identity and a long access token.]()

Figure 2. Malicious agent response, containing service agent credentials.

The extracted information includes:

* The GCP project that hosts the AI agent
* The identity of the AI agent
* The [scopes](https://docs.cloud.google.com/docs/authentication#authorization-gcp) of the machine that hosts the AI agent

Reformatting the JSON output provides an easy to read version of the information, shown in Figure 3.

![A screenshot of a snippet of JSON code related to Google Cloud Platform configuration, detailing the GCP project ID, AI agent identity, and associated OAuth scopes.]()

Figure 3. Reformatted output showing extracted information.

Using the stolen credentials, we were able to pivot from the AI agent’s execution context into the consumer project. This effectively broke isolation and granted unrestricted read access to all Google Cloud Storage Buckets data within the consumer project. (For organizations that use GCP managed services, the consumer project is their own Google Cloud project.)

This level of access constitutes a significant security risk, transforming the AI agent from a helpful tool into an insider threat. The excessive permissions include:

* storage.buckets.get
* storage.buckets.list
* storage.objects.get
* storage.objects.list

Figure 4 shows the full permissions from Google’s documentation, with the Google Cloud Storage Bucket and AI Platform Endpoint permissions highlighted.

![A screenshot of a permissions settings page for Vertex AI Reasoning Engine Service Agent, highlighting excessive default access to a key vulnerability.]()

Figure 4. Vertex AI Reasoning Engine Service Agent permissions.

## Unauthorized Access to Google's Internals: Downloading Restricted Producer Images

Having compromised the consumer environment, we turned our attention to the producer environment. The producer project is the Google‑managed project that hosts the underlying service – in this case, Vertex AI. We discovered that the stolen P4SA credentials also granted access to restricted, Google-owned Artifact Registry repositories that were found in the logs during the Agent Engine deployment. Figure 5 shows one such repository in the GCP Logs Explorer interface.

![A screenshot of GCP logs showing showing an internal Google Artifact Registry repository (cloud-aiplatform-private) being accessed during Agent Engine deployment, revealing restricted resources.]()

Figure 5. A GCP internal Artifact Registry repository, revealed while deploying the Agent Engine.

Using this access, we also accessed and downloaded container images from private repositories, including:

* us-docker.pkg[.]dev/**cloud-aiplatform-private**/reasoning-engine
* **cloud-aiplatform-private**/llm-extension/reasoning-engine-py310
* us-docker.pkg[.]dev/**cloud-aiplatform-private**/llm-extension/reasoning-engine-py310:prod

These images form the core of the Vertex AI Reasoning Engine. Gaining access to this proprietary code not only exposes Google's intellectual property, but also provides an attacker with a blueprint to find further vulnerabilities.

While attempts to access the repositories via the consumer service account confirm they are not publicly accessible, the use of the service agent credentials successfully grants access. This proves that the repository is restricted to that specific identity rather than being open to the public.

Figures 6 and 7 show that regular, customer-managed user identities cannot access the restricted reasoning-engine and llm-extension repositories.

![A screenshot of Google Cloud Artifact Registry interface. A warning message states "Failed to load" with further text explaining there was an error while loading a specific URL, suggesting a network issue. There's a tracking number provided and a link to troubleshoot the issue.]()

Figure 6. Restricted reasoning-engine repository is inaccessible to a regular user.

![A screenshot of Google Cloud interface showing a notification that says, "You need additional access." There are links for contacting support and menu options for "Repositories" and "Settings" on the left.]()

Figure 7. Restricted llm-extension repository is inaccessible to a regular user.

## Misconfigured Artifact Registry Exposes Restricted Images

The principle of least privilege dictates that a user or service should only have access to the specific resources they require. However, our compromised P4SA credentials not only allowed us to download images we knew about, but also exposed contents of restricted Artifact Registry repositories. This misconfiguration revealed the existence of numerous other restricted images we were not previously aware of.

The misconfigured Artifact Registry highlights a further flaw in access control management for critical infrastructure. An attacker could potentially leverage this unintended visibility to map Google's internal software supply chain, identify deprecated or vulnerable images, and plan further attacks.

Using the following code, we enumerated Google’s Artifact Registry:

packages\_request = artifactregistry\_service.projects().locations().repositories().packages().list(parent=f'projects/{project\_id}/locations/{location\_id}/repositories/llm-extension')
packages\_response = packages\_request.execute()
packages = packages\_response.get('packages', [])

|  |  |
| --- | --- |
| 1  2  3 | packages\_request = artifactregistry\_service.projects().locations().repositories().packages().list(parent=f'projects/{project\_id}/locations/{location\_id}/repositories/llm-extension')  packages\_response = packages\_request.execute()  packages = packages\_response.get('packages', []) |

Figure 8 displays the results of the Artifact enumeration, revealing that we gained access to the targeted container images within the repository.

![A screenshot of a terminal window displaying a JSON output. The text consists of various entries, each providing details about projects hosted on "cloud-platform-private." Information includes the project's name, creation time, and update time. Each entry follows a similar structure, specifying attributes. The timestamps are formatted with date and time details.]()

Figure 8. Enumerating Google Artifact Registry.

## Tenant Project Access Reveals Google's Internal Resources

When a Vertex Agent Engine is deployed, it runs in a tenant project – a Google-managed project dedicated to that specific instance. The credentials we extracted also granted us access to the Google Cloud Storage buckets within this tenant project. There, we discovered sensitive information about the agent's deployment, including:

* Dockerfile.zip
* code.pkl
* requirements.txt

The Dockerfile.zip was particularly revealing. It contained hardcoded information about internal Google Cloud projects and storage buckets, including a restricted bucket: gs[:]//reasoning-engine-restricted/versioned\_py/Dockerfile.zip. This provided more insights into Google's internal infrastructure and security posture.

Figure 9 shows a partial list of buckets from the tenant project.

![A screenshot of a terminal output listing Google Cloud Storage buckets within the tenant project, where sensitive deployment files were discovered.]()

Figure 9. Listing tenant project storage buckets.

Figure 10 shows that Google’s internal Dockerfile reveals restricted GCP internal buckets.

![A screenshot of a terminal window displays a script with instructions and code. The focus is on Google Cloud Storage (GCS) and Docker commands related to the Vertex AI platform. The code includes version numbers, environmental variables, and commands to update the GCS file in a specified directory. Error messages indicate missing files. Red boxes highlight key commands and sections of the script.]()

Figure 10. Agent Engine Dockerfile.

Although we attempted to access the exposed bucket, we lacked the necessary permissions. As a result, no direct data access was obtained. However, the disclosure of internal Google Cloud Storage references still represents sensitive infrastructure exposure and could serve as a pivot point for further attacks.

## A Recipe for Remote Code Execution

Among the discovered files, the presence of code.pkl immediately raised a red flag. The Python [pickle module is notoriously](https://docs.python.org/3/library/pickle.html) insecure for deserializing data from untrusted sources, as it can lead to arbitrary code execution.

Python’s pickle objects documentation provides a warning that this file type is inherently not secure, as reflected in the documentation shown in Figure 11.

![A screenshot of Python documentation warning against the security risks of deserializing untrusted data with the pickle module, due to potential arbitrary code execution.]()

Figure 11. Warning from Python documentation.

While testing this vulnerability was not in the scope of our investigation, the use of pickle for serializing agent code is a significant concern. An attacker who successfully manipulates this file could potentially achieve remote code execution within the agent's execution environment, creating a persistent and powerful backdoor. This highlights the risk of using insecure serialization formats in modern AI systems.

Upon deserializing the pickle object in a contained environment, we were able to inspect its structure to reveal more of Google's internal and proprietary source code.

## Beyond the Project: Overly Permissive Scopes and the Threat to Workspace Data

Our initial analysis of the AI agent's deployment environment revealed that the [OAuth 2.0 scopes](https://docs.cloud.google.com/docs/authentication#authorization-gcp) were far too permissive. OAuth scopes define the level of access that a token grants to specific Google APIs. Overly broad scopes can significantly expand the impact radius if those tokens are compromised. The scopes set by default on the Agent Engine could potentially extend access beyond the GCP environment and into an organization's Google Workspace, including services such as Gmail, Google Calendar and Google Drive.

Limiting OAuth scopes is a critical security control, particularly in environments where tokens may be exposed or abused. While identity and access management (IAM) provides granular authorization by principal and resource, OAuth scopes introduce an additional layer of access control at the API level. When configured too broadly, they can effectively bypass the principle of least privilege and increase the risk of cross-service access.

Figure 12 shows the OAuth scopes assigned to the Agent Engine deployment.

![A screenshot of code snippet displaying a list of URLs related to various Google APIs, including Gmail, Analytics, Calendar, Drive, and YouTube.]()

Figure 12. OAuth 2.0 assignment.

For an AI agent to access these services, it would need both the permissive scope and a corresponding IAM permission. By default, the necessary IAM permissions for Workspace are not granted, which acts as an effective security boundary.

However, the presence of these wide, non-editable scopes by default is a security concern in itself. This design represents a deviation from the principle of least privilege at the scope level and creates a latent risk. The fact that these broad scopes are present by default and cannot be edited represents a structural security weakness.

## Mitigation and Collaboration With Google

As part of our responsible disclosure process and in the spirit of collaboration and proactive threat mitigation, we shared our findings with Google. Prompted by our insights regarding privilege escalation via service agents, Google revised their [official documentation](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#resources) to explicitly document how Vertex AI uses resources, accounts and agents. This increased transparency raises awareness and underscores why proactive mitigation is so important. It is also a reminder that even when a behavior is documented, its security implications may not be immediately obvious.

Google also suggested a key best practice for securing Vertex Agent Engine and ensuring least-privilege execution: Bring Your Own Service Account (BYOSA). This empowers organizations to replace the default service agent with a custom, dedicated service account. Using BYOSA, Agent Engine users can enforce the principle of least privilege, granting the agent only the specific permissions it requires to function and effectively mitigating the risk of excessive privileges.

We also reviewed potential cross-tenant and supply-chain risks with Google’s security team, including whether production Artifact Registry base images could be modified or overridden. Google confirmed that strong, non-overridable controls are in place that prevent the service agent from altering production images. This validation was an important outcome of the collaboration, providing additional assurance that cross-tenant image poisoning scenarios are effectively blocked by design.

## Conclusion

AI agents are undeniably powerful tools that are reshaping the technological landscape. However, our findings demonstrate that when these agents are misconfigured or deployed in a vulnerable environment, they can pose a serious risk to an organization.

The “double agent” blind spot in Vertex AI highlights several critical security lessons:

* **The danger of overprivileged agents:** Granting agents broad permissions by default violates the principle of least privilege and is a dangerous security flaw by design.
* **Supply-chain attacks in the age of AI:** We are witnessing the weaponization of the open-source AI ecosystem. The ease with which developers can share and deploy pre-built agents is now a double-edged sword, leveraged by malicious actors to disguise their malware as a helpful productivity agent. Once deployed, this double agent payload activates, turning a trusted tool into an insider threat capable of compromising an organization's security.
* **Emergent risks in AI system interactions:** Our investigation highlights a core challenge of the AI era. Even when individual components function as designed, the way those components interact can create security risks. As AI technology accelerates, security paradigms must evolve beyond traditional vulnerability management to address the complex and often subtle ways these new systems can be misused.
* **Institutionalizing AI security reviews:** Organizations should treat AI agent deployment with the same rigor as new production code. Validate permission boundaries, restrict OAuth scopes to least privilege, review source integrity and conduct controlled security testing before production rollout. Making these steps part of the deployment lifecycle significantly reduces the impact radius of compromised or malicious agents.

As we adopt and integrate AI, we must not forget the fundamental principles of security. Otherwise, we run the risk of inviting a new generation of double agents into the very heart of our digital lives.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

Palo Alto Networks provides [AI Runtime Security (Prisma AIRS)](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) for real-time protection of AI applications, models, data and agents. It analyzes network traffic and application behavior to detect threats such as prompt injection, denial-of-service attacks and data exfiltration, with inline enforcement at the network and API levels.

Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) and Identity Threat Detection and Response (ITDR), and provides clients with the necessary capabilities to improve their identity-related security requirements. These features provide visibility into identities and their permissions, within cloud environments to accurately detect misconfigurations and unwanted access to sensitive data. The product also offers real-time analysis surrounding usage and access patterns.

Organizations are better equipped to [close the AI security gap](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/close-ai-security-gap) through the deployment of [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management), which delivers comprehensive visibility and posture management for AI agents. This posture management tool is designed to mitigate critical risks, including overprivileged AI agent access, misconfigurations and unauthorized data exposure. Cortex AI-SPM enables security teams to enforce compliance with NIST and OWASP standards, monitor for real-time behavioral anomalies, and secure the entire AI lifecycle within a unified cloud security context.

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

* [Glossary](https://docs.cloud.google.com/service-infrastructure/docs/glossary) – Google Cloud documentation
* [Overview of Agent Development Kit](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview) – Google Cloud documentation
* [Service Agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) – Google Cloud documentation
* [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview) – Google Cloud documentation
* [Vertex AI Access Control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#resources) – Google Cloud documentation
* [pickle — Python object serialization](https://docs.python.org/3/library/pickle.html) – Python

Back to top

### Tags

* [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
* [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")
* [GCP](https://unit42.paloaltonetworks.com/tag/gcp/ "GCP")
* [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
* [Google cloud storage](https://unit42.paloaltonetworks.com/tag/google-cloud-storage/ "google cloud storage")
* [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")
* [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")
* [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
* [Vertex AI](https://unit42.paloaltonetworks.com/tag/vertex-ai/ "Vertex AI")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Converging Interests: Analysis of Threat Clusters Targeting a Southeast Asian Government](https://unit42.paloaltonetworks.com/espionage-campaigns-target-se-asian-government-org/ "Converging Interests: Analysis of Threat Clusters Targeting a Southeast Asian Government")

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
