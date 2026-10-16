---
title: "Why Alzheimer's Patients With the Same Diagnosis Differ"
subtitle: "One diagnosis of Alzheimer's disease covers patients whose brains, proteins, and genes follow different paths. We should study each patient's profile, not only the average patient."
date: 2026-10-16
tags: [Alzheimer's disease, disease heterogeneity, genetics, precision medicine, computational biology, personal perspective]
slug: alzheimers-same-diagnosis-different-patients
target_query: "Why do Alzheimer's patients with the same diagnosis progress differently?"
sources:
  - https://doi.org/10.1038/s44400-026-00124-5
  - https://doi.org/10.1212/WNL.0000000000009058
  - https://doi.org/10.1038/s41591-021-01309-6
  - https://doi.org/10.1038/s43587-023-00550-7
  - https://doi.org/10.1038/s41591-024-02931-w
  - https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761269s013lbl.pdf
  - https://doi.org/10.1007/s00401-017-1717-7
  - https://doi.org/10.1002/alz.093276
  - https://arxiv.org/abs/2412.00160
  - https://doi.org/10.1093/braincomms/fcae426
---

# Why Alzheimer's Patients With the Same Diagnosis Differ

*One diagnosis of Alzheimer's disease covers patients whose brains, proteins, and genes follow different paths. We should study each patient's profile, not only the average patient.*

Two people can receive the same diagnosis of Alzheimer's disease and then decline in very different ways. One loses memory first and fast. Another keeps memory longer but struggles with language or vision. The short answer to why is that "Alzheimer's" is one label for several patterns. Patients differ in where pathology spreads in the brain, which molecular processes go wrong, which other brain diseases they carry at the same time, and which genetic variants they inherited. My view is that this variation is not noise around one typical patient. It has structure, and we should measure it patient by patient.

**In short:**

- Imaging and autopsy studies keep finding recurring subtypes of Alzheimer's disease. A meta-analysis found that the "typical" pattern describes only about half of patients.
- Genetics is part of the story. Two copies of APOE4 change both how the disease unfolds and how risky the new antibody drugs are.
- The evidence for subtypes is strong at the group level and weaker for assigning any single patient. That is a reason to build patient-level profiles carefully, not a reason to ignore the variation.

## How different can two Alzheimer's patients be?

Quite different, and in consistent ways. A [2020 systematic review and meta-analysis in *Neurology*](https://doi.org/10.1212/WNL.0000000000009058) pooled autopsy and imaging studies. Three subtypes kept appearing. "Typical" Alzheimer's, with damage in both the hippocampus and the cortex, had a pooled frequency of 55%. Limbic-predominant disease was 21%, and hippocampal-sparing disease was 17%. A minimal-atrophy group, at 15%, showed up in several imaging studies. The subtypes differed in age at onset, sex, education, APOE4 status, and spinal fluid biomarkers.

Tau imaging tells a similar story. Using tau PET scans from 1,612 people, [Vogel and colleagues](https://doi.org/10.1038/s41591-021-01309-6) found four distinct paths of tau spread, each covering 18% to 33% of patients. The subtypes were stable over follow-up and replicated in a separate sample with a different tracer. They also had different cognitive profiles and outcomes. The authors suggested that the idea of "typical AD" may need a second look.

The variation goes below the level of brain images. [A 2024 study in *Nature Aging*](https://doi.org/10.1038/s43587-023-00550-7) measured proteins in spinal fluid from 419 people with Alzheimer's and 187 controls. It found five molecular subtypes, tied to different processes such as immune activation and blood–brain barrier damage. Each subtype was linked to specific genetic risk variants, and the subtypes differed in survival.

And many patients have more than one disease. [A review by Kapasi, DeCarli, and Schneider](https://doi.org/10.1007/s00401-017-1717-7) describes how older people with Alzheimer's pathology often also carry vascular damage, Lewy bodies, or TDP-43 pathology. These extra pathologies lower the threshold at which dementia becomes visible. So two patients with the same amyloid and tau load can still look different in the clinic.

## Do genes explain some of the difference?

Yes, and the clearest case is APOE4. In a study of more than 10,000 people, [Fortea and colleagues](https://doi.org/10.1038/s41591-024-02931-w) found that almost all people with two copies of APOE4 showed Alzheimer's pathology. Their symptoms began earlier, at about 65, and at a more predictable age than in people with two copies of APOE3. The authors argue that APOE4 homozygosity should be seen as a distinct genetic form of the disease, not only as a risk factor.

This is not only a research question. According to the [FDA label for lecanemab](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761269s013lbl.pdf), about 15% of Alzheimer's patients are APOE4 homozygotes. In the phase 3 trial, brain swelling or bleeding on MRI (called ARIA) occurred in 45% of homozygotes on the drug, compared with 19% of heterozygotes and 13% of non-carriers. The label now says genotype testing should be done before treatment. **The same diagnosis already carries different risks for the same drug, depending on a patient's genes.**

Beyond APOE, the picture is less settled but points the same way. [Elman, Schork, and Rangan](https://doi.org/10.1002/alz.093276) found genetic signatures present in subsets of Alzheimer's cases but not in controls. In 399 people with mild cognitive impairment, one signature group showed faster cognitive decline and a faster rise in tau.

Our own recent work asked a related question. In [a paper in *npj Dementia*](https://doi.org/10.1038/s44400-026-00124-5), we built a genetic profile for each patient instead of one average effect for the whole cohort. Among 251 Alzheimer's patients in the ADNI cohort, the profiles split into two groups of 232 and 19 patients. The smaller group did worse across five memory measures. The split held in 500 subsampling runs, and it was not explained by ancestry, age, sex, or education. Variants linked to other brain traits, especially epilepsy, separated the two groups, including a variant near the sodium channel gene *SCN1A*. We call this exploratory. It is one cohort, the smaller group is small, and it needs replication and long-term follow-up. More on this line of work is on my [gene regulation and disease genetics page](../research/gene-regulation-disease-genetics.html).

## Are Alzheimer's subtypes real, or an artifact of the method?

This is the strongest objection, and it deserves a direct answer. Clustering methods always return clusters. Some of what looks like a subtype may just reflect how advanced the disease is. Ferreira and colleagues themselves propose that two continuous dimensions, typicality and severity, may describe the variation better than separate boxes.

Assigning individual patients is also shaky. A [2024 study in *Brain Communications*](https://doi.org/10.1093/braincomms/fcae426) derived subtypes from glucose PET and from MRI in the same ADNI patients. Both found cortical- and limbic-predominant patterns. But the subtype a patient received from one scan did not consistently match the subtype from the other.

At the group level, the patterns hold up better. [A reproducibility study](https://arxiv.org/abs/2412.00160) ran the same subtyping method on 5,444 people across three cohorts and recovered the same three atrophy subtypes in each. Its authors also note that these cohorts lack ethnic diversity, which applies to most of the studies here, including ours.

My reading is this. **The evidence that patients vary in systematic ways is strong. The evidence that we can sort any one patient into a fixed box is weak.** The conclusion I draw is not to drop the idea of heterogeneity. It is to treat each patient as a profile with several continuous dimensions, measured from more than one kind of data, and to test whether those profiles predict what happens next.

## What would change if we studied each patient?

A few things seem worth doing, for my group and for the field.

**Report how results vary across patients, not only the average.** A drug or a gene effect that is small on average may be large in a subgroup and absent in others. The APOE4 safety data show how much an average can hide.

**Link genetic profiles to how the disease unfolds over time.** Most subtype studies, ours included, are cross-sectional. The useful question is whether a profile measured early predicts the path a patient takes.

**Replicate in diverse cohorts before anything reaches the clinic.** Subtype findings are cheap to generate and expensive to confirm. Most were found in cohorts of mainly European ancestry.

A diagnosis is a starting point, not a description of the patient. For Alzheimer's disease, I think the next step is to describe each patient more fully and check whether the description helps.

*This is a personal perspective, not medical advice. For the study discussed above, see the [paper](https://doi.org/10.1038/s44400-026-00124-5) and the [code](https://github.com/zjh688/Het-PR).*
