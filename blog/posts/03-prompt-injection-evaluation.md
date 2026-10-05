---
title: "We Evaluate Prompt-Injection Defenses Too Simply"
subtitle: "A low attack success rate can mean a model handled untrusted text correctly, or that it threw the text away, and the standard metric does not say which."
date: 2026-10-05
tags: [LLM security, prompt injection, evaluation, personal perspective]
sources:
  - https://arxiv.org/abs/2606.30783
  - https://arxiv.org/pdf/2606.30783
  - https://dream.ischool.illinois.edu/blogs/security_fidelity_tradeoff.html
---

# We Evaluate Prompt-Injection Defenses Too Simply

*A low attack success rate can mean a model handled untrusted text correctly, or that it threw the text away, and the standard metric does not say which.*

Most prompt-injection defenses are judged by one number: how often the attack succeeds. The number is easy to compute and easy to compare. I have come to think it is also easy to misread.

This post is my opinion on why that matters. The technical details are in our ICML 2026 Spotlight paper, [Security–Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense](https://arxiv.org/abs/2606.30783). Mitchell Hermon led it, with Rahul Gupta, Weitong Ruan, and Ekraam Sabir. The [DREAM Lab blog post](https://dream.ischool.illinois.edu/blogs/security_fidelity_tradeoff.html) walks through the benchmark and results. Here I want to explain why I think the field should change how it reports defenses.

## One number, two behaviors

Consider an email assistant asked to translate a message. The message contains a sentence that reads like an instruction. A good assistant should translate that sentence along with the rest, because it is part of the email. It should not obey it.

Now suppose a defended model leaves the sentence out of the translation. The attack did not succeed, so the attack success rate counts this as a win. But the user received an incomplete translation, and nothing warned them.

That is the core problem. A model can avoid executing injected text in two ways. It can treat the text as data and process it as the task requires. Or it can suppress the text. Both lower the attack success rate by the same amount. Only the first is what we want when the task depends on that text.

Instruction-like text is common in ordinary data. Emails contain requests. Documentation contains commands. Legal text quotes obligations. A defense that learns to drop such text will look secure on a benchmark that only checks execution.

## What we found when we measured both

To separate these behaviors, the paper builds a benchmark, SecFid, where executing, processing, and ignoring an injected span each produce a different output. That makes a second quantity measurable. The paper calls it fidelity: how often the model avoids suppressing content the task needs.

Across 1,168 examples and 48 configurations, no model or defense scored high on both. The highest-fidelity model, undefended Llama 3.3 70B, reached 96.5% fidelity at 47.8% security. The most secure configurations, SecAlign on Llama 3.1 8B and Llama 3.3 70B, reached 99.3% security with 73.9% and 71.0% fidelity.

The result I would point to first concerns defenses with similar security. On Llama 3.1 8B, SecAlign and DefensiveTokens both push execution close to zero. Among the cases the undefended model had executed, SecAlign turned 54% into faithful processing and suppressed 37%. DefensiveTokens did roughly the reverse, repairing 27% and suppressing 60%. An attack-success leaderboard would rank these two defenses as nearly equal. For a translation or editing product, they are very different.

## Why I think this matters beyond one benchmark

Suppression is a silent failure. A model that drops a sentence still returns output that looks complete. The paper's impact statement makes the same point: fixed defenses can corrupt data without warning. Users and developers are unlikely to notice, so the cost can accumulate without anyone measuring it.

The right behavior also depends on the deployment. The paper formalizes this with a simple cost model. A translation service loses a lot by dropping content and should process all but the riskiest spans. An agent that can move money loses a lot from a single hijack and should filter on weak evidence. The same string can deserve opposite treatment. So I do not think a defense has a single correct operating point. A defense should be described by where it sits and whether that position can be tuned.

Research incentives point the same way. If papers report only attack success, one easy way to improve the number is to suppress more. A metric that rewards suppression will tend to produce defenses that suppress. Reporting fidelity alongside security changes what counts as progress. It also opens a path to better defenses. In the paper, a fidelity-aware preference-tuning step (DPO) on top of SecAlign raised processing on an unseen editing task from 43.2% to 80.6%, with execution still below 1%.

## What I am less sure about

The benchmark uses fixed probes. An adaptive attacker may behave differently, and we have not measured how adaptive attacks affect fidelity. The cost model reduces a defense's choices to two actions, process or filter. Real systems can do more, such as keeping the text while removing its authority. Fidelity for translation and editing is scored by embedding similarity to reference outputs, which is a reasonable proxy but still a proxy.

There is also a fair counterargument. For many agentic deployments, security matters much more than fidelity, and a defense that drops suspicious text may be the right choice. I agree. My point is narrower. Even in those settings, the team deploying the defense should know what it costs. A security number alone does not tell them.

## What I would ask for

When a paper or a product reports a prompt-injection defense, I would like the security number to come with two companions. One is a measure of how much legitimate content the defense removes, on tasks where that content matters. The other is a statement of the task and deployment the numbers are meant for. Neither is hard to report. Together they would let a reader see the price of the security they are buying.

*This is a personal perspective. For the full method and results, see the [paper](https://arxiv.org/abs/2606.30783) and the [lab blog post](https://dream.ischool.illinois.edu/blogs/security_fidelity_tradeoff.html).*
