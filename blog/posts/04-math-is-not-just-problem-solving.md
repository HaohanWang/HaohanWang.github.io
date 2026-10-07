---
title: "Math Is Not Just Problem Solving"
subtitle: "AI can now write research-level math proofs. Our new study asks whether models also track the hidden hypotheses that learning math trains us to notice."
date: 2026-10-07
tags: [AI for math, LLM reasoning, mathematical reasoning, OpenAI, evaluation, personal perspective]
slug: math-is-not-just-problem-solving
sources:
  - https://github.com/openai/math
  - https://github.com/openai/math/blob/main/lean/formalization.yaml
  - https://arxiv.org/abs/2610.03551
  - https://arxiv.org/pdf/2610.03551
---

# Math Is Not Just Problem Solving

*AI can now write research-level math proofs. Our new study asks whether models also track the hidden hypotheses that learning math trains us to notice.*

On October 6, 2026, OpenAI released 722 mathematical manuscripts, grouped into 372 result families, all produced by an unreleased internal model. According to the [repository README](https://github.com/openai/math), the model was given about 4,000 problems, and each published result used about three hours of ChatGPT Pro thinking compute on average. For 162 of the papers, the main result is formalized in Lean. The catalogue includes work on long-standing open problems.

This is a real milestone. I want to ask a different question: if a machine can solve math problems, has it learned what math is for?

**In short:**

- Solving problems is how we practice math. It is not the main reason we learn it.
- Our new paper, [Objects Without Morphisms](https://arxiv.org/abs/2610.03551), finds that seven current language models often lose a hidden hypothesis when they restate a theorem in a more general setting.
- Proof checkers and answer-based benchmarks cannot see this error, so better scores on those tests do not reveal it.

## Why do we learn math we will never use?

Most of us solved many equations in school that we never met again. We did not stop learning math when we could solve the exercise, and we did not stop because the exercise had no use in daily life. The exercises were never the point. They trained a way of thinking: say exactly what you assume, notice when an argument depends on it, and know when a result stops being true.

Most public measures of AI math ask whether the final answer or proof is correct. That matters, but it measures the exercise, not the habit of thought the exercise was meant to build.

## What did OpenAI's math release actually show?

As far as an outside reader can tell, it shows that a model can produce long, structured arguments that experts take seriously. Abridged reasoning summaries were released for 10 of the 372 families. The one for the Mézard–Parisi formula, for example, follows a single line of thought, not a vote over many guesses. Mathematicians are still checking the results, and OpenAI itself notes that some of the unformalized results "could have issues."

The release does not say how many of the roughly 4,000 problems or attempts failed. That is typical of how progress in AI math is built: many candidates are generated, and an external check, such as a verifier, a proof assistant, or a human judging significance, keeps the ones that pass. This improves the results that survive. It tells us less about what the model has understood.

## Can a model keep track of a hidden hypothesis?

We tested this on a task where no external checker can help: translating a theorem between the "dialects" of neighboring fields of math. A result about vector spaces can be restated for modules. A probability statement can be restated in measure theory.

The difficulty is that the original statement often hides one of its hypotheses in its vocabulary. "Vector space" already means the scalars come from a field, so nobody writes that down. When you restate the result for modules, you must write it down. Otherwise the new statement is about a larger class of objects. For example, the fact that every vector space has a basis becomes false for modules: ℤ/2ℤ is a ℤ-module with no basis.

Yanli Wang is the first author of this study, with Suijin Wang and Xiaopeng Yuan. We gave the task to seven models from four families. Here is what we found:

- When translating toward the more general setting, models widened the scope of the statement in **60.6%** of rewrites and narrowed it in **none**.
- When translating toward the more specific setting, they narrowed it in **28.3%** and widened it in **0.3%**.
- The pattern held for every model. Scale did not remove it. The most capable model widened least, but still in 46.7% of cases.
- Under a plain prompt, the most capable model stated the needed hypothesis in **8 of 37** rewrites that required it (21.6%). On statements written by mathematicians and taken from ProofWiki, the needed hypothesis was carried over in 4.2% of rewrites.
- Telling the model to state every hypothesis raised that rate to 89.2%, but it also kept hypotheses where they should be dropped. It wrote more without judging better when a hypothesis was needed.

Simple imprecision would produce errors in both directions. Instead, the output keeps whatever generality the input's wording implies, which looks like a missing step, not noise. In our words, the models have learned a dictionary between the objects of two fields, but not the rule that hypotheses must be carried over along with the objects.

## Why does this matter if the proofs check out?

Most of these errors produce statements that are still true, just of a different class of objects. In our data, scope was kept far more often when dropping the hypothesis would make the statement false than when the widened statement stayed true. So the part that survives is the part a truth checker would catch. The quieter error, a statement silently moved to a different setting, passes provers, type checkers, and equivalence-scored benchmarks.

Keeping track of scope is exactly the thinking math education is meant to build. It also matters in practice, because models are increasingly used to restate and formalize mathematics, and an error no checker sees is the kind that spreads.

## What I am less sure about

Our study does not test OpenAI's internal model. We tested general-purpose models, and math-specialized models may behave differently. The study covers six pairs of fields, some with few items, and our automatic measure undercounts stated hypotheses. Human mathematicians also leave hypotheses implicit, often on purpose.

There is also a fair counterargument. If a proof is checked in Lean, maybe it does not matter how the model "thinks." For a single theorem, I largely agree. My concern is the setting we are moving toward, where models write the statements, the definitions, and the translations that later proofs rely on. There, the questions that matter most are the ones no checker asks.

## What I would ask for

Celebrate the proofs. Alongside them, measure whether a model can say what a result assumes, notice when a restatement changes its meaning, and know where it stops being true. These are the skills we hope students take from math class. We should ask the same of our models before we call what they do mathematical thinking.

*This is a personal perspective. For the full method and results, see the [paper](https://arxiv.org/abs/2610.03551). For OpenAI's release, see the [openai/math repository](https://github.com/openai/math).*
