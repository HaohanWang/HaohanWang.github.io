---
title: "Sounding Like You Know"
subtitle: "Frontier models are getting better at sounding right. In biology, where answers are slow to check, that fluency is harder to catch than a plain error."
date: 2026-10-09
tags: [AI for science, trustworthy AI, biology, evaluation, LLM reasoning, personal perspective]
slug: sounding-like-they-know
sources:
  - https://arxiv.org/abs/2610.03551
  - https://haohanwang.ischool.illinois.edu/blog/math-is-not-just-problem-solving.html
---

# Sounding Like You Know

*Frontier models are getting better at sounding right. In biology, where answers are slow to check, that fluency is harder to catch than a plain error.*

Language models are improving fast. One thing they are improving at is sounding like they understand. In some fields that is fine, because a wrong answer gets caught quickly. In biology, it often does not.

**In short:**

- A fluent answer and a correct answer are different things. Models are getting better at the first faster than we can check the second.
- In math and code, a checker catches many errors. In open-ended biology, the check is often an experiment that takes months.
- Scientists should treat model output as a hypothesis to test. We also need evaluations that reward a model for saying what it does not know.

## Why is fluency a problem now?

A few years ago, a weak answer usually looked weak. It was vague, or it repeated itself, or it contradicted itself two paragraphs later. You could see the gap.

That signal is fading. A current model can write a clear, well-organized paragraph about a gene, a pathway, or a disease mechanism. It uses the right terms in the right order. It cites the kind of evidence a reviewer expects to see. The paragraph reads like it came from someone who knows the field.

**The problem is that the reading experience no longer tells you much about the content.** Fluency used to be a rough proxy for understanding. As models get better at writing, the proxy breaks. I think of this as a pretense of understanding. I do not mean the model is lying. I mean its writing has the shape of expertise whether or not the reasoning underneath holds.

## Why is biology harder than math or code?

In code, you run the tests. In math, a proof assistant like Lean can check a formal proof line by line. These checks are not perfect, but they are fast and they do not care how confident the text sounds.

Biology has few checks like that. Suppose a model proposes that a variant affects a disease through a particular regulatory element. The claim is plausible. It fits what is known. To find out if it is true, someone has to design an experiment, run it, and wait. That can take months, and a negative result is often unclear.

So the cost of a fluent wrong answer is not the same across fields. Where checking is cheap, fluency does little harm, because errors surface quickly. Where checking is slow, a convincing wrong idea can absorb real time and money before anyone sees the problem.

## Even checkers miss some errors

There is a quieter version of this problem that shows up even where checkers exist. In our recent study on translating theorems between fields of math ([Objects Without Morphisms](https://arxiv.org/abs/2610.03551)), models often dropped a hidden hypothesis when restating a theorem in a more general setting. Toward the more general setting, they widened the scope of the statement in 60.6% of rewrites. Most of these restated theorems were still true, just about a different class of objects. A truth checker would pass them.

I bring this up because it shows the pattern in a clean setting. The output read well. Often it was even true. But it had quietly changed what was being claimed. In biology, the same kind of drift is easy to imagine: a finding from one cell type, one population, or one model organism restated as if it holds in general.

## What I am less sure about

There is a fair counterargument. Human experts also sound confident when they are wrong. Grant proposals and discussion sections are full of fluent claims that later fail. Maybe models are just joining a problem science already has, and our existing defenses, such as peer review, replication, and skepticism, will handle it.

I partly agree. The difference I worry about is volume and cost. A model can produce many plausible hypotheses in the time it takes a person to write one. If each one reads as well as a careful expert's, the bottleneck moves to checking. Our checking capacity in biology has not grown at the same rate.

I am also not sure how to measure "sounding like you know" well. Calibration scores help, but a model can be well calibrated on average and still be confidently wrong on the questions that matter most for a given study.

## What should scientists do?

A few habits seem worth keeping, for my own group and for others.

**Treat model output as a hypothesis, not a finding.** This sounds obvious, but fluent text makes it easy to forget. Before acting on a suggestion, ask what experiment would show it is wrong, and how long that would take.

**Ask the model what it is unsure of, and check whether that answer is useful.** A model that can point to the weak step in its own reasoning is more helpful than one that writes a smoother paragraph.

**Build evaluations that reward honest uncertainty.** Most current benchmarks score whether an answer is right. Few score whether a model knows when it does not know, or whether it states the assumptions its answer depends on. In open-ended science, those may matter more than accuracy on questions with known answers.

None of this means we should stop using these models in biology. They are useful tools. It means the skill we need is shifting. Reading a fluent answer and asking whether it is true was always part of science. It is becoming the main part.

*This is a personal perspective. For the math study mentioned above, see the [paper](https://arxiv.org/abs/2610.03551) and my [earlier post](math-is-not-just-problem-solving.html).*
