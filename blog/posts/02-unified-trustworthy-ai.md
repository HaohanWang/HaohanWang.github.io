---
title: "A Unified View of Trustworthy AI"
subtitle: "Robustness, fairness, and interpretability are usually studied apart, but many of their methods answer the same question about data."
date: 2026-10-05
tags: [trustworthy AI, causality, robustness, fairness, personal perspective]
sources:
  - https://arxiv.org/abs/2307.16851
  - https://arxiv.org/pdf/2307.16851
  - https://arxiv.org/abs/2111.03740
  - https://proceedings.mlr.press/v180/wang22d.html
---

# A Unified View of Trustworthy AI

*Robustness, fairness, and interpretability are usually studied apart, but many of their methods answer the same question about data.*

Trustworthy machine learning is often taught as a list. There is robustness to distribution shift, and adversarial robustness. There is fairness, and there is interpretability. Each has its own venues, benchmarks, and vocabulary. A student who enters one of them can work for years without reading the others.

I think this division hides something. When I read across these areas, many methods look like the same idea in different clothes. In 2023, Haoyang Liu, Maheep Chaudhary, and I wrote [a survey](https://arxiv.org/abs/2307.16851) to make that idea explicit. This post is the short, opinionated version of why I care about it.

## The shared root is in the data

The view starts from a familiar example. Suppose we train a model to tell sea turtles from tortoises. Sea turtles are usually photographed in blue water, and tortoises on land. A model trained by standard empirical risk minimization will likely use the background, because it predicts the label well. A biologist would look at the feet or the shell.

Nothing in the training objective tells the model which signal to prefer. Both are correlated with the label. The data contains a feature we want the model to use and a feature we do not, and plain ERM has no reason to prefer one over the other.

Seen this way, several trustworthiness problems share a shape. In domain adaptation and generalization, the unwanted feature is something specific to one domain, such as a background or a texture. In fairness, it is often a sensitive attribute, such as gender or ethnicity in a hiring model. In adversarial robustness, it is a small perturbation that humans barely notice but the model responds to. Interpretability asks which features the model actually uses. The question underneath is the same in each case: which signals should the model rely on, and who decides?

## The methods converge

The survey's main observation is that methods built independently in these areas converge to a few forms. We wrote them as "master equations."

One recurring form adds an adversarial term. The model is trained to predict the label while a second model tries to recover something it should ignore. In domain adaptation, that something is the domain. In fairness, the same construction appears with the sensitive attribute in place of the domain. Several early fairness methods reuse the domain-adversarial network with only that substitution.

Adversarial training gives another form. It trains on worst-case perturbed inputs within some allowed distance. The same idea appears in domain generalization as data augmentation.

Sample reweighting is a plug-in that can be added to either form. It shows up in robustness, and in fairness work on groups that are underrepresented in the data.

Interpretability fits less cleanly. Perturbation-based and gradient-based explanation methods share a form with adversarial attacks, but our equation for them is less precise than the others. The survey says so directly.

The survey then connects these forms to Pearl's ladder of causation. Reweighting samples resembles inverse probability weighting, a standard tool for estimating the effect of an intervention. Augmentation that changes an unwanted feature and keeps everything else fixed asks a counterfactual question: what would this input have looked like with a different background? Many methods that never mention causality appear to make causal assumptions anyway. This line of thinking builds on earlier work of mine. A [UAI 2022 paper](https://proceedings.mlr.press/v180/wang22d.html), for example, derived a generalization bound that leads to the same families of methods.

## What the unified view buys

Some of the benefit is practical. If you know that a fairness method and a domain adaptation method share an equation, you can borrow progress from one area for the other. You also learn to recognize when a new paper reinvents an old method under a new name.

The view also exposes assumptions. In the survey we argue that a trustworthiness property is not well defined until we say what the model should be robust against, fair with respect to, or interpretable to. Those choices come from stakeholders, and they enter the method as a regularizer or an augmentation. A unified view makes that dependence visible. It moves the conversation from "which method is best" toward "what knowledge about the data did this method assume."

The same lens extends to large pretrained models. Fine-tuning, parameter-efficient tuning, and prompting can all be written as variants of ERM. If that holds, the same master equations should apply to them, and the survey reviews early methods that do this.

## Where the view is limited

The survey covers robustness, adversarial robustness, fairness, and interpretability. It explicitly sets aside privacy and label noise. I would like the unified view to reach privacy, but I have not shown that it does, and the fit may be poor. Privacy concerns what a model reveals about individual training points. That is a different question from which features the model relies on.

The view also takes a technical stance on fairness. It treats a fairness criterion as given and asks how to enforce it. Much of the hard work in fairness is deciding what "fair" should mean, and a shared equation says nothing about that.

The causal reading has its own limits. In deep learning, the features we want and the features we do not are rarely observed or cleanly separable. The survey notes that unobserved variables and entangled features make direct causal inference difficult. A unifying language can describe methods without making them work better.

Finally, a unification can flatten real differences. Adversarial robustness concerns an attacker who adapts, and domain shift usually does not. Writing both as one equation is useful for seeing the shared structure. It can also make a reader forget the threat model.

## Closing

I do not think the separate subfields should merge. Each has questions the others do not ask. But I think students and reviewers gain from seeing the shared root first. Many trustworthiness failures begin with a model that learned a correlation we did not want it to use. Naming that root makes it easier to see which part of a new problem is old.

*This is a personal perspective. The survey is at [arXiv:2307.16851](https://arxiv.org/abs/2307.16851), and I welcome disagreement.*
