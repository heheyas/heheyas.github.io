# Zilong Chen's CV

- Phone: +86 186 2945 1544
- Email: [jaysonabcchen@gmail.com](mailto:jaysonabcchen@gmail.com)
- Location: Tsinghua University, Beijing, China
- Website: [heheyas.github.io](https://heheyas.github.io/)
- LinkedIn: [zilong-chen-99671523b](https://linkedin.com/in/zilong-chen-99671523b)
- GitHub: [heheyas](https://github.com/heheyas)
- Google Scholar: [2pbka1gAAAAJ](https://scholar.google.com/citations?user=2pbka1gAAAAJ)


# Summary

I work on multimodal generation, currently on turning the text interface of a generative model into something that can be measured and scaled. My earlier work covers 3D and 4D reconstruction and generation, including text-to-3D with Gaussian splatting, video diffusion models as 3D generators, and native mesh generation, published at CVPR, NeurIPS, and T-PAMI. Before Tsinghua I worked on knowledge graphs and their applications in natural language processing.

# Education

## Tsinghua University, PhD in Computer Science

- Sept 2022 – present
- Advisor: [Huaping Liu](https://sites.google.com/site/thuliuhuaping)

## Xi'an Jiaotong University, BS in Physics

- Sept 2018 – July 2022
- Advisor: [Minnan Luo](https://gr.xjtu.edu.cn/web/minnluo)

# Experience

## ByteDance Seed., Top Seed intern on multimodal generation, led by [Haoqi Fan](https://haoqifan.github.io/)

- July 2025 – present
- Beijing, China
- **Seedream 5.0**:
 
    - Designed the structured prompt (SP) annotation pipeline and verified the effectiveness of SP on DiT.
 
    - Trained the prompter rewriting user prompts into SPs, exploring reward models, RL recipes, self-distillation, and thinking patterns.
 
    - Built the editing SP data pipeline, mining supervision from video and extending structured prompts from generation to instruction-based editing.

- **Scaling Properties of Text Conditioning in Visual Generation** [1]:
 
    - Showed that scaling visual generation means scaling caption informativeness and the LLM that produces it, not the DiT alone.
 
    - Across 15 controlled runs with data, architecture, and compute fixed, converged diffusion loss tracks caption informativeness, not caption length.
 
    - Proposed the diffusability × promptability decomposition of the caption interface, separating what the diffuser can use from what an LLM can instantiate.

- **Open-sourced unified model and data engine**:
 
    - Co-led LightFusion [3], fusing off-the-shelf generation and understanding models via interleaved multimodal self-attention: 0.91 GenEval and 82.16 DPG-Bench on ~35B tokens.
 
    - Co-led VQ-VA World [2], an agentic pipeline crawling ~1.8M interleaved image-text samples plus the IntelligentBench benchmark, lifting LightFusion from 7.78 to 53.06.

- **Seed world model** (ongoing):
 
    - Continued training on top of Seedance 2.5.
 
    - Built the captioning workflow, annotating both event-level and global information.
 
    - Owned its prompt enhancement model, proposing an offline + online scheme that meets the world model's latency budget.
 
    - Designed the 4D structured prompt and reference-to-world interfaces, giving control through 3D bounding boxes, reference views, and object references.

- **Negative results**: tested a pretrained ViT as the VAE and a fully discrete unified model, among other alternatives to the continuous latent; none outperformed VAE-based latent diffusion in our settings.

## Shengshu Inc., Research intern on video and 3D generation

- Nov 2023 – Mar 2025
- Beijing, China
- Alleviating Janus problem in optimization-based 3D generation methods. (CVPR 2024 [6])
- Finetune video diffusion model for 3D generation.
- Native 3D generation using limited 3D data. (CVPR 2025 Highlight [4])

# Publications (= Indicates Equal Contribution)

## [1] Scaling Properties of Text Conditioning in Visual Generation ([https://heheyas.github.io/context-scaling/](heheyas.github.io/context-scaling))
- ByteDance Seed 2026
- **#underline[Zilong Chen]**, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan

## [2] VQ-VA World: Towards High-Quality Visual Question-Visual Answering ([https://chenhuigou.github.io/VQ-VA-World/](chenhuigou.github.io/VQ-VA-World))
- CVPR 2026
- Chenhui Gou=, **#underline[Zilong Chen]=**, Zeyu Wang=, Feng Li, Deyao Zhu, Zicheng Duan, Kunchang Li, Chaorui Deng, Hongyi Yuan, Haoqi Fan, Cihang Xie, Jianfei Cai, Hamid Rezatofighi

## [3] LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation ([https://arxiv.org/abs/2510.22946](arxiv.org/abs/2510.22946))
- ECCV 2026
- Zeyu Wang=, **#underline[Zilong Chen]=**, Chenhui Gou=, Feng Li, Chaorui Deng, Deyao Zhu, Kunchang Li, Weihao Yu, Haoqin Tu, Haoqi Fan, Cihang Xie

## [4] MeshGen: Generating PBR Textured Mesh with Render-Enhanced Auto-Encoder and Generative Data Augmentation ([https://heheyas.github.io/MeshGen](heheyas.github.io/MeshGen))
- CVPR 2025 (**Highlight**)
- **#underline[Zilong Chen]**, Yikai Wang, Wenqiang Sun, Feng Wang, Yiwen Chen, Huaping Liu

## [5] V3D: Video Diffusion Models Are Effective 3D Generators ([https://heheyas.github.io/V3D](heheyas.github.io/V3D))
- T-PAMI 2025
- **#underline[Zilong Chen]**, Yikai Wang, Feng Wang, Zhengyi Wang, Huaping Liu

## [6] Text-to-3D Using Gaussian Splatting ([https://gsgen3d.github.io/](gsgen3d.github.io))
- CVPR 2024
- **#underline[Zilong Chen]**, Feng Wang, Yikai Wang, Huaping Liu

## [7] GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting ([https://buaacyw.github.io/gaussian-editor/](buaacyw.github.io/gaussian-editor))
- CVPR 2024
- Yiwen Chen=, **#underline[Zilong Chen]=**, Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin

## [8] Masked Space-Time Hash Encoding for Efficient Dynamic Scene Reconstruction ([https://masked-spacetime-hashing.github.io/](masked-spacetime-hashing.github.io))
- NeurIPS 2023 (**Spotlight**)
- Feng Wang=, **#underline[Zilong Chen]=**, Guokang Wang, Yafei Song, Huaping Liu

## [9] Video4DGen: Enhancing Video and 4D Generation Through Mutual Optimization ([https://vidu4d-dgs.github.io/](vidu4d-dgs.github.io))
- T-PAMI 2025
- Yikai Wang, Guangce Liu, Xinzhou Wang, **#underline[Zilong Chen]**, Jiafang Li, Xin Liang, Fuchun Sun, Jun Zhu

## [10] Vidu4D: Single Generated Video to High-Fidelity 4D Reconstruction with Dynamic Gaussian Surfels ([https://vidu4d-dgs.github.io/](vidu4d-dgs.github.io))
- NeurIPS 2024
- Yikai Wang, Xinzhou Wang, **#underline[Zilong Chen]**, Zhengyi Wang, Fuchun Sun, Jun Zhu

## [11] MeshAnything V2: Artist-Created Mesh Generation with Adjacent Mesh Tokenization ([https://buaacyw.github.io/meshanything-v2/](buaacyw.github.io/meshanything-v2))
- arXiv 2024
- Yiwen Chen, Yikai Wang, Yihao Luo, Zhengyi Wang, **#underline[Zilong Chen]**, Jun Zhu, Chi Zhang, Guosheng Lin

## [12] DimensionX: Create Any 3D and 4D Scenes from a Single Image with Controllable Video Diffusion ([https://chenshuo20.github.io/DimensionX/](chenshuo20.github.io/DimensionX))
- arXiv 2024
- Wenqiang Sun, Shuo Chen, Fangfu Liu, **#underline[Zilong Chen]**, Yueqi Duan, Jun Zhang, Yikai Wang

## [13] FreePlane: Unlocking Free Lunch in Triplane-Based Sparse-View Reconstruction Models ([https://freeplane3d.github.io/](freeplane3d.github.io))
- arXiv 2024
- Wenqiang Sun, Zhengyi Wang, Shuo Chen, Yikai Wang, **#underline[Zilong Chen]**, Jun Zhu, Jun Zhang

## [14] TwiBot-22: Towards Graph-Based Twitter Bot Detection 
- NeurIPS 2022
- Shangbin Feng=, Zhaoxuan Tan=, Herun Wan=, Ningnan Wang=, **#underline[Zilong Chen]=**, Binchi Zhang=, Qinghua Zheng, Wenqian Zhang, Zhenyu Lei, Shujie Yang, others

## [15] Knowledge Graph Augmented Political Perspective Detection in News Media 
- arXiv 2021
- Shangbin Feng, **#underline[Zilong Chen]**, Qingyao Li, Minnan Luo

## [16] Encoding Heterogeneous Social and Political Context for Entity Stance Prediction 
- arXiv 2021
- Shangbin Feng, **#underline[Zilong Chen]**, Peisheng Yu, Minnan Luo

## [17] KCD: Knowledge Walks and Textual Cues Enhanced Political Perspective Detection in News Media 
- NAACL 2022 (**Oral**)
- Wenqian Zhang=, Shangbin Feng=, **#underline[Zilong Chen]=**, Zhenyu Lei, Jundong Li, Minnan Luo

## [18] BIC: Twitter Bot Detection with Text-Graph Interaction and Semantic Consistency 
- ACL 2023
- Zhenyu Lei, Herun Wan, Wenqian Zhang, Shangbin Feng, **#underline[Zilong Chen]**, Jundong Li, Qinghua Zheng, Minnan Luo

## [19] KRACL: Contrastive Learning with Graph Context Modeling for Sparse Knowledge Graph Completion 
- WWW 2023
- Zhaoxuan Tan, **#underline[Zilong Chen]**, Shangbin Feng, Qingyue Zhang, Qinghua Zheng, Jundong Li, Minnan Luo

## [20] KGAP: Knowledge Graph Augmented Political Perspective Detection in News Media 
- arXiv 2021
- Shangbin Feng, **#underline[Zilong Chen]**, Wenqian Zhang, Qingyao Li, Qinghua Zheng, Xiaojun Chang, Minnan Luo

## [21] PAR: Political Actor Representation Learning with Social Context and Expert Knowledge 
- EMNLP 2022
- Shangbin Feng, Zhaoxuan Tan, **#underline[Zilong Chen]**, Ningnan Wang, Peisheng Yu, Qinghua Zheng, Xiaojun Chang, Minnan Luo

# Awards

## Huiyan Scholarship (Tsinghua University)

- 2024

## Track winner, BMW hackathon

- 2023

# Technologies

- Languages: C++, C, CUDA, Python
- Software: Blender
