---
title: "Vision Should Be Structural"
subtitle: "Why my group spent a few years turning images into SVG code that language models can read, and what I think still holds."
date: 2026-10-05
tags: [computer vision, vector graphics, SVG, multimodal models, personal perspective]
sources:
  - https://arxiv.org/abs/2311.15543
  - https://arxiv.org/pdf/2311.15543
  - https://arxiv.org/abs/2504.09764
  - https://arxiv.org/pdf/2504.09764
  - https://openreview.net/forum?id=hDKLrK8AwP
  - https://arxiv.org/abs/2306.06094
  - https://openaccess.thecvf.com/content/WACV2025/papers/Cai_An_Investigation_on_LLMs_Visual_Understanding_Ability_using_SVG_for_WACV_2025_paper.pdf
  - https://arxiv.org/abs/2404.06479
  - https://arxiv.org/abs/2407.06581
  - https://arxiv.org/abs/2312.11556
  - https://openaccess.thecvf.com/content/CVPR2025/html/Rodriguez_StarVector_Generating_Scalable_Vector_Graphics_Code_from_Images_and_Text_CVPR_2025_paper.html
  - https://arxiv.org/abs/2505.20793
  - https://github.com/OmniSVG/OmniSVG
  - https://arxiv.org/abs/2510.11341
  - https://arxiv.org/abs/2604.08809
---

# Vision Should Be Structural

*Why my group spent a few years turning images into SVG code that language models can read, and what I think still holds.*

A few years ago I started to believe that vision models were missing something language models had. Text arrives with structure. Words form phrases, phrases form sentences, and a model can reason over those units. An image, as most vision models see it, arrives as a grid of pixels. Any structure in it has to be recovered from scratch.

My guess was that this difference matters. If vision is to become as capable as language AI, it may need a representation with explicit parts and relations. We chose SVG (Scalable Vector Graphics) as one concrete candidate. This post explains that choice, what our papers showed, and where I now think the idea is weaker than I hoped.

## Why SVG

An SVG file describes an image as a list of shapes. A circle has a center, a radius, and a fill color. A polygon has a list of points. Because the format is XML text, a language model can read it directly. The image becomes something closer to a sentence: discrete objects with attributes, in an order you can inspect.

That property suggested a simple test. Convert an image to SVG, give the SVG to a language model, and ask a question about the picture.

Our first look at this was a collaboration with Yong Jae Lee's group, led by Mu Cai and Zeyi Huang. It was [later published at WACV 2025](https://openaccess.thecvf.com/content/WACV2025/papers/Cai_An_Investigation_on_LLMs_Visual_Understanding_Ability_using_SVG_for_WACV_2025_paper.pdf) ([arXiv](https://arxiv.org/abs/2306.06094)). The study converted images to SVG and tested a text-only LLM on visual question answering, classification under distribution shift, few-shot learning, and generation. The model often did a reasonable job, which was encouraging.

## Making the SVG readable

A practical obstacle remained. Common vectorization methods tend to produce SVGs that are overly complex and hard to interpret. That led to two papers on readable SVG. In [Beyond Pixels](https://arxiv.org/abs/2311.15543), Tong Zhang, Haoyang Liu, Peiyan Zhang, Yuxuan Cheng, and I built S²VG², which fine-tunes a vision-language model (BLIP) to write SVG code. A differentiable renderer (DiffVG) then refines the shape parameters against the original image. We tested it on simple synthetic images: colored circles, rectangles, and triangles on a 3×3 grid.

On that data, the SVGs from S²VG² let GPT-4-32k answer questions about the image at almost the same accuracy as the ground-truth SVG (87.75% versus 87.73%). With SVGs from LIVE and DiffVG alone, accuracy was about 50% on yes/no questions, which is chance. In a small user study, people also found our SVGs easier to read. The lesson I took was concrete. The same image can be written as SVG in many ways, and only some of them carry structure a reader can use.

A companion paper, [Towards Readable Scalable Vector Graphic Generation](https://openreview.net/forum?id=hDKLrK8AwP) with Peiyan Zhang, tried to make readability something a model can optimize. It proposed desiderata for readable SVG code, metrics for them, and differentiable objectives that push a generator toward simpler, better-organized code.

## A harder test: charts

Synthetic shapes are a toy. Charts are a real case where structure matters, because the answer often depends on an exact bar height or line position. In [Socratic Chart](https://arxiv.org/abs/2504.09764), Yuyang Ji and I first checked whether strong multimodal models read charts visually or through shortcuts. We removed the text labels from ChartQA charts, and separately stretched charts horizontally or vertically. The paper reports drops of up to 30% for models such as GPT-4o and Gemini 2.0 Pro.

Socratic Chart converts the chart into SVG with a set of agents. Each agent extracts one kind of element, such as bars, lines, pie segments, text, or axes, and a critic agent reconciles their outputs. The SVG then goes to the model along with the image. On the label-removed charts, this reached 57.6% relaxed accuracy, against 40.8% for GPT-4V and 37.2% for Gemini 2.0. On standard ChartQA it ranked second overall, behind SIMPLOT. An ablation showed that removing the y-axis elements from the SVG cost about 7 points. That result fits the original intuition: the explicit numeric structure is what the model leans on.

## What has happened since

Other groups have pursued related ideas independently. [VDLM](https://arxiv.org/abs/2404.06479) (Wang et al., TMLR 2025) converts SVG into a higher-level text description of shapes, positions, and measurements, and reports gains over GPT-4o on low-level perception tasks. The ["VLMs are blind"](https://arxiv.org/abs/2407.06581) study found that leading vision-language models struggle with simple geometric questions, such as whether two circles overlap. Both are consistent with the view that pixel-based models do not reliably recover fine structure.

Most of the SVG activity I can find has been on generation. Systems such as [StarVector](https://openaccess.thecvf.com/content/CVPR2025/html/Rodriguez_StarVector_Generating_Scalable_Vector_Graphics_Code_from_Images_and_Text_CVPR_2025_paper.html) (CVPR 2025), [OmniSVG](https://github.com/OmniSVG/OmniSVG) (NeurIPS 2025), and [InternSVG](https://arxiv.org/abs/2510.11341) train multimodal models to write SVG for icons, illustrations, and diagrams. Others use [feedback from the rendered image](https://arxiv.org/abs/2505.20793) to train SVG generators with reinforcement learning. Some recent work also measures SVG structure directly, such as [element-level structural metrics](https://arxiv.org/abs/2604.08809), which is close to the readability question we cared about. Meanwhile, most widely used vision-language models still read images through pixel encoders.

## What I would keep, and what I would revise

I still believe the core claim: a model reasons better over a scene when the scene is given as explicit parts with attributes. Our results support this in settings where the structure is clean, such as simple shapes and charts.

I would revise how strongly I tied the idea to SVG. SVG was a convenient choice because LLMs already read code and the format is precise. But a natural photograph does not decompose neatly into circles and paths. Its SVG either loses detail or becomes too long to read. Our strongest evidence comes from synthetic images and charts, which are close to vector graphics already. I would now say the structure matters more than the format. SVG may be one useful case among several, and VDLM's intermediate description suggests the right level of abstraction may sit above raw SVG.

I would also hold the pixel-versus-structure contrast more loosely. The two can be combined, and Socratic Chart already passes both the image and the SVG to the model.

## Closing

The question I started with still seems right to me: what is the unit a vision model should reason over? For charts, diagrams, and simple graphics, explicit structure helped in our experiments. For natural images, I think the question is still open.

*This is a personal perspective. The findings it describes are early, and comments and disagreements are welcome.*
