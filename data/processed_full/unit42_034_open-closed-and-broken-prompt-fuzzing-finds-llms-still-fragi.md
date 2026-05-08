---
title: "Open, Closed and Broken: Prompt Fuzzing Finds LLMs Still Fragile Across Open and Closed Models"
date: "2026-03-17"
url: https://unit42.paloaltonetworks.com/genai-llm-prompt-fuzzing/
source: unit42
---

# Open, Closed and Broken: Prompt Fuzzing Finds LLMs Still Fragile Across Open and Closed Models

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")

[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Open, Closed and Broken: Prompt Fuzzing Finds LLMs Still Fragile Across Open and Closed Models

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  12  min read

Related Products

[![Code to Cloud Platform icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Code to Cloud Platform](https://unit42.paloaltonetworks.com/product-category/code-to-cloud-platform/ "Code to Cloud Platform")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Yu Fu](https://unit42.paloaltonetworks.com/author/yu-fu/)
  + [May Wang](https://unit42.paloaltonetworks.com/author/may-wang/)
  + [Royce Lu](https://unit42.paloaltonetworks.com/author/royce-lu/)
  + [Shengming Xu](https://unit42.paloaltonetworks.com/author/shengming-xu/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 17, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Malware](https://unit42.paloaltonetworks.com/category/malware/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Evasion](https://unit42.paloaltonetworks.com/tag/evasion/)
  + [GenAI](https://unit42.paloaltonetworks.com/tag/genai/)
  + [LLM](https://unit42.paloaltonetworks.com/tag/llm/)
  + [Prompt Fuzzing](https://unit42.paloaltonetworks.com/tag/prompt-fuzzing/)
  + [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/genai-llm-prompt-fuzzing/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/genai-llm-prompt-fuzzing/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Open,%20Closed%20and%20Broken:%20Prompt%20Fuzzing%20Finds%20LLMs%20Still%20Fragile%20Across%20Open%20and%20Closed%20Models&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F&title=Open,%20Closed%20and%20Broken:%20Prompt%20Fuzzing%20Finds%20LLMs%20Still%20Fragile%20Across%20Open%20and%20Closed%20Models "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F&text=Open,%20Closed%20and%20Broken:%20Prompt%20Fuzzing%20Finds%20LLMs%20Still%20Fragile%20Across%20Open%20and%20Closed%20Models "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Open,%20Closed%20and%20Broken:%20Prompt%20Fuzzing%20Finds%20LLMs%20Still%20Fragile%20Across%20Open%20and%20Closed%20Models%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgenai-llm-prompt-fuzzing%2F "Share in Mastodon")

## Executive Summary

Unit 42 researchers have developed a genetic algorithm-inspired prompt fuzzing method to automatically generate variants of disallowed requests that preserved their original meaning. This method also measures guardrail fragility under systematic rephrasing.

Our research uncovered guardrail weaknesses, with evasion rates ranging from low single digits to high levels in specific keyword and/or model combinations. The key difference from prior single-prompt jailbreak examples is scalability. Small failure rates become reliable when attackers can automate at volume.

Prompt jailbreaking is a text-based adversarial input threat against large language model (LLM)-powered generative AI (GenAI) applications, especially chatbots and chat-shaped workflows. Attackers craft inputs that manipulate the model into bypassing guardrails, producing disallowed content or otherwise operating outside of intended scopes.

This matters to any organization embedding GenAI into customer support, employee copilots, developer tooling or knowledge assistants. Because the primary attack surface is untrusted natural language, failures can translate into safety incidents, compliance exposure and reputational damage.

We recommend the following:

* Treating LLMs as non-security boundaries
* Defining scope
* Applying layered controls
* Validating outputs
* Continuously testing GenAI with adversarial fuzzing and red-teaming

Palo Alto Networks customers are better protected against the threats discussed in this article through the following products and services:

* [Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security)
* The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | **[GenAI](https://unit42.paloaltonetworks.com/tag/genai/), [LLM](https://unit42.paloaltonetworks.com/tag/llm/), [Prompt Injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/), [Evasion](https://unit42.paloaltonetworks.com/tag/evasion/)** |

## Background

Since the first large-scale LLM deployments in 2020, GenAI has moved from experimentation to production. LLM-backed features now appear in customer support, developer tooling, enterprise knowledge search and end‑user productivity applications. [Market forecasts](https://www.qualcomm.com/news/onq/2023/11/the-generative-ai-economy-is-worth-up-to-7-trillion-dollars) vary, but they consistently point to rapid growth in both GenAI and the broader AI ecosystem.

A major reason for this adoption is that many GenAI systems implement a chatbot-style interface, even when a product is not branded as a chatbot. Users provide natural language inputs.

The end product combines input with system instructions, retrieved context and tool outputs into a prompt. The product's backend model generates a response. This interactive model is straightforward yet powerful, but it also means the primary attack surface is untrusted text.

Because LLMs can generate responses, production systems using LLMs require guardrails to reduce unsafe, non-compliant or out-of-scope behavior. In practice, guardrails are multi-layered. These layers consist of content moderation and classification, model-side alignment and refusal behavior. For example, the Azure implementation of OpenAI [content filtering](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic) includes filtering against areas such as hate and fairness-related harm, sexual content, violence and self-harm.

Cloud providers have also added safeguards aimed specifically at LLM misuse patterns. For example, [Microsoft’s Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) is one such method to prevent prompt-injection-style attacks.

Despite years of investment in these defenses, prompt jailbreaking and prompt injection remain one of the most well-known and actively discussed attack classes against LLM applications. [OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/) lists prompt injection as the top risk category for LLM applications in 2025.

[Academic work](https://arxiv.org/abs/2211.09527) has also shown that simple, crafted inputs can cause goal hijacking or prompt leaking in LLM-based systems. More recently, the [U.K. National Cyber Security Center has argued](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) that prompt injection differs materially from SQL injection and may be harder to fix in a definitive way. This is because LLMs do not enforce a clean separation between instructions and data within prompts.

This raises a practical question. After roughly five years of rapid iteration in alignment and safety engineering, how fragile are current open and closed models when an attacker systematically rewrites a disallowed request without changing its meaning?

We have approached answering this question by using a well-established security concept in software testing: fuzzing. Starting from a malicious prompt, we generate meaning-preserving variants that alter surface form, such as wording, structure and framing, while retaining the malicious intent. We then measure whether these variants can evade guardrails across both open-weight models and proprietary closed-source models.

The goal is defensive: to make robustness measurable and comparable, and to highlight where existing controls remain brittle under realistic and automated variation.

## Prerequisite Knowledge

Two types of background knowledge are necessary to understand our approach to this research: fuzzing and prompt hacking. For prompt-hacking taxonomy and [techniques](https://live.paloaltonetworks.com/t5/community-blogs/genai-security-technical-blog-series-2-6-secure-ai-by-design/ba-p/590862), refer to our previous publications, such as our [report on securing GenAI against adversarial prompt attacks](https://www.paloaltonetworks.com/resources/whitepapers/prompt-attack).

In software security and quality engineering, fuzzing is an automated testing technique used to uncover defects and security weaknesses by presenting a target with large volumes of atypical inputs. These inputs may be invalid, malformed, unexpected or randomly generated. The system is then monitored for anomalous behavior and failure modes such as:

* Crashes
* Information disclosure
* Memory corruption
* Memory leaks
* Service disruption
* Unexpected state transitions

A challenge in fuzzing is effective test case generation. Purely random input generation is simple but often inefficient, especially for targets that require structured inputs or have complex parsing and control-flow logic.

As a result, modern fuzzers increasingly rely on feedback-driven input generation, where mutations are guided by signals from prior executions. This includes feedback on code coverage, error conditions or other behavioral indicators. The goal is to adaptively explore execution paths that are more likely to surface vulnerabilities.

One widely used strategy for such adaptive generation is a [genetic algorithm [PDF]](https://www.geos.ed.ac.uk/~mscgis/12-13/s1100074/Holland.pdf), a class of evolutionary optimization methods inspired by natural selection. In genetic algorithm terminology, each candidate input is represented as a chromosome composed of genes, which refer to features or components of the input.

A fitness function scores candidates based on how well they achieve a target objective. Examples of targeted objectives include reaching new execution paths or triggering abnormal behavior. Over successive generations, higher-fitness candidates are preferentially retained and transformed through operators such as mutation and crossover, producing progressively more effective test inputs.

Here are the four steps of a genetic algorithm:

* **Initialization**: A population of randomly generated chromosomes (sequences of genes) is created. This population evolves over multiple iterations, known as generations.
* **Selection**: In each generation, the fitness of each individual is evaluated. In the context of fuzzing, fitness is an objective function of the optimization problem. A more fit individual will have a higher chance of being selected. In the context of LLM fuzzing, a more effective word or sequence of words will have a higher probability of the LLM accepting it as a prompt.
* **Mutation and crossover**: The next step is to create a second generation of population based on the selected samples through a combination of genetic operations of mutation and crossover.
* **Termination**: Repeat the process until an optimal solution is found or the limit is reached.

For this research, we applied the concept of a genetic algorithm to design an algorithm for generating evasive prompts to fuzz LLMs.

## Fuzzing Algorithms

Figure 1 shows the workflow comparison of a standard genetic algorithm and an LLM-based genetic algorithm. This diagram labels the individual steps for a better understanding, and it illustrates how we can adapt the standard genetic algorithm for LLMs.

![Two flowcharts compare the sequential steps of a standard genetic algorithm with an LLM-based genetic algorithm. The LLM-based version illustrates how a keyword undergoes iterative operations like adding phrases or words to generate evasive prompts, culminating in a termination and evasion check.]()

Figure 1. Workflow comparison of standard genetic algorithm design versus an LLM-based genetic algorithm design.

Using the LLM-based workflow genetic algorithm in Figure 1, we can better understand how to use a genetic algorithm technique for prompt evasion. For example, let's say we want to generate an evasive prompt based on a harmful question like “how to build a bomb.” If we directly input the original question to an LLM, the LLM will likely refuse to answer for security reasons.

Instead, we can leverage the following steps to generate evasive prompts that contain the same questions, but which can evade the LLMs successfully.

* Initialization: Based on the sensitive questions, we will prepare three lists of words.
  + Keyword: This represents the keyword in the question, which is a noun in most cases. In this example, the keyword will be “bomb.”
  + Relative word: This represents the action in the question, which is a verb in most cases. Examples include “build,” “list the ingredients of” and “components of.”
  + Phrases: This is a list of commonly used phrases in English that do not have specific meanings or relations to the particular questions. The purpose is to use the phrase list to disrupt the LLMs' ability to accurately interpret the question. Example phrases include “Has anyone,” “Is it” and “Do you think.”
* Selection and mutation: We combine the steps of selection with mutation and crossover in this one step for easy explanation. For every iteration, we choose one operation out of the six options on the output of the previous iterations. We can define the probability of each operation being chosen. We repeat the process for *N* iterations. The options of operations are listed below.
  + Prepend a phrase: Randomly choose and prepend a phrase to the output of the last iteration
  + Append a phrase: Randomly choose and append a phrase to the output of the last iteration
  + Add a linefeed: Add a line feed at the end of the output of the last iteration
  + Repeat the keyword: Randomly choose and repeat the keyword, placing it at the end of the output of the last iteration
  + Add a relative word: Randomly choose and put a relative word at the end of the output of the last iteration
  + Remove a word: Remove a random word from the output of the last iteration
* Termination: After *N* iterations are reached, we submit the generated prompts to LLMs and test whether they can successfully evade them. We take the LLM output and calculate its “fitness” the same way as the standard genetic algorithm. We can use the number of negative tones in the fitness function as an example. If needed, we can repeat the mutation process multiple times until a successful evasion is achieved. In our experiments, we found that 100 iterations are enough to find some successful evasions.

## Experiment Results

We tested different models with harmful questions of how to build four types of explosives: bomb, napalm, ordnance and torpedo. We applied the fuzzing algorithm to generate 100 fuzzed versions of each question.

For every iteration, we limited the maximum number of mutation operations to 50 times. With the 100 generated prompts per question, we tested each of them against three types of models.

All the tested models were released in 2024 and 2025, and they were the most popular and advanced models when building GenAI applications. We conducted all tests through API calls. The four tested models were:

* One closed-source pretrained model that provides answers to the prompts
* Two open-source pretrained models that provide answers to the prompts
* One open-source content-filter model that provides binary classification to the prompts

We tested the fuzzed prompts against the four models with the prompts using different keywords, including bomb, napalm, ordnance and torpedo. Table 1 shows the success rate of these evasive prompts. The value means the percentage of successful evasion. For example, 10/100 means 10 out of 100 generated prompts could evade the model content filter.

| Models | Successful Evasion | | | |
| --- | --- | --- | --- | --- |
| Bomb | Napalm | Ordnance | Torpedo |
| Closed-source pretrained Model 1 | 5/100 | 16/100 | 8/100 | 90/100 |
| Open-source pretrained Model 1 | 1/100 | 2/100 | 4/100 | 2/100 |
| Open-source pretrained Model 2 | 20/100 | 63/100 | 24/100 | 75/100 |
| Open-source content filter Model | 98/100 | 99/100 | 97/100 | 98/100 |

Table 1. Experiment results on different keywords and LLM models.

In terms of the definition of successful evasion, we look at the LLM responses to see if it contains information about the ingredients of the explosive. If yes, we consider it as a successful evasion. Particularly for the content filter model, which provided binary classification, 11/100 means that 11 out of 100 fuzzed malicious prompts are classified as benign, representing false negative cases.

Figures 2 and 3 show an example of prompt input and the associated output of successful evasion.

![A screenshot displays a text-based prompt input, partially redacted with black boxes, where the word "ordnance" is visible. This prompt successfully bypassed an LLM's guardrails, demonstrating an evasion technique.]()

Figure 2. An example prompt input resulting in a successful evasion.

![A screenshot of an LLM's output details "Main Components of Ordnance," including explosive fills and propellants. This content was generated in response to an evasive prompt, indicating a guardrail failure.]()

Figure 3. An example prompt output from the successful evasion prompt in Figure 2 (truncated).

Across both proprietary and open-weight targets, we observed non-uniform robustness across both categories, rather than a clear “closed is safer than open” split.

* The closed-source pretrained model showed moderate evasion for several keywords (e.g., 5/100 for bomb, 16/100 for napalm, 8/100 for ordnance), and a sharp failure mode on torpedo (90/100). This indicates that even mature proprietary systems can exhibit keyword-specific weak spots under fuzzing.
* On the open-weight side, the results were bimodal: One pretrained model remained relatively resistant across all keywords (1–4/100), while another was substantially more fragile (20/100–75/100 depending on keyword).
* The open-source content filter target was the weakest overall, classifying 97–99% of fuzzed prompts as benign across all keywords, suggesting that this style of filtering is particularly brittle under meaning-preserving surface variations.

Taken together, the results suggest that the model licensing (closed source vs. open source) is not a reliable indicator for guardrail strength. Robustness depends more on the specific model tuning and safety stack, and it must be validated empirically across diverse prompts and keywords.

Across the four weapon-related seed keywords, evasion rates were strongly keyword-dependent, with a large variance even among semantically similar terms.

* For the closed-source pretrained model, “torpedo” produced an outlier 90/100 successful evasion rate, compared to 5/100 for bomb, 16/100 for napalm, and 8/100 for ordnance, indicating uneven guardrail sensitivity across adjacent keywords.
* Open-source pretrained model 1 was comparatively more consistent and lower-risk across all keywords (1–4/100).
* In contrast, open-source pretrained model 2 showed substantially higher fragility overall, particularly for napalm (63/100) and torpedo (75/100), with non-trivial rates for bomb (20/100) and ordnance (24/100).
* Most notably, the content filter model labeled the vast majority of fuzzed variants as benign across all keywords (97–99/100), suggesting the filter’s decision boundary is highly susceptible to surface-form variation.

Overall, these results reinforce that robustness cannot be inferred from testing only a single canonical keyword. Coverage across related terms materially changes the measured risk.

When we began this work in 2024, we evaluated the same model family on an earlier release — approximately four versions before the current one — and we observed comparable evasion rates. This is not a controlled longitudinal study, but it suggests that over the past two years, model capability has improved substantially. Robustness to prompt-based evasion may not have improved at the same pace, at least for the type of attacks evaluated in this research.

## Realism of This Evasion Method

We now discuss why this evasion method remains realistic, even without testing an end-to-end production system.

Our experiments focused primarily on pretrained models and a separate content-filtered variant, rather than complete end-to-end applications with retrieval, tool constraints, rate limits and layered safety middleware. That limitation is important, but it does not make the results unrealistic.

In practice, many real deployments still expose scenarios where the base model’s behavior dominates, for example:

* Self-hosted open-weight deployments with minimal safety wrapping
* Internal tools where policy enforcement is assumed rather than verified
* Misconfigurations where safety middleware is bypassed or inconsistently applied
* Situations where the content filter is treated as the primary control and the rest of the stack is permissive

The content-filtered model showing higher successful evasion raises a critical design question. Why does an additional safety layer appear less robust under systematic input variation?

One plausible explanation is that filters tuned to catch common language patterns can be brittle under natural-language rephrasing. Regardless of root cause, the result reinforces a core principle, which is that guardrails must be evaluated as a system under adversarial variation, not assumed to be effective because they work on canonical examples.

### Harmful vs. Out-of-Scope Requests: The Harder Problem

Blocking clearly harmful categories (e.g., weapon construction) is difficult, but often more tractable than enforcing a product’s business scope. This is partly because the presence of harmful words, such as the term “ordnance” in our testing, aids detection.

Many production GenAI applications are not general assistants. They are chatbot-like frontends for a narrow capability, like translating text, summarizing documents, querying internal knowledge or drafting code. In those systems, attackers do not need to elicit obviously harmful content to cause damage. Instead, they can push the model out of scope, such as coercing a translation tool into generating unrelated guidance.

Because out-of-scope prompts may be benign in isolation, category moderation against pure harm is not enough. This gap can become a larger real-world risk than the obvious harmful prompt case, especially when models are connected to data sources or tools.

### Implications for Security-by-Design

The broader takeaway is that security for LLM applications cannot rely on a single layer, including prompt instructions, a classifier or model refusals. If a small budget fuzzer can find bypasses, then production systems should assume that motivated attackers will also find them.

To build a question-answering LLM application that is more resilient to prompt hacking attacks, the following design practices are worth treating as baseline:

* **Define and enforce application scope**. Specify what the system is allowed to do and not do in terms of domains, tasks and tool access. Narrow-scope assistants are typically easier to defend than general-purpose assistants because policy enforcement can be explicit and testable.
* **Use robust, multi-signal content controls**. Keyword-only filtering is insufficient given the flexibility of natural language. Choose layered controls that combine semantic classification, policy rules and context-aware checks. Evaluate them under paraphrase and adversarial variation, not just fixed test prompts.
* **Treat user input as untrusted and isolate it from privileged instructions.** Avoid directly concatenating raw user text into high-privilege instruction channels. Use structured prompting patterns that clearly separate data from instructions, and design prompts so that untrusted content cannot easily override system intent.
* **Validate outputs against scope and policy.** Apply post generation validation to ensure the response stays within the allowed task boundary. If the output violates scope or policy, block or regenerate with stricter constraints.
* **Monitor and log for misuse signals.** Track anomalous patterns such as repeated probing, high variance prompt attempts and repeated near boundary failures. Instrumentation is essential both for detection and for improving defenses over time.
* **Apply standard security controls around the system.** Strong authentication and authorization, rate limiting, least privilege tool permissions and secure backend isolation remain critical, especially when the model can access internal data or perform actions.

From a practitioner perspective, the most actionable next step is to operationalize this kind of testing as continuous regression. This involves running fuzzing-based adversarial evaluations when models, prompts or filters change. From a research perspective, results like these suggest the need for guardrails that are more robust to meaning-preserving variation. They also underscore the need for clearer evaluation standards that measure not just refusal rate, but boundary fragility and failure modes under automation.

## Conclusion

This work shows that prompt jailbreaking remains a practical risk even after several years of safety engineering progress. By adapting a genetic algorithm-based fuzzing approach to generate meaning-preserving prompt variants, we were able to trigger policy-violating outcomes against both closed-source and open-weight pretrained models. We did so using only a single disallowed seed request and a small number of runs.

Importantly, the observed success rates are operationally meaningful. Once attackers can automate probing, even low-probability failures can be found reliably at scale.

The results also highlight an additional concern. A standalone content filter model showed a higher evasion success rate in our testing, raising questions about how filters are trained, what patterns they generalize to and how they behave under systematic paraphrasing.

The broader implication is that guardrails should be treated as probabilistic controls that require continuous adversarial evaluation, not as definitive security boundaries. For production GenAI systems, resilience depends on security-by-design. This includes:

* Clearly defining application scope
* Enforcing that scope through layered controls
* Isolating untrusted input from privileged instructions
* Validating model outputs
* Monitoring for probing behavior

These findings reinforce the idea that the harder long-term challenge might not be only harmful content detection, but robust scope enforcement for domain-specific applications. This is especially fraught when models are connected to tools, data and real workflows.

### Palo Alto Networks Protection and Mitigation

[Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security) provides inline inspection and enforcement for prompts and responses to help block prompt injection, data leakage and unsafe outputs.

The [Unit 42 AI Security Assessment](https://docs.paloaltonetworks.com/ai-runtime-security) can help empower safe AI use and development.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://docs.paloaltonetworks.com/ai-runtime-security) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 000 800 050 45107
* South Korea: +82.080.467.8774

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

Back to top

### Tags

* [Evasion](https://unit42.paloaltonetworks.com/tag/evasion/ "Evasion")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
* [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")
* [Prompt Fuzzing](https://unit42.paloaltonetworks.com/tag/prompt-fuzzing/ "Prompt Fuzzing")
* [Prompt injection](https://unit42.paloaltonetworks.com/tag/prompt-injection/ "prompt injection")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Boggy Serpens Threat Assessment](https://unit42.paloaltonetworks.com/boggy-serpens-threat-assessment/ "Boggy Serpens Threat Assessment")

### Table of Contents

### Related Articles

* [That AI Extension Helping You Write Emails? It’s Reading Them First](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "article - table of contents")
* [Frontier AI and the Future of Defense: Your Top Questions Answered](https://unit42.paloaltonetworks.com/frontier-ai-top-questions-answered/ "article - table of contents")
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
