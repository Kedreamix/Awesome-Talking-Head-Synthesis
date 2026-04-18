# Awesome-Talking-Head-Synthesis

- [Datasets](#datasets)
- [Survey](#survey)
- [Funny Work](#funny-work)
- [Audio-driven](#audio-driven)
- [Portrait Animation](#portrait-animation)
- [Text-driven](#text-driven)
- [NeRF \& 3D Head Avatar](#nerf--3d-head-avatar)
- [3D Gaussian Splatting](#3d-gaussian-splatting)
- [Conversational \& Dialogue](#conversational--dialogue)
- [Talking Body \& Avatar](#talking-body--avatar)
- [Metrics](#metrics)
- [Tools \& Software](#tools--software)
- [Slides \& Presentations](#slides--presentations)
- [References](#references)
- [Star History](#star-history)

This repository organizes papers, codes and resources related to generative adversarial networks (GANs) 🤗 and neural radiance fields (NeRF) 🎨, with a main focus on image-driven and audio-driven talking head synthesis papers and released codes. 👤

Papers for Talking Head Synthesis, released codes collections. ✍️

Most papers are linked to PDFs on "arXiv" or journal/conference websites 📚. However, some papers require an academic license to view 🔐.

🔆 This project Awesome-Talking-Head-Synthesis is ongoing - pull requests are welcome! If you have any suggestions (missing papers, new papers, key researchers or typos), please feel free to edit and submit a PR. You can also open an issue or contact me directly via email. 📩

⭐ If you find this repo useful, please give it a star! 🤩



**2023.12 Update** 📆

Thank you to https://github.com/Curated-Awesome-Lists/awesome-ai-talking-heads, I have added some of its contents, such as `Tools & Software` and `Slides & Presentations`. 🙏 I hope this will be helpful.😊

If you have any feedback or ideas on extending this aggregated resource, please open an issue or PR - community contributions are vital to advancing this shared knowledge. 🤝

Let's keep pushing forward to recreate ever more realistic digital human faces! 💪 We've come so far but still have a long way to go. With continued research 🔬 and collaboration, I'm sure we'll get there! 🤗

Please feel free to star ⭐ and share this repo if you find it a valuable resource. Your support helps motivate me to keep maintaining and improving it. 🥰 Let me know if you have any other questions!

---



## Datasets

![dataset描述](https://img-blog.csdnimg.cn/direct/841257d9dee74547bbd4f717794a9492.png#pic_center)

| Year | Dataset | Conference/Journal | Download Link | Description |
| ---- | ---- | ---- | ---- | ---- |
| 2026 | [Leveraging Avatar Fingerprinting: A Multi-Generator Photorealistic Talking-Head Public Database and Benchmark](http://arxiv.org/abs/2603.26934) | ArXiv 2026 | N/A | Multi-generator benchmark for talking-head avatar fingerprinting and photorealistic avatar generation evaluation. |
| 2026 | [A Near-Raw Talking-Head Video Dataset for Various Computer Vision Tasks](http://arxiv.org/abs/2603.26763) | ArXiv 2026 | N/A | Near-raw talking-head video dataset for computer vision tasks including detection, recognition, and generation. |
| 2026 | [Face-to-Face: A Video Dataset for Multi-Person Interaction Modeling](http://arxiv.org/abs/2603.14794) | ArXiv 2026 | [Download](https://huggingface.co/datasets/ernestchu/f2f-jf) | 70-hour, 14k-clip dataset of two-person talk-show exchanges for multi-person interaction modeling. |
| 2026 | [SFQA](http://arxiv.org/abs/2601.20385) | ArXiv | N/A | A dataset for singing face generation quality assessment with 5,184 videos generated from 100 photographs and 36 music clips using 12 generation methods. |
| 2025 | [TalkCuts](http://arxiv.org/abs/2510.07249) | ArXiv 2025 | [Download](https://talkcuts.github.io) | A large-scale dataset with 164k clips totaling over 500 hours of human speech videos featuring diverse camera shots and detailed annotations including textual descriptions, 2D keypoints, and 3D SMPL-X motions for multi-shot speech video generation. |
| 2025 | [EmojiBench++](http://arxiv.org/abs/2509.16630) | IJCV 2025 | [Download](https://follow-your-emoji.github.io/) | A comprehensive benchmark for portrait animation comprising diverse portraits, driving videos, and landmark sequences. |
| 2025 | [Multi-human Interactive](https://arxiv.org/abs/2508.03050) | ArXiv 2025 | [Download](https://github.com/showlab/Multi-human-Talking-Video-Dataset) | 12 hours of high-res footage with 2-4 speakers, fine-grained body pose and speech interaction annotations. |
| 2025 | [THQA-10K](https://arxiv.org/abs/2507.23343) | ArXiv 2025 | [Download](https://github.com/zyj-2000/Talker) | Largest AGTH quality assessment dataset with 10,457 samples from 12 T2I models and 14 talkers. |
| 2025 | [SpeakerVid-5M](http://arxiv.org/abs/2507.09862) | ArXiv | [Download](https://dorniwang.github.io/SpeakerVid-5M) | Large-scale dataset with 5.2M video clips (8,743 hours) for audio-visual dyadic interactive virtual human generation, covering monadic talking, listening, and dyadic conversations, with pre-training and SFT subsets. |
| 2025 | [TalkingHeadBench](https://arxiv.org/abs/2505.24866) | WACV 2026 | [Download](https://huggingface.co/datasets/luchaoqi/TalkingHeadBench) | Comprehensive benchmark for talking-head deepfake detection with multi-model generators. |
| 2025 | [Motion-X++](https://arxiv.org/abs/2501.05098) | ArXiv 2025 | N/A | 19.5M 3D whole-body pose annotations covering 120.5K motion sequences with 80.8K RGB videos. |
| 2024 | [GLCF (MSTF)](https://arxiv.org/abs/2412.13656) | ArXiv 2024 | N/A | First large-scale multi-scenario talking face dataset with 22 audio/video forgery techniques. |
| 2024 | [SAVEE](https://arxiv.org/abs/2411.02964) | ArXiv 2024 | [Download](http://kahlan.eps.surrey.ac.uk/savee/Download.html) | 480 British English utterances from 4 male actors expressing 7 emotions. |
| 2024 | [Allo-AVA](https://arxiv.org/abs/2410.16503) | ArXiv 2024 | N/A | ~1,250 hours of conversational content for allocentric avatar gesture animation. |
| 2024 | [MMHead](http://arxiv.org/abs/2410.07757) | ACMMM 2024 | [Download](https://github.com/wsj-sjtu/MMHead) | Large-scale multi-modal 3D facial animation dataset with 49 hours of 3D facial motion sequences, speech audios, and hierarchical text annotations for text-induced 3D talking head animation and text-to-3D facial motion generation. |
| 2024 | [DH-FaceVid-1K](https://arxiv.org/abs/2410.07151) | ICCV 2025 | [Download](https://luna-ai-lab.github.io/DH-FaceVid-1K/) | 1,200 hours, 270K+ clips from 20K+ individuals with speech audio, keypoints, and text annotations. |
| 2024 | [MultiTalk](https://arxiv.org/abs/2406.14272) | CVPR 2024 | [Download](https://github.com/postech-ami/MultiTalk/tree/main/MultiTalk_dataset) | 420+ hours across 20 languages, 293K clips (512x512, 25fps, avg 5.19s duration). |
| 2024 | [THQA](https://arxiv.org/abs/2404.09003) | ArXiv 2024 | [Download](https://github.com/zyj-2000/THQA) | 800 talking head videos from 8 speech-driven methods with subjective quality assessments. |
| 2023 | [GRID](https://arxiv.org/abs/2312.09727) | ArXiv 2023 | [Download](http://spandh.dcs.shef.ac.uk/avlombard/) | 34 volunteers each speaking 1000 phrases (34K utterances) with 6-word sentence structures. |
| 2023 | [ViCo](http://arxiv.org/abs/2307.02090) | ArXiv 2023 | [Download](https://vico.solutions/) | ViCo and ViCo-X are datasets for conversational head generation, with ViCo for sentence-level independent talking and listening tasks, and ViCo-X for multi-turn conversational scenarios. |
| 2023 | [TalkingHead-1KH](https://arxiv.org/abs/2306.11541) | ArXiv 2023 | [Download](https://github.com/tcwang0509/TalkingHead-1KH) | 500K video clips with ~80K greater than 512x512 resolution. Only permissive license videos included. |
| 2023 | [CelebV](https://arxiv.org/abs/2303.14717) | CVPR 2023 | [Download](https://drive.google.com/file/d/1jQ6d76T5GQuvQH4dq8_Wq1T0cxvN0_xp/view) | Includes CelebV-Text with 70,000 in-the-wild face video clips for text-to-video generation. |
| 2023 | [MMFace4D](https://arxiv.org/abs/2303.09797) | ArXiv 2023 | [Download](https://wuhaozhe.github.io/mmface4d/) | Large-scale multi-modal 4D dataset with 35,000+ sequences from 431 subjects (age 15-68). |
| 2022 | [CelebV-HQ](https://arxiv.org/abs/2207.12393) | ECCV 2022 | [Download](https://github.com/CelebV-HQ/CelebV-HQ) | 35,666 clips with 15,653 identities, each labeled with 83 facial attributes. |
| 2022 | [Multiface](https://arxiv.org/abs/2207.11243) | NeurIPS 2022 | [Download](https://github.com/facebookresearch/multiface) | High-quality multi-view recordings of 13 people with 12K-23K frames per subject at 30fps. 65TB dataset. |
| 2022 | [VFHQ](https://arxiv.org/abs/2205.03409) | CVPRW 2022 | [Download](https://liangbinxie.github.io/projects/vfhq) | 16,000+ high-fidelity clips for video face super-resolution research. |
| 2021 | [HDTF](https://arxiv.org/abs/2106.00656) | CVPR 2021 | [Download](https://github.com/MRzzm/HDTF) | High-definition Talking-Face Dataset with ~362 videos (15.8 hours) in 720P/1080P resolution. |
| 2020 | [MEAD](https://arxiv.org/abs/2005.05136) | ECCV 2020 | [Download](https://github.com/uniBruce/Mead) | Large-scale audio-visual dataset with 60 actors expressing 8 emotions at 3 intensity levels. |
| 2019 | [BIWI](https://arxiv.org/abs/1910.03735) | ArXiv 2019 | [Download](https://data.vision.ee.ethz.ch/cvl/datasets/b3dac2.en.html) | 3D Audiovisual Corpus of Affective Communication with 40 sentences spoken by 14 subjects. |
| 2019 | [VOCA](https://arxiv.org/abs/1905.00313) | SIGGRAPH 2019 | [Download](https://voca.is.tue.mpg.de/) | 4D-face dataset with ~29 minutes of 4D face scans and synchronized audio from 12 speakers. |
| 2019 | [CN-CVS](https://arxiv.org/abs/1904.03111) | ArXiv 2019 | [Download](https://cnceleb.org) | Large-scale continuous visual-speech dataset in Mandarin Chinese from TV news and speech shows. |
| 2019 | [FaceForensics++](https://arxiv.org/abs/1901.08971) | ICCV 2019 | [Download](https://github.com/ondyari/FaceForensics) | Large-scale dataset for detecting manipulated facial images with over 1.8M images. |
| 2018 | [VoxCeleb2](https://arxiv.org/abs/1806.05622) | Interspeech 2018 | [Download](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox2.html) | Largest public audio-visual dataset with video URLs and timestamps. Requires 300GB+ storage. |
| 2018 | [LRS2](https://arxiv.org/abs/1611.05358) | ArXiv 2018 | [Download](https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrs2.html) | Lip reading dataset with videos recorded in diverse settings from BBC television. |
| 2018 | [LRW](https://arxiv.org/abs/1611.05358) | ACCV 2018 | [Download](https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrw1.html) | Diverse English-speaking dataset from BBC with 1000+ speakers. Each video is 1.16s (29 frames). |
| 2017 | [VoxCeleb1](https://arxiv.org/abs/1706.08612) | Interspeech 2017 | [Download](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html) | Contains over 100,000 utterances for 1,251 celebrities, extracted from YouTube videos. |
| 2017 | [ObamaSet](https://dl.acm.org/doi/10.1145/3072959.3073640) | SIGGRAPH 2017 | [Download](https://github.com/supasorn/synthesizing_obama_network_training) | Specialized audio-visual dataset focused on analyzing visual speech of Barack Obama from weekly address footage. |
| 2014 | [CREMA-D](https://arxiv.org/abs/2301.12331) | ACM TOCC 2014 | [Download](https://github.com/CheyneyComputerScience/CREMA-D) | Diverse dataset with 7,442 clips featuring 91 actors (48 male, 43 female) aged 20-74, expressing six emotions at four intensity levels. |

---



## Survey

| Year | Title | Conference/Journal |
| ---- | ---- | ---- |
| 2025 | [A Survey of Body and Face Motion: Datasets, Performance Evaluation Metrics and Generative Techniques](https://arxiv.org/abs/2512.09005) | ArXiv 2025 |
| 2025 | [Human Motion Video Generation: A Survey](https://arxiv.org/abs/2509.03883) | TPAMI |
| 2025 | [A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977) | ArXiv 2025 |
| 2025 | [Controllable Video Generation: A Survey](https://arxiv.org/abs/2507.16869) | ArXiv 2025 |
| 2025 | [Advancing Talking Head Generation: A Comprehensive Survey of Multi-Modal Methodologies, Datasets, Evaluation Metrics, and Loss Functions](http://arxiv.org/abs/2507.02900) | ArXiv 2025 |
| 2025 | [Survey of Video Diffusion Models: Foundations, Implementations, and Applications](https://arxiv.org/abs/2504.16081) | TMLR |
| 2025 | [A Survey on Human Interaction Motion Generation](https://arxiv.org/abs/2503.12763) | ArXiv 2025 |
| 2024 | [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://arxiv.org/abs/2412.06602) | EMNLP 2025 |
| 2024 | [Passive Deepfake Detection Across Multi-modalities: A Comprehensive Survey](https://arxiv.org/abs/2411.17911) | ArXiv 2024 |
| 2024 | [3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418) | ArXiv 2024 |
| 2024 | [A Comprehensive Survey on Human Video Generation: Challenges, Methods, and Insights](https://arxiv.org/abs/2407.08428) | ArXiv 2024 |
| 2024 | [A Survey on 3D Human Avatar Modeling — From Reconstruction to Generation](http://arxiv.org/abs/2406.04253) | ArXiv 2024 |
| 2024 | [Video Diffusion Models: A Survey](https://arxiv.org/abs/2405.03150) | ArXiv 2024 |
| 2024 | [Deepfake Generation and Detection: A Benchmark and Survey](https://arxiv.org/abs/2403.17881) | ACM Computing Surveys |
| 2024 | [A Comparative Study of Perceptual Quality Metrics for Audio-driven Talking Head Videos](http://arxiv.org/abs/2403.06421) | ArXiv 2024 |
| 2024 | [How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey](https://arxiv.org/abs/2402.13255) | ArXiv 2024 |
| 2024 | [3D Gaussian as a New Vision Era: A Survey](https://arxiv.org/abs/2402.07181) | IEEE TVCG |
| 2024 | [Advances in 3D Generation: A Survey](https://arxiv.org/abs/2401.17807) | ArXiv 2024 |
| 2024 | [A Survey on 3D Gaussian Splatting](https://arxiv.org/abs/2401.03890.pdf) | ArXiv 2024 |
| 2024 | [Neural Radiance Fields: Past, Present, and Future](https://arxiv.org/abs/2304.10050.pdf) | ArXiv 2024 |
| 2023 | [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](https://arxiv.org/abs/2308.16041) | ArXiv 2023 |
| 2023 | [Human Motion Generation: A Survey](https://arxiv.org/abs/2307.10894) | TPAMI |
| 2023 | [Human 3D Avatar Modeling with Implicit Neural Representation: A Brief Survey](https://arxiv.org/abs/2306.03576) | ArXiv 2023 |
| 2023 | [Human-Computer Interaction System: A Survey of Talking-Head Generation](https://www.mdpi.com/2079-9292/12/1/218) | IEEE |
| 2023 | [Talking human face generation: A survey](https://dl.acm.org/doi/10.1016/j.eswa.2023.119678) | ACM |
| 2022 | [Face Generation and Editing with StyleGAN: A Survey](https://arxiv.org/abs/2212.09102) | ArXiv 2022 |
| 2022 | [Deep Learning for Visual Speech Analysis: A Survey](https://arxiv.org/abs/2205.10839) | ArXiv 2022 |
| 2022 | [A Survey on Applications of Digital Human Avatars toward Virtual Co-presence](https://arxiv.org/abs/2201.04168) | ArXiv 2022 |
| 2021 | [A Review of 3D Face Reconstruction From a Single Image](https://arxiv.org/abs/2110.09299) | ArXiv 2021 |
| 2021 | [Deep Person Generation: A Survey from the Perspective of Face, Pose and Cloth Synthesis](https://arxiv.org/abs/2109.02081) | ArXiv 2021 |
| 2021 | [AudioVisual Speech Synthesis: A brief literature review](https://arxiv.org/abs/2103.03927) | ArXiv 2021 |
| 2020 | [What comprises a good talking-head video generation?: A Survey and Benchmark](https://arxiv.org/abs/2005.03201) | ArXiv 2020 |

---



## Funny Work

| Year | Title | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- |
| 2024 | [LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control](https://arxiv.org/abs/2407.03168) | [Code](https://github.com/KwaiVGI/LivePortrait) | [Project](https://liveportrait.github.io/) | 🔥快手 |
| 2024 | [From Audio to Photoreal Embodiment: Synthesizing Humans in Conversations](https://arxiv.org/abs/2401.01885.pdf) | [Code](https://github.com/facebookresearch/audio2photoreal/) | [Project](https://people.eecs.berkeley.edu/~evonne_ng/projects/audio2photoreal/#) | Photoreal |
| 2024 | [Animate Anyone: Consistent and Controllable Image-to-Video Synthesis for Character Animation](https://arxiv.org/abs/2311.17117.pdf) | [Code](https://github.com/HumanAIGC/AnimateAnyone) | [Project](https://humanaigc.github.io/animate-anyone/) | 🔥Animate (阿里科目三驱动) |
| 2024 | [What You See Is What You GAN: Rendering Every Pixel for High-Fidelity Geometry in 3D GANs](https://research.nvidia.com/labs/nxp/wysiwyg/media/WYSIWYG.pdf) |  | [Project](https://research.nvidia.com/labs/nxp/wysiwyg/) | 🔥Nvidia |

---



## Audio-driven

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580) | ArXiv 2026 |  |  | distillation, audio-driven, avatar, head avatar |
| 2026 | [SEDTalker: Emotion-Aware 3D Facial Animation Using Frame-Level Speech Emotion Diarization](https://arxiv.org/abs/2604.13335) | ArXiv 2026 | [Code](https://github.com/FarzanehJafari1987/SEDTalker) | [Project](https://farzanehjafari1987.github.io/SEDTalker.github.io) | audio-driven, 3D, emotion, facial animation |
| 2026 | [PrivFedTalk: Privacy-Aware Federated Diffusion with Identity-Stable Adapters for Personalized Talking-Head Generation](https://arxiv.org/abs/2604.08037) | ArXiv 2026 | [Code](https://github.com/mazumdarsoumya/PrivFedTalk) |  | federated learning, diffusion, privacy-aware, personalized talking head |
| 2026 | [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](https://arxiv.org/abs/2604.07786) | CVPR 2026 | [Code](https://github.com/ChanHyeok-Choi/C-MET) | [Project](https://chanhyeok-choi.github.io/C-MET) | emotion transfer, emotion editing, talking face, cross-modal |
| 2026 | [MMTalker: Multiresolution 3D Talking Head Synthesis with Multimodal Feature Fusion](https://arxiv.org/abs/2604.02941) | ArXiv 2026 |  |  | 3D, Audio-Driven, Multimodal Fusion, Mesh Parameterization |
| 2026 | [Realistic Lip Motion Generation Based on 3D Dynamic Viseme and Coarticulation Modeling for Human-Robot Interaction](https://arxiv.org/abs/2604.01756) | ArXiv 2026 | [Code](https://github.com/yuesheng21/Phoneme-to-Lip-14DOF) |  | lip sync, 3D viseme, coarticulation, humanoid robot, ARKit |
| 2026 | [EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332) | CVPR 2026 | [Code](https://github.com/jamesdemon923/EmoTaG) | [Project](https://emotag26.github.io/) | Gaussian Splatting, 3DGS, Audio-Driven, Emotion, Few-Shot |
| 2026 | [EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307) | ArXiv 2026 |  |  | Autoregressive, GPT-style, Talking Head |
| 2026 | [FreeTalk: Emotional Topology-Free 3D Talking Heads](https://arxiv.org/abs/2603.15512) | ArXiv 2026 |  |  | 3D Talking Heads, Emotional, Topology-Free |
| 2026 | [AvatarForcing: One-Step Streaming Talking Avatars via Local-Future Sliding-Window Denoising](https://arxiv.org/abs/2603.14331) | ArXiv 2026 | [Code](https://github.com/KlingAIResearch/AvatarForcing) | [Project](https://cuiliyuan121.github.io/AvatarForcing/) | Streaming Avatar, Real-Time, Diffusion |
| 2026 | [DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](https://arxiv.org/abs/2603.14267) | CVPR 2026 Findings | [Code](https://github.com/Fsoft-AIC/DiFlowDubber) | [Project](https://nngocson2002.github.io/projects/diflowdubber/) | Video Dubbing, Flow Matching, Cross-Modal |
| 2026 | [OmniEdit: A Training-free Framework for Lip Synchronization and Audio-Visual Editing](https://arxiv.org/abs/2603.09084) | ArXiv 2026 | [Code](https://github.com/l1346792580123/OmniEdit) |  | Lip Sync, Audio-Visual Editing, Training-Free |
| 2026 | [EmbedTalk: Triplane-Free Talking Head Synthesis using Embedding-Driven Gaussian Deformation](https://arxiv.org/abs/2603.07604) | Preprint |  |  | Gaussian Splatting, 3DGS, Audio-Driven, Talking Head |
| 2026 | [TempoSyncDiff: Distilled Temporally-Consistent Diffusion for Low-Latency Audio-Driven Talking Head Generation](https://arxiv.org/abs/2603.06057) | ArXiv 2026 | [Code](https://mazumdarsoumya.github.io/TempoSyncDiff) | [Project](https://mazumdarsoumya.github.io/TempoSyncDiff) | Diffusion, Audio-Driven, Talking Head, VAE, Latent |
| 2026 | [UniSync: Towards Generalizable and High-Fidelity Lip Synchronization for Challenging Scenarios](http://arxiv.org/abs/2603.03882) | ArXiv 2026 |  |  | Lip Sync, Pose-Anchored, Generalizable |
| 2026 | [UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418) | CVPR 2026 |  |  | Audio-Driven, Portrait Animation, Talking Head, CVPR, Transformer, Attention |
| 2026 | [FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159) | ArXiv 2026 |  |  | Audio-Driven, Portrait Animation, Reinforcement Learning, GRPO |
| 2026 | [Narrating For You: Prompt-guided Audio-visual Narrating Face Generation Employing Multi-entangled Latent Space](https://arxiv.org/abs/2602.18618) | WACV 2026 | [Code](https://github.com/narratingForYou/NarratingForYou) |  | Audio-Driven, WACV, Latent |
| 2026 | [VineetVC: Adaptive Video Conferencing Under Severe Bandwidth Constraints Using Audio-Driven Talking-Head Reconstruction](https://arxiv.org/abs/2602.12758) | ArXiv 2026 |  |  | audio-driven, video conferencing, talking head |
| 2026 | [DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160) | ArXiv 2026 | [Code](https://github.com/Guoxu1233/DreamID-Omni) | [Project](https://guoxu1233.github.io/DreamID-Omni/) | Audio-Driven, Transformer, Attention |
| 2026 | [3DXTalker: Unifying Identity, Lip Sync, Emotion, and Spatial Dynamics in Expressive 3D Talking Avatars](https://arxiv.org/abs/2602.10516) | ArXiv 2026 | [Code](https://github.com/EngineeringAI-LAB/3DXTalker) | [Project](https://engineeringai-lab.github.io/3DXTalker.github.io/) | 3D, Emotional, Lip Sync, Avatar, Talking Head, Transformer |
| 2026 | [AUHead: Realistic Emotional Talking Head Generation via Action Units Control](http://arxiv.org/abs/2602.09534) | ArXiv 2026 | [Code](https://github.com/laura990501/AUHead_ICLR) |  | Action Units, Audio-Driven Generation, Emotion Control, Diffusion Model |
| 2026 | [MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794) | ArXiv 2026 | [Code](https://github.com/OpenMOSS/MOVA) | [Project](https://mosi.cn/models/mova) | Audio-Driven |
| 2026 | [VedicTHG: Symbolic Vedic Computation for Low-Resource Talking-Head Generation in Educational Avatars](https://arxiv.org/abs/2602.08775) | ArXiv 2026 | [Code](https://vineetkumarrakesh.github.io/vedicthg) | [Project](https://vineetkumarrakesh.github.io/vedicthg) | Avatar, Talking Head |
| 2026 | [SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449) | ArXiv 2026 | [Code](https://github.com/Soul-AILab/SoulX-FlashHead) | [Project](https://soul-ailab.github.io/soulx-flashhead/) | Real-time, Streaming, Talking Head |
| 2026 | [Asymmetric Hierarchical Anchoring for Audio-Visual Joint Representation](https://arxiv.org/abs/2602.03570) | ArXiv 2026 |  |  | Audio-Driven |
| 2026 | [JoyAvatar: Unlocking Highly Expressive Avatars via Harmonized Text-Audio Conditioning](https://arxiv.org/abs/2602.00702) | ArXiv 2026 |  | [Project](https://joyavatar.github.io/) | Audio-Driven, Avatar |
| 2026 | [LPIPS-AttnWav2Lip: Generic Audio-Driven lip synchronization for Talking Head Generation in the Wild](https://arxiv.org/abs/2602.00189) | ArXiv 2026 | [Code](https://github.com/FelixChan9527/LPIPS-AttnWav2Lip) | [Project](https://github.com/FelixChan9527/LPIPS-AttnWav2Lip) | Lip Sync, Audio-Driven, Talking Head, Latent |
| 2026 | [MIRRORTALK: Forging Personalized Avatars Via Disentangled Style and Hierarchical Motion Control](http://arxiv.org/abs/2601.22501) | ICASSP 2026 |  |  | Personalized Avatars, Lip Sync, Style Disentanglement, Diffusion Model |
| 2026 | [JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](http://arxiv.org/abs/2601.22143) | ArXiv 2026 | [Code](https://github.com/justdubit/just-dub-it) | [Project](https://justdubit.github.io) | Audio-Visual Diffusion, LoRA, Lip Sync |
| 2026 | [EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127) | ArXiv 2026 |  | [Project](https://edit-yourself.github.io/) | Diffusion, Audio-Driven, Talking Head |
| 2026 | [Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation](https://arxiv.org/abs/2601.19112) | ICASSP 2026 | [Code](https://github.com/Mrask999/UA-3DTalk) | [Project](https://mrask999.github.io/UA-3DTalk) | 3D, Emotional, Talking Head, ICASSP, Attention |
| 2026 | [Audio-Driven Talking Face Generation with Blink Embedding and Hash Grid Landmarks Encoding](https://arxiv.org/abs/2601.18849) | ArXiv 2026 |  |  | Audio-Driven, Talking Head, Transformer |
| 2026 | [SkyReels-V3 Technique Report](http://arxiv.org/abs/2601.17323) | ArXiv 2026 | [Code](https://github.com/SkyworkAI/SkyReels-V3) |  | Video Generation, Audio-Guided, Talking Avatar, Diffusion Transformers |
| 2026 | [Exploring Talking Head Models With Adjacent Frame Prior for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2601.12876) | ACM Trans. Multimedia | [Code](https://github.com/liluoqaq/THFEM) | [Project](https://liluoqaq.github.io/THFEM-Supp) | Speech-Driven, Talking Head |
| 2026 | [Now You See Me, Now You Don't: A Unified Framework for Expression Consistent Anonymization in Talking Head Videos](https://arxiv.org/abs/2601.11635) | ArXiv 2026 |  |  | Talking Head |
| 2026 | [EditEmoTalk: Controllable Speech-Driven 3D Facial Animation with Continuous Expression Editing](https://arxiv.org/abs/2601.10000) | ArXiv 2026 |  |  | 3D, Speech-Driven |
| 2026 | [SingingBot: An Avatar-Driven System for Robotic Face Singing Performance](https://arxiv.org/abs/2601.02125) | ArXiv 2026 |  |  | robotic face, singing, avatar-driven, lip sync |
| 2026 | [ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847) | ArXiv 2026 |  |  | 3D, Gaussian Splatting, 3DGS, Emotional, Audio-Driven |
| 2026 | [DyStream: Streaming Dyadic Talking Heads Generation via Flow Matching-based Autoregressive Model](https://arxiv.org/abs/2512.24408) | ArXiv 2026 | [Code](https://github.com/RobinWitch/DyStream) | [Project](https://robinwitch.github.io/DyStream-Page) | Streaming, Talking Head, Flow Matching |
| 2026 | [SoulX-FlashTalk: Real-Time Infinite Streaming of Audio-Driven Avatars via Self-Correcting Bidirectional Distillation](https://arxiv.org/abs/2512.23379) | ArXiv 2026 | [Code](https://github.com/Soul-AILab/SoulX-FlashTalk) | [Project](https://soul-ailab.github.io/soulx-flashtalk/) | Real-time, Streaming, Audio-Driven, Avatar, Attention, VAE |
| 2026 | [SyncAnyone: Implicit Disentanglement via Progressive Self-Correction for Lip-Syncing in the wild](https://arxiv.org/abs/2512.21736) | ArXiv 2026 |  | [Project](https://humanaigc.github.io/sync_anyone_demo_page/) | Transformer |
| 2026 | [JoyAvatar-Flash: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion](https://arxiv.org/abs/2512.11423) | ArXiv 2026 |  | [Project](https://joystreamer.github.io) | Diffusion, Real-time, Audio-Driven, Avatar |
| 2026 | [REST: Diffusion-based Real-time End-to-end Streaming Talking Head Generation via ID-Context Caching and Asynchronous Streaming Distillation](https://arxiv.org/abs/2512.11229) | ArXiv 2026 |  |  | Diffusion, Real-time, Streaming, Talking Head, Latent |
| 2026 | [Lightning Fast Caching-based Parallel Denoising Prediction for Accelerating Talking Head Generation](https://arxiv.org/abs/2509.00052) | ArXiv 2026 |  |  | Talking Head, Attention, Latent |
| 2025 | [From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing](http://arxiv.org/abs/2512.25066) | ArXiv 2025 | [Code](https://github.com/KlingAIResearch/X-Dub) | [Project](https://hjrphoebus.github.io/X-Dub) | Visual dubbing, Diffusion Transformer, Self-bootstrapping, Lip sync |
| 2025 | [PTalker: Personalized Speech-Driven 3D Talking Head Animation via Style Disentanglement and Modality Alignment](https://arxiv.org/abs/2512.22602) | ArXiv 2025 |  |  | 3D, Speech-Driven, Talking Head, Attention |
| 2025 | [FlashLips: 100-FPS Mask-Free Latent Lip-Sync using Reconstruction Instead of Diffusion or GANs](https://arxiv.org/abs/2512.20033) | ArXiv 2025 |  |  | Diffusion, Transformer, GAN, Latent |
| 2025 | [In-Context Audio Control of Video Diffusion Transformers](https://arxiv.org/abs/2512.18772) | ArXiv 2025 |  |  | Diffusion, Audio-Driven, Transformer, Attention |
| 2025 | [Asynchronous Pipeline Parallelism for Real-Time Multilingual Lip Synchronization in Video Communication Systems](https://arxiv.org/abs/2512.18318) | IEEE Big Data 2025 |  |  | lip sync, real-time, multilingual |
| 2025 | [TalkVerse: Democratizing Minute-Long Audio-Driven Video Generation](https://arxiv.org/abs/2512.14938) | ArXiv 2025 | [Code](https://github.com/snap-research/TalkVerse) | [Project](https://zhenzhiwang.github.io/talkverse/) | Audio-Driven, VAE, Latent |
| 2025 | [VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image](https://arxiv.org/abs/2512.14677) | NeurIPS 2025 |  |  | 3D, Gaussian Splatting, Audio-Driven, Avatar |
| 2025 | [FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling](https://arxiv.org/abs/2512.14056) | ArXiv 2025 |  | [Project](https://facedit.github.io/) | Talking Head, Transformer, Attention, Flow Matching |
| 2025 | [JoVA: Unified Multimodal Learning for Joint Video-Audio Generation](https://arxiv.org/abs/2512.13677) | ArXiv 2025 | [Code](https://github.com/Visual-AI/JoVA) | [Project](https://visual-ai.github.io/jova) | Audio-Driven, Transformer, Attention, GAN |
| 2025 | [Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model](https://arxiv.org/abs/2512.13507) | Tech Report |  |  | Audio-Driven, Transformer, Reinforcement Learning |
| 2025 | [STARCaster: Spatio-Temporal AutoRegressive Video Diffusion for Identity- and View-Aware Talking Portraits](https://arxiv.org/abs/2512.13247) | ArXiv 2025 | [Code](https://github.com/foivospar/STARCaster) | [Project](https://foivospar.github.io/STARCaster/) | Diffusion, Portrait Animation, Talking Head |
| 2025 | [GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939) | WACV 2026 |  |  | 3D, Gaussian Splatting, 3DGS, Audio-Driven, Talking Head |
| 2025 | [UniLS: End-to-End Audio-Driven Avatars for Unified Listening and Speaking](https://arxiv.org/abs/2512.09327) | ArXiv 2025 | [Code](https://github.com/xg-chu/UniLS) |  | Audio-Driven, Avatar |
| 2025 | [Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length](https://arxiv.org/abs/2512.04677) | ArXiv 2025 | [Code](https://github.com/Alibaba-Quark/LiveAvatar) | [Project](https://liveavatar.github.io) | Real-time, Streaming, Audio-Driven, Avatar |
| 2025 | [EvalTalker: Learning to Evaluate Real-Portrait-Driven Multi-Subject Talking Humans](https://arxiv.org/abs/2512.01340) | ArXiv 2025 |  |  | Portrait Animation, Talking Head |
| 2025 | [AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement](https://arxiv.org/abs/2511.23475) | ArXiv 2025 | [Code](https://github.com/HKUST-C4G/AnyTalker) | [Project](https://hkust-c4g.github.io/AnyTalker-homepage) | Talking Head, Transformer, Attention |
| 2025 | [AI killed the video star. Audio-driven diffusion model for expressive talking head generation](https://arxiv.org/abs/2511.22488) | ArXiv 2025 |  |  | audio-driven, diffusion, talking head |
| 2025 | [IMTalker: Efficient Audio-driven Talking Face Generation with Implicit Motion Transfer](https://arxiv.org/abs/2511.22167) | ArXiv 2025 |  |  | Audio-Driven, Talking Head, Attention, Latent |
| 2025 | [Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy](https://arxiv.org/abs/2511.21579) | ArXiv 2025 |  |  | Audio-Driven, Attention, Latent |
| 2025 | [StreamingTalker: Audio-driven 3D Facial Animation with Autoregressive Diffusion Model](https://arxiv.org/abs/2511.14223) | ArXiv 2025 |  | [Project](https://zju3dv.github.io/StreamingTalker/) | 3D, Diffusion, Streaming, Audio-Driven |
| 2025 | [ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search](https://arxiv.org/abs/2511.06833) | AAAI 2026 |  |  | Diffusion, Talking Head, AAAI, Knowledge Distillation |
| 2025 | [Shared Latent Representation for Joint Text-to-Audio-Visual Synthesis](https://arxiv.org/abs/2511.05432) | ArXiv 2025 |  |  | Audio-Driven, Latent |
| 2025 | [UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions](https://arxiv.org/abs/2511.03334) | ArXiv 2025 |  |  | Audio-Driven, Transformer, Attention, Latent |
| 2025 | [See the Speaker: Crafting High-Resolution Talking Faces from Speech with Prior Guidance and Region Refinement](http://arxiv.org/abs/2510.26819) | TASLP 2025 |  |  | High-Resolution, Talking Faces, Speech-to-Face, Diffusion |
| 2025 | [Learning Disentangled Speech- and Expression-Driven Blendshapes for 3D Talking Face Animation](http://arxiv.org/abs/2510.25234) | ICXR 2025 |  |  | Blendshapes, FLAME, Disentanglement, 3D Animation |
| 2025 | [Awakening Facial Emotional Expressions in Human-Robot](https://arxiv.org/abs/2510.23059) | IROS 2025 |  |  | humanoid robot, facial expression generation, emotion, social robot |
| 2025 | [MAGIC-Talk: Motion-aware Audio-Driven Talking Face Generation with Customizable Identity Control](https://arxiv.org/abs/2510.22810) | ArXiv 2025 |  |  |  |
| 2025 | [LSF-Animation: Label-Free Speech-Driven Facial Animation via Implicit Feature Representation](http://arxiv.org/abs/2510.21864) | SIGGRAPH Asia 2025 | [Code](https://github.com/Dogter521/LSF-Animation) |  | Label-Free, Speech-Driven, Facial Animation, FLAME |
| 2025 | [Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback](https://arxiv.org/abs/2510.12089) | ArXiv 2025 |  |  | Diffusion, Audio-Driven, AAAI, Transformer |
| 2025 | [DEMO: Disentangled Motion Latent Flow Matching for Fine-Grained Controllable Talking Portrait Synthesis](http://arxiv.org/abs/2510.10650) | ArXiv 2025 |  |  | Disentangled Motion, Flow Matching, Talking Portrait, Controllable |
| 2025 | [SyncLipMAE: Contrastive Masked Pretraining for Audio-Visual Talking-Face Representation](http://arxiv.org/abs/2510.10069) | ArXiv 2025 |  |  | Contrastive Masked Pretraining, Audio-Visual, Talking-Face |
| 2025 | [EGSTalker: Real-Time Audio-Driven Talking Head Generation with Efficient Gaussian Deformation](http://arxiv.org/abs/2510.08587) | IEEE SMC 2025 |  |  | Real-Time, Audio-Driven, Gaussian Deformation, Talking Head |
| 2025 | [A Bridge from Audio to Video: Phoneme-Viseme Alignment Allows Every Face to Speak Multiple Languages](http://arxiv.org/abs/2510.06612) | ArXiv 2025 |  |  | Phoneme-Viseme Alignment, Multilingual TFS, Mixture-of-Experts |
| 2025 | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](http://arxiv.org/abs/2510.02617) | ArXiv 2025 | [Code](https://github.com/Beijia11/IASA) | [Project](https://beijia11.github.io/IASA) | Diffusion models, co-speech video, real-time, sparse attention |
| 2025 | [Audio Driven Real-Time Facial Animation for Social Telepresence](https://arxiv.org/abs/2510.01176) | SIGGRAPH Asia 2025 |  | [Project](https://jiyewise.github.io/projects/AudioRTA) | Real-time, Audio-Driven, SIGGRAPH, Transformer, Latent |
| 2025 | [StableDub: Taming Diffusion Prior for Generalized and Efficient Visual Dubbing](http://arxiv.org/abs/2509.21887) | ArXiv 2025 |  | [Project](https://stabledub.github.io) | Visual Dubbing, Diffusion, Mamba-Transformer |
| 2025 | [KSDiff: Keyframe-Augmented Speech-Aware Dual-Path Diffusion for Facial Animation](http://arxiv.org/abs/2509.20128) | ArXiv 2025 |  |  | Keyframe, Diffusion, Dual-Path, Facial Animation |
| 2025 | [SynchroRaMa: Lip-Synchronized and Emotion-Aware Talking Face Generation via Multi-Modal Emotion Embedding](http://arxiv.org/abs/2509.19965) | WACV 2026 | [Code](https://github.com/novicemm/synchrorama_) | [Project](https://novicemm.github.io/synchrorama) | Multi-Modal, Emotion-Aware, LLM |
| 2025 | [Talking Head Generation via AU-Guided Landmark Prediction](http://arxiv.org/abs/2509.19749) | ArXiv 2025 |  |  | Action Units, Landmark Prediction, Diffusion |
| 2025 | [PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control](http://arxiv.org/abs/2509.16922) | ICONIP 2025 |  |  | 3DGS, Real-Time, Pixel-Aware, Audio-Driven |
| 2025 | [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](https://arxiv.org/abs/2509.12831) | ArXiv 2025 |  |  | lip sync, voice cloning |
| 2025 | [Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis](http://arxiv.org/abs/2509.09595) | ArXiv 2025 |  | [Project](https://klingavatar.github.io) | Multimodal Instructions, Avatar Synthesis, Lip Synchronization |
| 2025 | [Think2Sing: Orchestrating Structured Motion Subtitles for Singing-Driven 3D Head Animation](http://arxiv.org/abs/2509.02278) | ArXiv 2025 |  |  | Singing-Driven, 3D Head, Diffusion |
| 2025 | [EmoCAST: Emotional Talking Portrait via Emotive Text Description](https://arxiv.org/abs/2508.20615) | ArXiv 2025 | [Code](https://github.com/GVCLab/EmoCAST) | [Project](https://github.com/GVCLab/EmoCAST) | Emotional, Portrait Animation, Talking Head, Attention |
| 2025 | [Wan-S2V: Audio-Driven Cinematic Video Generation](http://arxiv.org/abs/2508.18621) | ArXiv 2025 |  |  | Cinematic, Audio-Driven, Video Generation |
| 2025 | [Warm Chat: Diffuse Emotion-aware Interactive Talking Head Avatar with Tree-Structured Guidance](https://arxiv.org/abs/2508.18337) | ArXiv 2025 (Withdrawn) |  |  | Emotional, Avatar, Talking Head, Transformer, Latent |
| 2025 | [Audio2Face-3D: Audio-driven Realistic Facial Animation For Digital Avatars](https://arxiv.org/abs/2508.16401) | ArXiv 2025 |  |  | Audio-driven Realistic Facial Animation, Digital Avatars |
| 2025 | [D^3-Talker: Dual-Branch Decoupled Deformation Fields for Few-Shot 3D Talking Head Synthesis](http://arxiv.org/abs/2508.14449) | ECAI 2025 |  |  | Few-Shot, 3DGS, Deformation Fields |
| 2025 | [InfiniteTalk: Audio-driven Video Generation for Sparse-Frame Video Dubbing](http://arxiv.org/abs/2508.14033) | ArXiv 2025 |  |  | Sparse-Frame Dubbing, Full-Body |
| 2025 | [CEM-Net: Cross-Emotion Memory Network for Emotional Talking Face Generation](http://arxiv.org/abs/2508.12368) | ArXiv 2025 |  |  | Cross-emotion memory, audio emotion enhancement, expression displacement, lip sync |
| 2025 | [RealTalk: Realistic Emotion-Aware Lifelike Talking-Head Synthesis](http://arxiv.org/abs/2508.12163) | ICCV 2025 Workshop |  |  | Emotion, NeRF, VAE |
| 2025 | [FantasyTalking2: Timestep-Layer Adaptive Preference Optimization for Audio-Driven Portrait Animation](http://arxiv.org/abs/2508.11255) | ArXiv 2025 | [Code](https://github.com/Fantasy-AMAP/fantasy-talking2) | [Project](https://fantasy-amap.github.io/fantasy-talking2/) | Audio-Driven, Portrait Animation, Preference Optimization |
| 2025 | [HM-Talker: Hybrid Motion Modeling for High-Fidelity Talking Head Synthesis](http://arxiv.org/abs/2508.10566) | ArXiv 2025 |  |  | Hybrid Motion, High-Fidelity, Talking Head |
| 2025 | [StableAvatar: Infinite-Length Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2508.08248) | ArXiv 2025 | [Code](https://github.com/Francis-Rings/StableAvatar) | [Project](https://francis-rings.github.io/StableAvatar/) | Stable Diffusion |
| 2025 | [DiTalker: A Unified DiT-based Framework for High-Quality and Speaking Styles Controllable Portrait Animation](http://arxiv.org/abs/2508.06511) | ArXiv 2025 |  | [Project](https://thenameishope.github.io/DiTalker/) | DiT, Portrait Animation, Speaking Styles |
| 2025 | [READ: Real-time and Efficient Asynchronous Diffusion for Audio-driven Talking Head Generation](https://arxiv.org/abs/2508.03457) | ArXiv 2025 |  | [Project](https://readportrait.github.io/READ/) | Diffusion, Real-time, Audio-Driven, Talking Head, Transformer, VAE |
| 2025 | [X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio](http://arxiv.org/abs/2508.02944) | ArXiv 2025 |  | [Project](https://byteaigc.github.io/X-Actor/) | Emotional Portrait, Long-range, Audio-driven |
| 2025 | [SpA2V: Harnessing Spatial Auditory Cues for Audio-driven Spatially-aware Video Generation](http://arxiv.org/abs/2508.00782) | ACM MM 2025 |  |  | Spatial Audio, Video Generation, MLLM |
| 2025 | [Mask-Free Audio-driven Talking Face Generation for Enhanced Visual Quality and Identity Preservation](http://arxiv.org/abs/2507.20953) | ArXiv 2025 |  |  | Mask-Free, Identity Preservation, Audio-driven |
| 2025 | [Learning Phonetic Context-Dependent Viseme for Enhancing Speech-Driven 3D Facial Animation](http://arxiv.org/abs/2507.20568) | Interspeech 2025 | [Code](https://github.com/kimhyungkyu-1208/interspeech25) | [Project](https://cau-irislab.github.io/interspeech25) | Phonetic Context, Viseme, 3D Facial Animation |
| 2025 | [MemoryTalker: Personalized Speech-Driven 3D Facial Animation via Audio-Guided Stylization](http://arxiv.org/abs/2507.20562) | ICCV 2025 | [Code](https://github.com/kimhyungkyu-1208/MemoryTalker) | [Project](https://cau-irislab.github.io/ICCV25-MemoryTalker/) | Personalized, 3D Facial Animation, Memory |
| 2025 | [JOLT3D: Joint Learning of Talking Heads and 3DMM Parameters with Application to Lip-Sync](https://arxiv.org/abs/2507.20452) | ArXiv 2025 |  |  | 3DMM, Joint Learning, Talking Head |
| 2025 | [Livatar-1: Real-Time Talking Heads Generation with Tailored Flow Matching](http://arxiv.org/abs/2507.18649) | Technical Report |  | [Project](https://www.hedra.com/) | real-time, flow matching, lip-sync |
| 2025 | [ATL-Diff: Audio-Driven Talking Head Generation with Early Landmarks-Guide Noise Diffusion](http://arxiv.org/abs/2507.12804) | ArXiv 2025 | [Code](https://github.com/sonvth/ATL-Diff) |  | Diffusion, Landmarks-Guide, Real-time, Identity Preservation |
| 2025 | [MOSPA: Human Motion Generation Driven by Spatial Audio](http://arxiv.org/abs/2507.11949) | NeurIPS 2025 | [Code](https://github.com/xsy27/Mospa-Acoustic-driven-Motion-Generation) |  | Spatial Audio, Human Motion Generation, Virtual Human |
| 2025 | [M2DAO-Talker: Harmonizing Multi-granular Motion Decoupling and Alternating Optimization for Talking-head Generation](http://arxiv.org/abs/2507.08307) | ArXiv 2025 |  | [Project](https://m2dao-talker.github.io/M2DAO-Talk.github.io) | Multi-granular Motion, Decoupling, Optimization |
| 2025 | [MEDTalk: Multimodal Controlled 3D Facial Animation with Dynamic Emotions by Disentangled Embedding](http://arxiv.org/abs/2507.06071) | ArXiv 2025 | [Code](https://github.com/SJTU-Lucy/MEDTalk) |  | Multimodal, 3D Facial Animation, Dynamic Emotions |
| 2025 | [MoDiT: Learning Highly Consistent 3D Motion Coefficients with Diffusion Transformer for Talking Head Generation](http://arxiv.org/abs/2507.05092) | ArXiv 2025 |  |  | 3DMM, Diffusion Transformer, Temporal Consistency, Blinking Dynamics |
| 2025 | [MoDA: Multi-modal Diffusion Architecture for Talking Head Generation](http://arxiv.org/abs/2507.03256) | ArXiv 2025 | [Code](https://github.com/lixinyyang/MoDA) | [Project](https://lixinyyang.github.io/MoDA.github.io/) | Multi-modal, Diffusion, Talking Head Generation |
| 2025 | [FixTalk: Taming Identity Leakage for High-Quality Talking Head Generation in Extreme Cases](http://arxiv.org/abs/2507.01390) | ArXiv 2025 |  |  | Identity Leakage, Extreme Cases |
| 2025 | [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](http://arxiv.org/abs/2506.23552) | ArXiv 2025 |  |  | Flow Matching, Audio-Motion |
| 2025 | [Few-Shot Identity Adaptation for 3D Talking Heads via Global Gaussian Field](http://arxiv.org/abs/2506.22044) | ArXiv 2025 | [Code](https://github.com/gme-hong/FIAG) |  | Few-Shot, Global Gaussian Field, 3DGS |
| 2025 | [GGTalker: Talking Head Synthesis with Generalizable Gaussian Priors and Identity-Specific Adaptation](http://arxiv.org/abs/2506.21513) | ICCV 2025 | [Code](https://github.com/vincenthu19/GGTalker) | [Project](https://vincenthu19.github.io/GGTalker/) | 3D Talking Head, Gaussian Priors, Identity Adaptation |
| 2025 | [SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](http://arxiv.org/abs/2506.14742) | ArXiv 2025 | [Code](https://github.com/ziqiaopeng/SyncTalk) | [Project](https://ziqiaopeng.github.io/synctalk++) | 3DGS, Synchronization |
| 2025 | [LLIA -- Enabling Low-Latency Interactive Avatars: Real-Time Audio-Driven Portrait Video Generation with Diffusion Models](http://arxiv.org/abs/2506.05806) | ArXiv 2025 |  |  | Low-Latency, Real-Time, Interactive |
| 2025 | [TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models](http://arxiv.org/abs/2506.03099) | ArXiv 2025 | [Code](https://github.com/aaxwaz/TalkingMachines) | [Project](https://aaxwaz.github.io/TalkingMachines) | Real-Time, Autoregressive Diffusion |
| 2025 | [SkyReels-Audio: Omni Audio-Conditioned Talking Portraits in Video Diffusion Transformers](https://arxiv.org/abs/2506.00830) | ArXiv 2025 |  |  | video diffusion transformer, multimodal, talking portrait, audio-conditioned |
| 2025 | [Video Editing for Audio-Visual Dubbing](http://arxiv.org/abs/2505.23406) | ArXiv 2025 |  |  | Video Editing, Dubbing |
| 2025 | [Wav2Sem: Plug-and-Play Audio Semantic Decoupling for 3D Speech-Driven Facial Animation](http://arxiv.org/abs/2505.23290) | CVPR 2025 | [Code](https://github.com/wslh852/Wav2Sem.git) |  | 3D, Semantic Decoupling |
| 2025 | [MMGT: Motion Mask Guided Two-Stage Network for Co-Speech Gesture Video Generation](http://arxiv.org/abs/2505.23120) | ArXiv 2025 | [Code](https://github.com/SIA-IDE/MMGT) |  | Co-Speech Gesture, Two-Stage |
| 2025 | [FaceEditTalker: Interactive Talking Head Generation with Facial Attribute Editing](http://arxiv.org/abs/2505.22141) | ArXiv 2025 |  | [Project](https://peterfanfan.github.io/FaceEditTalker) | Attribute Editing, Interactive |
| 2025 | [OmniSync: Towards Universal Lip Synchronization via Diffusion Transformers](https://arxiv.org/abs/2505.21448) | ArXiv 2025 |  |  | Lip Sync, Universal, Visual Prosody |
| 2025 | [OT-Talk: Animating 3D Talking Head with Optimal Transportation](http://arxiv.org/abs/2505.01932) | ArXiv 2025 |  |  | FLAME, 3D |
| 2025 | [GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](http://arxiv.org/abs/2505.01928) | CVPRW 2025 |  |  | 3DGS |
| 2025 | [Model See Model Do: Speech-Driven Facial Animation with Style Control](http://arxiv.org/abs/2505.01319) | SIGGRAPH 2025 |  |  |  |
| 2025 | [KeySync: A Robust Approach for Leakage-free Lip Synchronization in High Resolution](http://arxiv.org/abs/2505.00497) | ArXiv 2025 | [Code](https://github.com/antonibigata/keysync) | [Project](https://antonibigata.github.io/KeySync) |  |
| 2025 | [IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](http://arxiv.org/abs/2504.19165) | CVPR 2025 |  | [Project](https://y-u-a-n-l-i.github.io/projects/IM-Portrait) | 3D-aware, Video Diffusion |
| 2025 | [Audio-Driven Talking Face Video Generation with Joint Uncertainty Learning](http://arxiv.org/abs/2504.18810) | ArXiv 2025 |  |  | Joint uncertainty learning, Audio-driven talking face, Lip sync, Visual uncertainty |
| 2025 | [DICE-Talk: Disentangle Identity, Cooperate Emotion: Correlation-Aware Emotional Talking Portrait Generation](http://arxiv.org/abs/2504.18087) | ACM MM 2025 |  |  | Emotional Portrait, Identity Preservation, Emotion Cooperation |
| 2025 | [ExFace: Expressive Facial Control for Humanoid Robots with Diffusion Transformers and Bootstrap Training](https://arxiv.org/abs/2504.14477) | ArXiv 2025 |  |  | diffusion transformer, humanoid robot, facial control, blendshape |
| 2025 | [PASE: Phoneme-Aware Speech Encoder to Improve Lip Sync Accuracy for Talking Head Synthesis](https://arxiv.org/abs/2504.05803) | ArXiv 2025 |  |  | Lip Sync, Phoneme-Aware, Speech Encoder |
| 2025 | [Exploiting Temporal Audio-Visual Correlation Embedding for Audio-Driven One-Shot Talking Head Animation](http://arxiv.org/abs/2504.05746) | TMM 2025 |  |  | Talking Head Animation, Temporal Correlation, One-Shot |
| 2025 | [FantasyTalking: Realistic Talking Portrait Generation via Coherent Motion Synthesis](https://arxiv.org/abs/2504.04842) | ArXiv 2025 | [Code](https://github.com/Fantasy-AMAP/fantasy-talking) | [Project](https://fantasy-amap.github.io/fantasy-talking) | talking portrait, motion synthesis, video diffusion, audio-visual alignment |
| 2025 | [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](http://arxiv.org/abs/2504.02542) | ArXiv 2025 | [Code](https://github.com/harlanhong/ACTalker) | [Project](https://harlanhong.github.io/publications/actalker/index.html) |  |
| 2025 | [MGGTalk：Monocular and Generalizable Gaussian Talking Head Animation](http://arxiv.org/abs/2504.00665) | CVPR 2025 |  |  | One Shot, 3DGS |
| 2025 | [STSA: Spatial-Temporal Semantic Alignment for Visual Dubbing](http://arxiv.org/abs/2503.23039) | ICME 2025 | [Code](https://github.com/SCAILab-USTC/STSA) |  | Spatial-Temporal Alignment, Semantic Features, Visual Dubbing, Stability |
| 2025 | [Dual Audio-Centric Modality Coupling for Talking Head Generation](http://arxiv.org/abs/2503.22728) | ArXiv 2025 |  |  | NeRF |
| 2025 | [Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis](http://arxiv.org/abs/2503.22605) | ArXiv 2025 |  | [Project](https://sstzal.github.io/Audio-Plane/) | 3DGS |
| 2025 | [Audio-driven Gesture Generation via Deviation Feature in the Latent Space](http://arxiv.org/abs/2503.21616) | ArXiv 2025 |  |  | Gesture |
| 2025 | [Perceptually Accurate 3D Talking Head Generation: New Definitions, Speech-Mesh Representation, and Evaluation Metrics](http://arxiv.org/abs/2503.20308) | CVPR 2025 | [Code](https://github.com/kaist-ami/Perceptual-3D-Talking-Head) | [Project](https://perceptual-3d-talking-head.github.io) |  |
| 2025 | [AudCast: Audio-Driven Human Video Generation by Cascaded Diffusion Transformers](http://arxiv.org/abs/2503.19824) | CVPR 2025 |  | [Project](https://guanjz20.github.io/projects/AudCast) | DiT |
| 2025 | [EmoHead: Emotional Talking Head via Manipulating Semantic Expression Parameters](http://arxiv.org/abs/2503.19416) | ArXiv 2025 |  |  | Neural Radiance Fields, Expression Parameters, Emotion Control, Audio-Driven |
| 2025 | [DisentTalk: Cross-lingual Talking Face Generation via Semantic Disentangled Diffusion Model](http://arxiv.org/abs/2503.19001) | ICME 2025 |  | [Project](https://kangweiiliu.github.io/DisentTalk) |  |
| 2025 | [Teller: Real-Time Streaming Audio-Driven Portrait Animation with Autoregressive Motion Generation](http://arxiv.org/abs/2503.18429) | CVPR 2025 |  |  | Autoregressive |
| 2025 | [DiffusionTalker: Efficient and Compact Speech-Driven 3D Talking Head via Personalizer-Guided Distillation](http://arxiv.org/abs/2503.18159) | ICME 2025 | [Code](https://github.com/ChenVoid/DiffusionTalker) |  | Diffusion, 3D |
| 2025 | [Unlock Pose Diversity: Accurate and Efficient Implicit Keypoint-based Spatiotemporal Diffusion for Audio-driven Talking Portrait](http://arxiv.org/abs/2503.12963) | ArXiv 2025 | [Code](https://github.com/chaolongy/KDTalker) |  | implicit keypoint, spatiotemporal diffusion, audio-driven, talking portrait |
| 2025 | [StyleSpeaker: Audio-Enhanced Fine-Grained Style Modeling for Speech-Driven 3D Facial Animation](http://arxiv.org/abs/2503.09852) | ArXiv 2025 |  |  | 3D |
| 2025 | [MagicInfinite: Generating Infinite Talking Videos with Your Words and Voice](https://arxiv.org/abs/2503.05978) | ArXiv 2025 |  | [Project](https://magicinfinite.github.io) |  |
| 2025 | [FREAK: Frequency-modulated High-fidelity and Real-time Audio-driven Talking Portrait Synthesis](http://arxiv.org/abs/2503.04067) | ICMR 2025 |  |  |  |
| 2025 | [KeyFace: Expressive Audio-Driven Facial Animation for Long Sequences via KeyFrame Interpolation](http://arxiv.org/abs/2503.01715) | CVPR 2025 |  |  | Diffusion, Long Sequences |
| 2025 | [Towards High-fidelity 3D Talking Avatar with Personalized Dynamic Texture](http://arxiv.org/abs/2503.00495) | CVPR 2025 | [Code](https://github.com/XuanchenLi/TexTalk) | [Project](https://xuanchenli.github.io/TexTalk) | Texture |
| 2025 | [InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387) | CVPR 2025 | [Code](https://github.com/Fictionarry/InsTaG) | [Project](https://fictionarry.github.io/InsTaG) | Few Shot, 3DGS |
| 2025 | [ARTalk: Speech-Driven 3D Head Animation via Autoregressive Model](http://arxiv.org/abs/2502.20323) | SIGGRAPH Asia | [Code](https://github.com/xg-chu/ARTalk) | [Project](https://xg-chu.site/project_artalk) | Autoregressive, FLAME, 3D |
| 2025 | [FLAP: Fully-controllable Audio-driven Portrait Video Generation through 3D head conditioned diffusion model](http://arxiv.org/abs/2502.19455) | ArXiv 2025 |  |  | Diffusion |
| 2025 | [Dimitra: Audio-driven Diffusion model for Expressive Talking Head Generation](http://arxiv.org/abs/2502.17198) | ArXiv 2025 |  |  | Audio-driven, Diffusion model, Motion Diffusion Transformer, Lip sync |
| 2025 | [NeRF-3DTalker: Neural Radiance Field with 3D Prior Aided Audio Disentanglement for Talking Head Synthesis](https://arxiv.org/abs/2502.14178) | ICASSP 2025 | [Code](https://github.com/NeRF-3DTalker/NeRF-3DTalker-code) | [Project](https://nerf-3dtalker.github.io/NeRF-3Dtalker) |  |
| 2025 | [Emotional Face-to-Speech](http://arxiv.org/abs/2502.01046) | ArXiv 2025 |  | [Project](https://demoface-ai.github.io) | emotion, face2speech |
| 2025 | [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](http://arxiv.org/abs/2502.00654) | ArXiv 2025 |  |  | emotion, 3DGS |
| 2025 | [Identity-Preserving Video Dubbing Using Motion Warping](https://arxiv.org/abs/2501.04586) | ArXiv 2025 |  |  | Video Dubbing |
| 2025 | [MoEE: Mixture of Emotion Experts for Audio-Driven Portrait Animation](http://arxiv.org/abs/2501.01808) | ArXiv 2025 |  |  | Audio-driven, Emotion Synthesis, Mixture of Experts, Portrait Animation |
| 2025 | [DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](http://arxiv.org/abs/2412.20148) | ICASSP 2025 | [Code](https://github.com/CVI-SZU/DEGSTalk) |  | Hair-Preserving |
| 2025 | [UniAvatar: Taming Lifelike Audio-Driven Talking Head Generation with Comprehensive Motion and Lighting Control](http://arxiv.org/abs/2412.19860) | ArXiv 2025 |  |  | SD, Lighting control |
| 2025 | [FADA: Fast Diffusion Avatar Synthesis with Mixed-Supervised Multi-CFG Distillation](http://arxiv.org/abs/2412.16915) | CVPR 2025 |  | [Project](https://fadavatar.github.io) | Fast Diffusion 12.5X speedup |
| 2025 | [Synergizing Motion and Appearance: Multi-Scale Compensatory Codebooks for Talking Head Video Generation](http://arxiv.org/abs/2412.00719) | CVPR 2025 | [Code](https://github.com/ShaelynZ/synergize-motion-appearance) | [Project](https://shaelynz.github.io/synergize-motion-appearance) |  |
| 2025 | [V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow](http://arxiv.org/abs/2411.19486) | ICASSP 2025 | [Code](https://github.com/kaistmm/V2SFlow) |  | Video-to-Speech, Speech Decomposition |
| 2025 | [Sonic: Shifting Focus to Global Audio Perception in Portrait Animation](http://arxiv.org/abs/2411.16331) | CVPR 2025 | [Code](https://github.com/jixiaozhong/Sonic) | [Project](https://jixiaozhong.github.io/Sonic/) | Global Audio Perception, Portrait Animation |
| 2025 | [MuseTalk: Real-Time High-Fidelity Video Dubbing via Spatio-Temporal Sampling](http://arxiv.org/abs/2410.10122) | ArXiv 2025 | [Code](https://github.com/TMElyralab/MuseTalk) |  |  |
| 2025 | [Lipschitz-Driven Noise Robustness in VQ-AE for High-Frequency Texture Repair in ID-Specific Talking Heads](http://arxiv.org/abs/2410.00990) | ArXiv 2025 |  |  | Noise Robustness, VQ-AE, High-Frequency |
| 2025 | [Loopy: Taming Audio-Driven Portrait Avatar with Long-Term Motion Dependency](http://arxiv.org/abs/2409.02634) | ICLR 2025 |  | [Project](https://loopyavatar.github.io) |  |
| 2025 | [EmoFace: Emotion-Content Disentangled Speech-Driven 3D Talking Face Animation](http://arxiv.org/abs/2408.11518) | ArXiv 2025 |  |  | emotion，3D |
| 2025 | [DGTalker: Disentangled Generative Latent Space Learning for Audio-Driven Gaussian Talking Heads](https://openaccess.thecvf.com/content/ICCV2025/papers/Liang_DGTalker_Disentangled_Generative_Latent_Space_Learning_for_Audio-Driven_Gaussian_Talking_ICCV_2025_paper.pdf) | ICCV 2025 |  | [Project](https://shawks0419.github.io/dgtalker/) | Gaussian, Latent Space |
| 2025 | [Talking Head Generation via Viewpoint and Lighting Simulation Based on Global Representation](https://dl.acm.org/doi/pdf/10.1145/3746027.3755503) | ACM MM 2025 |  |  | Depth-based |
| 2025 | [PESTalk: Speech-Driven 3D Facial Animation with Personalized Emotional Styles](https://dl.acm.org/doi/abs/10.1145/3746027.3755190) | ACM MM 2025 |  |  | FLAME |
| 2025 | [DisenEmo: Learning disentangled emotional representation from facial motion for 3D talking head generation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11084454) | ICIP 2025 |  |  | Disentangled Emotional Representation, 3D Talking Head Generation |
| 2025 | [ExpTalk: Diverse Emotional Expression via Adaptive Disentanglement and Refined Alignment for Speech-Driven 3D Facial Animation](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7737.pdf) | IJCAI 2025 |  |  | Adaptive Disentanglement, Refined Alignment, 3D Facial Animation |
| 2025 | [SyncGaussian: Stable 3D Gaussian-Based Talking Head Generation with Enhanced Lip Sync via Discriminative Speech Feature](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/850.pdf) | IJCAI 2025 |  |  | Stable 3D Gaussian-Based Talking Head Generation, Enhanced Lip Sync, Discriminative Speech Feature |
| 2025 | [SyncAnimation: A Real-Time End-to-End Framework for Audio-Driven Human Pose and Talking Head Animation](https://syncanimation.github.io/) | ArXiv 2025 |  |  | Huaman Pose |
| 2025 | [JoyGen: Audio-Driven 3D Depth-Aware Talking-Face Video Editing](https://arxiv.org/bas/2501.01798) | ArXiv 2025 |  |  | Depth, JD work |
| 2024 | [VQTalker: Towards Multilingual Talking Avatars through Facial Motion Tokenization](http://arxiv.org/abs/2412.09892) | ArXiv 2024 | [Code](https://github.com/X-LANCE/VQTalker) | [Project](https://x-lance.github.io/VQTalker) | visemes, code book |
| 2024 | [LatentSync: Audio Conditioned Latent Diffusion Models for Lip Sync](http://arxiv.org/abs/2412.09262) | ArXiv 2024 |  |  | Diffusion, SyncNet |
| 2024 | [PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](http://arxiv.org/abs/2412.08504) | AAAI 2025 |  |  | Point Cloud, Gaussian Splatting |
| 2024 | [PortraitTalk: Towards Customizable One-Shot Audio-to-Talking Face Generation](http://arxiv.org/abs/2412.07754) | ArXiv 2024 |  |  | Diffusion, Attention, One-Shot |
| 2024 | [MEMO: Memory-Guided Diffusion for Expressive Talking Video Generation](http://arxiv.org/abs/2412.04448) | ArXiv 2024 | [Code](https://github.com/memoavatar/memo) | [Project](https://memoavatar.github.io) | Memory |
| 2024 | [IF-MDM: Implicit Face Motion Diffusion Model for High-Fidelity Realtime Talking Head Generation](http://arxiv.org/abs/2412.04000) | ArXiv 2024 |  |  | Motion Diffusion Model |
| 2024 | [FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait](http://arxiv.org/abs/2412.01064) | ICCV 2025 | [Code](https://github.com/deepbrainai-research/float) | [Project](https://deepbrainai-research.github.io/float/) | Flow Matching |
| 2024 | [LokiTalk: Learning Fine-Grained and Generalizable Correspondences to Enhance NeRF-based Talking Head Synthesis](http://arxiv.org/abs/2411.19525) | ArXiv 2024 |  | [Project](https://digital-avatar.github.io/ai/LokiTalk) | NeRF |
| 2024 | [Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis](http://arxiv.org/abs/2411.19509) | ArXiv 2024 | [Code](https://github.com/antgroup/ditto-talkinghead) | [Project](https://digital-avatar.github.io/ai/Ditto) | Diffusion |
| 2024 | [GaussianSpeech: Audio-Driven Gaussian Avatars](http://arxiv.org/abs/2411.18675) | ArXiv 2024 | [Code](https://github.com/shivangi-aneja/GaussianSpeech) | [Project](https://shivangi-aneja.github.io/projects/gaussianspeech) | 3DGS, 3D |
| 2024 | [LetsTalk: Latent Diffusion Transformer for Talking Video Synthesis](http://arxiv.org/abs/2411.16748) | ArXiv 2024 |  |  |  |
| 2024 | [EmotiveTalk: Expressive Talking Head Generation through Audio Information Decoupling and Emotional Video Diffusion](http://arxiv.org/abs/2411.16726) | CVPR 2025 |  | [Project](https://emotivetalk.github.io) | Emotion, Expressive, Diffusion |
| 2024 | [Comparative Analysis of Audio Feature Extraction for Real-Time Talking Portrait Synthesis](http://arxiv.org/abs/2411.13209) | ArXiv 2024 |  |  | Audio Feature Extraction, Whisper, Real-time processing, Talking portrait synthesis |
| 2024 | [LES-Talker: Fine-Grained Emotion Editing for Talking Head Generation in Linear Emotion Space](http://arxiv.org/abs/2411.09268) | ArXiv 2024 |  |  | Fine-Grained Emotion |
| 2024 | [JoyVASA: Portrait and Animal Image Animation with Diffusion-Based Audio-Driven Facial Dynamics and Head Motion Generation](http://arxiv.org/abs/2411.09209) | ArXiv 2024 | [Code](https://github.com/jdh-algo/JoyVASA) |  | Diffusion, VASA |
| 2024 | [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](http://arxiv.org/abs/2410.23836) | ArXiv 2024 |  |  |  |
| 2024 | [Audio-Driven Emotional 3D Talking-Head Generation](http://arxiv.org/abs/2410.17262) | ArXiv 2024 |  |  | Emotion |
| 2024 | [Takin-ADA: Emotion Controllable Audio-Driven Animation with Canonical and Landmark Loss Optimization](http://arxiv.org/abs/2410.14283) | ArXiv 2024 |  |  |  |
| 2024 | [DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking Head Video Generation](http://arxiv.org/abs/2410.13726) | ArXiv 2024 | [Code](https://github.com/Hanbo-Cheng/DAWN-pytorch) |  | Non-autoregressive Diffusion |
| 2024 | [Hallo2: Long-Duration and High-Resolution Audio-Driven Portrait Image Animation](https://arxiv.org/abs/2410.07718) | ICLR 2025 | [Code](https://github.com/fudan-generative-vision/hallo2) | [Project](https://fudan-generative-vision.github.io/hallo2) | Diffusion, Hallo |
| 2024 | [Diverse Code Query Learning for Speech-Driven Facial Animation](http://arxiv.org/abs/2409.19143) | ArXiv 2024 |  |  |  |
| 2024 | [TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans](http://arxiv.org/abs/2409.16666) | ECCVW 2024 | [Code](https://github.com/aggelinacha/talkinnerf) | [Project](https://aggelinacha.github.io/TalkinNeRF) | NeRF |
| 2024 | [JoyHallo: Digital human model for Mandarin](https://arxiv.org/abs/2409.13268) | ArXiv 2024 | [Code](https://github.com/jdh-algo/JoyHallo) | [Project](https://jdh-algo.github.io/JoyHallo) | Diffusion, Hallo |
| 2024 | [JEAN: Joint Expression and Audio-guided NeRF-based Talking Face Generation](http://arxiv.org/abs/2409.12156) | BMVC 2024 |  | [Project](https://starc52.github.io/publications/2024-07-19-JEAN) | NeRF |
| 2024 | [3DFacePolicy: Speech-Driven 3D Facial Animation with Diffusion Policy](http://arxiv.org/abs/2409.10848) | ArXiv 2024 |  |  |  |
| 2024 | [LawDNet: Enhanced Audio-Driven Lip Synthesis via Local Affine Warping Deformation](http://arxiv.org/abs/2409.09326) | ArXiv 2024 |  |  |  |
| 2024 | [StyleTalk++: A Unified Framework for Controlling the Speaking Styles of Talking Heads](http://arxiv.org/abs/2409.09292) | TPAMI 2024 |  |  |  |
| 2024 | [ProbTalk3D: Non-Deterministic Emotion Controllable Speech-Driven 3D Facial Animation Synthesis Using VQ-VAE](http://arxiv.org/abs/2409.07966) | SIGGRAPH MIG 2024 | [Code](https://github.com/uuembodiedsocialai/ProbTalk3D) |  | 3D |
| 2024 | [DiffTED: One-shot Audio-driven TED Talk Video Generation with Diffusion-based Co-speech Gestures](http://arxiv.org/abs/2409.07649) | ArXiv 2024 |  |  | diffusion |
| 2024 | [EMOdiffhead: Continuously Emotional Control in Talking Head Generation via Diffusion](http://arxiv.org/abs/2409.07255) | ArXiv 2024 |  |  | Diffusion |
| 2024 | [PersonaTalk: Bring Attention to Your Persona in Visual Dubbing](http://arxiv.org/abs/2409.05379) | SIGGRAPH Asia 2024 |  | [Project](https://grisoon.github.io/PersonaTalk) |  |
| 2024 | [KAN-Based Fusion of Dual-Domain for Audio-Driven Facial Landmarks Generation](http://arxiv.org/abs/2409.05330) | ArXiv 2024 |  |  | KAN |
| 2024 | [SVP: Style-Enhanced Vivid Portrait Talking Head Diffusion Model](http://arxiv.org/abs/2409.03270) | ArXiv 2024 |  |  | Diffusion, Style |
| 2024 | [PoseTalk: Text-and-Audio-based Pose Control and Motion Refinement for One-Shot Talking Head Generation](http://arxiv.org/abs/2409.02657) | ArXiv 2024 |  | [Project](https://junleen.github.io/projects/posetalk) | Pose Latent Diffusion, Lip Synchronization, Text-Audio Control |
| 2024 | [Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming](http://arxiv.org/abs/2408.16725) | Tech Report | [Code](https://github.com/gpt-omni/mini-omni) |  | Omni！！！ |
| 2024 | [TalkLoRA: Low-Rank Adaptation for Speech-Driven Animation](http://arxiv.org/abs/2408.13714) | ArXiv 2024 |  |  | LoRA |
| 2024 | [Meta-Learning Empowered Meta-Face: Personalized Speaking Style Adaptation for Audio-Driven 3D Talking Face Animation](http://arxiv.org/abs/2408.09357) | ArXiv 2024 |  |  |  |
| 2024 | [S^3D-NeRF: Single-Shot Speech-Driven Neural Radiance Field for High Fidelity Talking Head Synthesis](https://arxiv.org/abs/2408.09347) | ECCV 2024 |  |  |  |
| 2024 | [DEEPTalk: Dynamic Emotion Embedding for Probabilistic Speech-Driven 3D Face Animation](http://arxiv.org/abs/2408.06010) | AAAI 2025 | [Code](https://github.com/whwjdqls/DEEPTalk) | [Project](https://whwjdqls.github.io/deeptalk_website) | 3D face, FLAME, Emotion |
| 2024 | [High-fidelity and Lip-synced Talking Face Synthesis via Landmark-based Diffusion Model](http://arxiv.org/abs/2408.05416) | IEEE TIP |  |  |  |
| 2024 | [Style-Preserving Lip Sync via Audio-Aware Style Reference](http://arxiv.org/abs/2408.05412) | IEEE TIP |  |  |  |
| 2024 | [MDT-A2G: Exploring Masked Diffusion Transformers for Co-Speech Gesture Generation](http://arxiv.org/abs/2408.03312) | ArXiv 2024 |  |  | Co-Speech Gesture |
| 2024 | [GLDiTalker: Speech-Driven 3D Facial Animation with Graph Latent Diffusion Transformer](http://arxiv.org/abs/2408.01826) | ArXiv 2024 |  |  |  |
| 2024 | [Landmark-guided Diffusion Model for High-fidelity and Temporally Coherent Talking Head Generation](http://arxiv.org/abs/2408.01732) | ArXiv 2024 |  |  |  |
| 2024 | [JambaTalk: Speech-Driven 3D Talking Head Generation Based on Hybrid Transformer-Mamba Model](http://arxiv.org/abs/2408.01627) | ArXiv 2024 |  |  | 3D |
| 2024 | [Talk Less, Interact Better: Evaluating In-context Conversational Adaptation in Multimodal LLMs](http://arxiv.org/abs/2408.01417) | COLM 2024 | [Code](https://github.com/lil-lab/ICCA) |  | LLM |
| 2024 | [UniTalker: Scaling up Audio-Driven 3D Facial Animation through A Unified Model](http://arxiv.org/abs/2408.00762) | ArXiv 2024 | [Code](https://github.com/X-niper/UniTalker) |  |  |
| 2024 | [DiM-Gesture: Co-Speech Gesture Generation with Adaptive Layer Normalization Mamba-2 framework](http://arxiv.org/abs/2408.00370) | ArXiv 2024 |  |  |  |
| 2024 | [EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head](http://arxiv.org/abs/2408.00297) | ECCV 2024 |  | [Project](https://nju-3dv.github.io/projects/EmoTalk3D) |  |
| 2024 | [LinguaLinker: Audio-Driven Portraits Animation with Implicit Facial Control Enhancement](http://arxiv.org/abs/2407.18595) | ArXiv 2024 |  |  |  |
| 2024 | [Text-based Talking Video Editing with Cascaded Conditional Diffusion](http://arxiv.org/abs/2407.14841) | ArXiv 2024 |  |  |  |
| 2024 | [EmoFace: Audio-driven Emotional 3D Face Animation](http://arxiv.org/abs/2407.12501) | IEEE VR 2024 | [Code](https://github.com/SJTU-Lucy/EmoFace) |  |  |
| 2024 | [Learning Online Scale Transformation for Talking Head Video Generation](http://arxiv.org/abs/2407.09965) | ArXiv 2024 |  |  |  |
| 2024 | [Audio-driven High-resolution Seamless Talking Head Video Editing via StyleGAN](http://arxiv.org/abs/2407.05577) | ArXiv 2024 |  |  | StyleGAN |
| 2024 | [Enhancing Speech-Driven 3D Facial Animation with Audio-Visual Guidance from Lip Reading Expert](http://arxiv.org/abs/2407.01034) | Interspeech 2024 | [Code](https://github.com/kaist-ami/3d-talking-head-av-guidance) | [Project](https://3d-talking-head-avguide.github.io) | 3D |
| 2024 | [RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network](http://arxiv.org/abs/2406.18284) | ArXiv 2024 |  |  |  |
| 2024 | [MultiTalk: Enhancing 3D Talking Head Generation Across Languages with Multilingual Video Dataset](http://arxiv.org/abs/2406.14272) | Interspeech 2024 | [Code](https://github.com/postech-ami/MultiTalk) | [Project](https://multi-talk.github.io) | 3D, Dataset |
| 2024 | [RITA: A Real-time Interactive Talking Avatars Framework](https://arxiv.org/abs/2406.13093) | ArXiv 2024 |  |  | Real-time, Interactive, Talking Avatar |
| 2024 | [NLDF: Neural Light Dynamic Fields for Efficient 3D Talking Head Generation](http://arxiv.org/abs/2406.11259) | ArXiv 2024 |  |  | NeRF |
| 2024 | [Hallo: Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation](https://arxiv.org/abs/2406.08801) | ArXiv 2024 | [Code](https://github.com/fudan-generative-vision/hallo) | [Project](https://fudan-generative-vision.github.io/hallo) | 🔥EMO, Diffusion, Open-source |
| 2024 | [Make Your Actor Talk: Generalizable and High-Fidelity Lip Sync with Motion and Appearance Disentanglement](http://arxiv.org/abs/2406.08096) | ArXiv 2024 |  | [Project](https://Ingrid789.github.io/MyTalk) |  |
| 2024 | [Emotional Conversation: Empowering Talking Faces with Cohesive Expression, Gaze and Pose Generation](http://arxiv.org/abs/2406.07895) | ArXiv 2024 |  |  | Emotion |
| 2024 | [Controllable Talking Face Generation by Implicit Facial Keypoints Editing](http://arxiv.org/abs/2406.02880) | ArXiv 2024 | [Code](https://github.com/NetEase-Media/ControlTalk) |  | Face Edit |
| 2024 | [SPEAK: Speech-Driven Pose and Emotion-Adjustable Talking Head Generation](http://arxiv.org/abs/2405.07257) | ArXiv 2024 |  |  |  |
| 2024 | [NeRFFaceSpeech: One-shot Audio-driven 3D Talking Head Synthesis via Generative Prior](http://arxiv.org/abs/2405.05749) | CVPRW 2024 |  |  | SadTalker+NeRF |
| 2024 | [SwapTalk: Audio-Driven Talking Face Generation with One-Shot Customization in Latent Space](http://arxiv.org/abs/2405.05636) | ICASSP 2025 |  |  |  |
| 2024 | [AniTalker: Animate Vivid and Diverse Talking Faces through Identity-Decoupled Facial Motion Encoding](http://arxiv.org/abs/2405.03121) | ArXiv 2024 | [Code](https://github.com/X-LANCE/AniTalker) |  |  |
| 2024 | [GSTalker: Real-time Audio-Driven Talking Face Generation via Deformable Gaussian Splatting](http://arxiv.org/abs/2404.19040) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [CSTalk: Correlation Supervised Speech-driven 3D Emotional Facial Animation Generation](http://arxiv.org/abs/2404.18604) | ArXiv 2024 |  |  | Emotion |
| 2024 | [GaussianTalker: Real-Time High-Fidelity Talking Head Synthesis with Audio-Driven 3D Gaussian Splatting](https://arxiv.org/abs/2404.16012) | ACMM 2024 | [Code](https://github.com/KU-CVLAB/GaussianTalker) | [Project](https://ku-cvlab.github.io/GaussianTalker) | 🔥Gaussian Splatting |
| 2024 | [TalkingGaussian: Structure-Persistent 3D Talking Head Synthesis via Gaussian Splatting](https://arxiv.org/abs/2404.15264.pdf) | ECCV 2024 | [Code](https://github.com/Fictionarry/TalkingGaussian) | [Project](https://fictionarry.github.io/TalkingGaussian) | 🔥Gaussian Splatting |
| 2024 | [GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting](https://arxiv.org/abs/2404.14037) | ACMM 2024 |  | [Project](https://yuhongyun777.github.io/GaussianTalker) | 🔥Gaussian Splatting |
| 2024 | [Learn2Talk: 3D Talking Face Learns from 2D Talking Face](http://arxiv.org/abs/2404.12888) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [VASA-1: Lifelike Audio-Driven Talking Faces Generated in Real Time](https://arxiv.org/abs/2404.10667) | NeurIPS 2024 |  |  | 🔥🔥🔥Awesome，Microsoft |
| 2024 | [EDTalk: Efficient Disentanglement for Emotional Talking Head Synthesis](https://arxiv.org/abs/2404.01647) | ECCV 2024 | [Code](https://github.com/tanshuai0219/EDTalk) | [Project](https://tanshuai0219.github.io/EDTalk) | Emotion |
| 2024 | [Talk3D: High-Fidelity Talking Portrait Synthesis via Personalized 3D Generative Prior](http://arxiv.org/abs/2403.20153) | ArXiv 2024 | [Code](https://github.com/KU-CVLAB/Talk3D) | [Project](https://ku-cvlab.github.io/Talk3D) |  |
| 2024 | [AniPortrait: Audio-Driven Synthesis of Photorealistic Portrait Animation](https://arxiv.org/abs/2403.17694) | ArXiv 2024 | [Code](https://github.com/scutzzj/AniPortrait) |  | 🔥🔥🔥Similar to EMO |
| 2024 | [Adaptive Super Resolution For One-Shot Talking-Head Generation](http://arxiv.org/abs/2403.15944) | ICASSP 2024 | [Code](https://github.com/Songluchuan/AdaSR-TalkingHead) |  |  |
| 2024 | [EmoVOCA: Speech-Driven Emotional 3D Talking Heads](http://arxiv.org/abs/2403.12886) | ArXiv 2024 |  |  | 3D, VOCA |
| 2024 | [ScanTalk: 3D Talking Heads from Unregistered Scans](https://arxiv.org/abs/2403.10942) | ECCV 2024 | [Code](https://github.com/miccunifi/ScanTalk) |  | 3D |
| 2024 | [FlowVQTalker: High-Quality Emotional Talking Face Generation through Normalizing Flow and Quantization](http://arxiv.org/abs/2403.06375) | ArXiv 2024 |  |  | Normalizing Flow, Vector-Quantization, Lip Sync, Emotional Talking Faces |
| 2024 | [Style2Talker: High-Resolution Talking Head Generation with Emotion Style and Art Style](http://arxiv.org/abs/2403.06365) | ArXiv 2024 |  |  |  |
| 2024 | [FaceChain-ImagineID: Freely Crafting High-Fidelity Diverse Talking Faces from Disentangled Audio](https://arxiv.org/abs/2403.01901) | ArXiv 2024 | [Code](https://github.com/modelscope/facechain) |  |  |
| 2024 | [G4G:A Generic Framework for High Fidelity Talking Face Generation with Fine-grained Intra-modal Alignment](http://arxiv.org/abs/2402.18122) | ArXiv 2024 |  |  | A Generic Framework |
| 2024 | [EMO: Emote Portrait Alive - Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions](https://arxiv.org/abs/2402.17485) | ArXiv 2024 |  |  | 🔥🔥🔥Amazing, Diffusion |
| 2024 | [Learning Dynamic Tetrahedra for High-Quality Talking Head Synthesis](http://arxiv.org/abs/2402.17364) | CVPR 2024 |  |  | High-Quality |
| 2024 | [DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer](http://arxiv.org/abs/2402.05712) | ArXiv 2024 | [Code](https://github.com/theEricMa/DiffSpeaker) |  | 3D |
| 2024 | [EmoSpeaker: One-shot Fine-grained Emotion-Controlled Talking Face Generation](http://arxiv.org/abs/2402.01422) | ArXiv 2024 | [Code](https://github.com/PeterFanFan/Emospeaker_code) | [Project](https://peterfanfan.github.io/EmoSpeaker) | Emotion |
| 2024 | [NeRF-AD: Neural Radiance Field with Attention-based Disentanglement for Talking Face Synthesis](http://arxiv.org/abs/2401.12568) | ICASSP 2024 | [Code](https://github.com/Xiaoxingliu02/codeNeRF-AD) | [Project](https://xiaoxingliu02.github.io/NeRF-AD) | AU |
| 2024 | [Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis](http://arxiv.org/abs/2401.08503) | ICLR 2024 | [Code](https://github.com/yerfor/Real3DPortrait) | [Project](https://real3dportrait.github.io) | 3D, One-Shot, Realistic |
| 2024 | [Dubbing for Everyone: Data-Efficient Visual Dubbing using Neural Rendering Priors](https://arxiv.org/abs/2401.06126) | ArXiv 2024 |  | [Project](https://dubbingforeveryone.github.io) | visual dubbing, lip sync, neural rendering, data-efficient |
| 2024 | [DREAM-Talk: Diffusion-based Realistic Emotional Audio-driven Method for Single Image Talking Face Generation](http://arxiv.org/abs/2312.13578) | ArXiv 2024 |  | [Project](https://magic-research.github.io/dream-talk) | Emotion |
| 2024 | [VectorTalker: SVG Talking Face Generation with Progressive Vectorisation](http://arxiv.org/abs/2312.11568) | ArXiv 2024 |  |  | SVG |
| 2024 | [AE-NeRF: Audio Enhanced Neural Radiance Field for Few Shot Talking Head Synthesis](http://arxiv.org/abs/2312.10921) | AAAI 2024 |  |  |  |
| 2024 | [Mimic: Speaking Style Disentanglement for Speech-Driven 3D Facial Animation](http://arxiv.org/abs/2312.10877) | AAAI 2024 | [Code](https://github.com/huifu99/Mimic) | [Project](https://zeqing-wang.github.io/Mimic) | 3D |
| 2024 | [DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models](http://arxiv.org/abs/2312.09767) | ArXiv 2024 | [Code](https://github.com/ali-vilab/dreamtalk) | [Project](https://dreamtalk-project.github.io) | Diffusion |
| 2024 | [FaceTalk: Audio-Driven Motion Diffusion for Neural Parametric Head Models](http://arxiv.org/abs/2312.08459) | ArXiv 2024 | [Code](https://github.com/shivangi-aneja/FaceTalk) | [Project](https://shivangi-aneja.github.io/projects/facetalk) |  |
| 2024 | [GMTalker: Gaussian Mixture based Emotional talking video Portraits](http://arxiv.org/abs/2312.07669) | ArXiv 2024 |  | [Project](https://bob35buaa.github.io/GMTalker) | Emotion |
| 2024 | [GSmoothFace: Generalized Smooth Talking Face Generation via Fine Grained 3D Face Guidance](http://arxiv.org/abs/2312.07385) | ArXiv 2024 | [Code](https://github.com/zhanghm1995/GSmoothFace) | [Project](https://zhanghm1995.github.io/GSmoothFace) | 3D |
| 2024 | [R2-Talker: Realistic Real-Time Talking Head Synthesis with Hash Grid Landmarks Encoding and Progressive Multilayer Conditioning](http://arxiv.org/abs/2312.05572) | ArXiv 2024 |  |  | based-RAD-NeRF |
| 2024 | [VividTalk: One-Shot Audio-Driven Talking Head Generation Based on 3D Hybrid Prior](http://arxiv.org/abs/2312.01841) | ArXiv 2024 |  |  | Mesh |
| 2024 | [SyncTalk: The Devil😈 is in the Synchronization for Talking Head Synthesis](https://arxiv.org/abs/2311.17590) | CVPR 2024 | [Code](https://github.com/ziqiaopeng/SyncTalk) | [Project](https://ziqiaopeng.github.io/synctalk) | 😈Talking Head |
| 2024 | [GAIA: Zero-shot Talking Avatar Generation](https://arxiv.org/abs/2311.15230.pdf) | ArXiv 2024 |  | [Project](https://microsoft.github.io/GAIA) | 😲😲😲 |
| 2024 | [AdaMesh: Personalized Facial Expressions and Head Poses for Adaptive Speech-Driven 3D Facial Animation](http://arxiv.org/abs/2310.07236) | IEEE Transactions on Multimedia | [Code](https://github.com/adamesh/adamesh) | [Project](https://adamesh.github.io) | 3D, Mesh |
| 2024 | [DT-NeRF: Decomposed Triplane-Hash Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://arxiv.org/abs/2309.07752) | ICASSP 2024 |  |  | ER-NeRF |
| 2024 | [EchoMimic: Lifelike Audio-Driven Portrait Animations through Editable Landmark Conditioning](https://github.com/BadToBest/EchoMimic) | AAAI 2025 |  |  | 🔥阿里 |
| 2024 | [Pose-Aware 3D Talking Face Synthesis using Geometry-guided Audio-Vertices Attention](https://ieeexplore.ieee.org/abstract/document/10452856) | IEEE 2024 |  |  |  |
| 2023 | [DiffDub: Person-generic Visual Dubbing Using Inpainting Renderer with Diffusion Auto-encoder](https://arxiv.org/abs/2311.01811) | ICASSP 2024 | [Code](https://github.com/liutaocode/DiffDub) | [Project](https://liutaocode.github.io/DiffDub) | visual dubbing, diffusion, inpainting, person-generic |
| 2023 | [Towards Streaming Speech-to-Avatar Synthesis](http://arxiv.org/abs/2310.16287) | ArXiv 2023 |  |  | Streaming Synthesis, Articulatory Inversion, Real-time, Speech-driven |
| 2023 | [OSM-Net: One-to-Many One-shot Talking Head Generation with Spontaneous Head Motions](http://arxiv.org/abs/2309.16148) | ArXiv 2023 |  |  | One-shot Talking Head, Head Motions, One-to-Many Mapping, Audio-driven |
| 2023 | [Efficient Emotional Adaptation for Audio-Driven Talking-Head Generation](https://arxiv.org/abs/2309.04946) | ICCV 2023 | [Code](https://github.com/yuangan/EAT_code) | [Project](https://yuangan.github.io/eat) | - |
| 2023 | [Audio-Driven Dubbing for User Generated Contents via Style-Aware Semi-Parametric Synthesis](https://arxiv.org/abs/2309.00030) | TCSVT 2023 |  |  |  |
| 2023 | [Implicit Identity Representation Conditioned Memory Compensation Network for Talking Head Video Generation](https://arxiv.org/abs/2307.10008) | ICCV 2023 |  |  | - |
| 2023 | [Emotional Talking Head Generation based on Memory-Sharing and Attention-Augmented Networks](https://arxiv.org/abs/2306.03594) | InterSpeech 2023 |  |  | Emotion |
| 2023 | [StyleSync: High-Fidelity Generalized and Personalized Lip Sync in Style-based Generator](https://arxiv.org/abs/2305.05445.pdf) | CVPR 2023 | [Code](https://github.com/guanjz20/StyleSync) | [Project](https://hangz-nju-cuhk.github.io/projects/StyleSync) | - |
| 2023 | [High-fidelity Generalized Emotional Talking Face Generation with Multi-modal Emotion Space Learning](https://arxiv.org/abs/2305.02572) | CVPR 2023 |  |  | Emotion |
| 2023 | [FONT: Flow-guided One-shot Talking Head Generation with Natural Head Motions](http://arxiv.org/abs/2303.17789) | ICME 2023 |  |  | Natural Head Motions, Flow-guided, Audio-driven Pose Prediction, One-shot Talking Head |
| 2023 | [DAE-Talker: High Fidelity Speech-Driven Talking Face Generation with Diffusion Autoencoder](https://arxiv.org/abs/2303.17550.pdf) | ACMM 2023 |  |  | 🔥Diffusion |
| 2023 | [TalkLip: Seeing What You Said - Talking Face Generation Guided by a Lip Reading Expert](https://arxiv.org/abs/2303.17480.pdf) | CVPR 2023 |  |  |  |
| 2023 | [OTAvatar: One-shot Talking Face Avatar with Controllable Tri-plane Rendering](http://arxiv.org/abs/2303.14662) | CVPR 2023 | [Code](https://github.com/theEricMa/OTAvatar) |  | Tri-plane Rendering, One-shot Avatar, Controllable, 3D Consistency |
| 2023 | [Emotionally Enhanced Talking Face Generation](https://arxiv.org/abs/2303.11548.pdf) | ArXiv 2023 |  |  | Emotion |
| 2023 | [EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation](https://arxiv.org/abs/2303.11089) | ICCV 2023 | [Code](https://github.com/psyai-net/EmoTalk_release) | [Project](https://ziqiaopeng.github.io/emotalk) | 3D, Emotion |
| 2023 | [READ Avatars: Realistic Emotion-controllable Audio Driven Avatars](https://arxiv.org/abs/2303.00744) | ArXiv 2023 |  |  | - |
| 2023 | [OPT: One-shot Pose-Controllable Talking Head Generation](http://arxiv.org/abs/2302.08197) | ICASSP 2023 |  |  | pose control, identity preservation, audio feature disentanglement |
| 2023 | [DiffTalk: Crafting Diffusion Models for Generalized Talking Head Synthesis](https://arxiv.org/abs/2301.03786) | CVPR 2023 | [Code](https://github.com/sstzal/DiffTalk) | [Project](https://sstzal.github.io/DiffTalk) | 🔥Diffusion |
| 2023 | [CodeTalker: Speech-Driven 3D Facial Animation with Discrete Motion Prior](https://arxiv.org/abs/2301.02379) | CVPR 2023 | [Code](https://github.com/Doubiiu/CodeTalker) | [Project](https://doubiiu.github.io/projects/codetalker) | 3D, codebook |
| 2023 | [StyleTalk: One-shot Talking Head Generation with Controllable Speaking Styles](https://arxiv.org/abs/2301.01081) | AAAI 2023 | [Code](https://github.com/FuxiVirtualHuman/styletalk) |  | Style |
| 2023 | [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation](https://arxiv.org/abs/2211.12194.pdf) | CVPR 2023 | [Code](https://github.com/Winfredy/SadTalker) | [Project](https://sadtalker.github.io) | 3D, Single Image |
| 2023 | [Efficient Region-Aware Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Efficient_Region-Aware_Neural_Radiance_Fields_for_High-Fidelity_Talking_Portrait_Synthesis_ICCV_2023_paper.pdf) | ICCV 2023 |  |  | Tri-plane |
| 2023 | [LipNeRF: What is the right feature space to lip-sync a NeRF?](https://www.amazon.science/publications/lipnerf-what-is-the-right-feature-space-to-lip-sync-a-nerf) | FG 2023 |  |  | Wav2lip |
| 2023 | [ToonTalker: Cross-Domain Face Reenactment](https://openaccess.thecvf.com/content/ICCV2023/papers/Gong_ToonTalker_Cross-Domain_Face_Reenactment_ICCV_2023_paper.pdf) | ICCV 2023 |  |  | - |
| 2023 | [EMMN: Emotional Motion Memory Network for Audio-driven Emotional Talking Face Generation](https://openaccess.thecvf.com/content/ICCV2023/papers/Tan_EMMN_Emotional_Motion_Memory_Network_for_Audio-driven_Emotional_Talking_Face_ICCV_2023_paper.pdf) | ICCV 2023 |  |  | Emotion |
| 2023 | [Facediffuser: Speech-driven 3d facial animation synthesis using diffusion](https://dl.acm.org/doi/abs/10.1145/3623264.3624447) | ACM SIGGRAPH MIG 2023 |  |  | 🔥Diffusion, 3D |
| 2023 | [DINet: Deformation Inpainting Network for Realistic Face Visually Dubbing on High Resolution Video](https://fuxivirtualhuman.github.io/pdf/AAAI2023_FaceDubbing.pdf) | AAAI 2023 |  |  |  |
| 2023 | [Diffused Heads: Diffusion Models Beat GANs on Talking-Face Generation](https://mstypulkowski.github.io/diffusedheads/diffused_heads.pdf) | ArXiv 2023 |  |  | 🔥Diffusion |
| 2022 | [Memories are One-to-Many Mapping Alleviators in Talking Face Generation](https://arxiv.org/abs/2212.05005.pdf) | ArXiv 2022 |  | [Project](https://memoryface.github.io) | - |
| 2022 | [Masked Lip-Sync Prediction by Audio-Visual Contextual Exploitation in Transformers](https://arxiv.org/abs/2212.04970.pdf) | SIGGRAPH Asia 2022 |  |  | - |
| 2022 | [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](https://arxiv.org/abs/2211.14758) | SIGGRAPH 2022 |  |  |  |
| 2022 | [Progressive Disentangled Representation Learning for Fine-Grained Controllable Talking Head Synthesis](http://arxiv.org/abs/2211.14506) | ArXiv 2022 |  |  | disentangled representation, contrastive learning, multi-motion control |
| 2022 | [SPACEx 🚀: Speech-driven Portrait Animation with Controllable Expression](https://arxiv.org/abs/2211.09809.pdf) | ArXiv 2022 |  | [Project](https://deepimagination.cc/SPACEx/) | - |
| 2022 | [Pre-Avatar: An Automatic Presentation Generation Framework Leveraging Talking Avatar](https://arxiv.org/abs/2210.06877) | ICTAI2022 |  |  | talking avatar, presentation |
| 2022 | [EAMM: One-Shot Emotional Talking Face via Audio-Based Emotion-Aware Motion Model](https://arxiv.org/abs/2205.15278.pdf) | SIGGRAPH 2022 |  |  | Emotion |
| 2022 | [Emotion-Controllable Generalized Talking Face Generation](http://arxiv.org/abs/2205.01155) | IJCAI 2022 |  |  | emotion control, graph convolutional network, geometry-aware |
| 2022 | [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](http://arxiv.org/abs/2203.04036) | ArXiv 2022 |  |  | StyleGAN, high-resolution, one-shot, lip sync |
| 2022 | [Expressive Talking Head Generation with Granular Audio-Visual Control](https://openaccess.thecvf.com/content/CVPR2022/papers/Liang_Expressive_Talking_Head_Generation_With_Granular_Audio-Visual_Control_CVPR_2022_paper.pdf) | CVPR 2022 |  |  | - |
| 2022 | [Talking Face Generation with Multilingual TTS](https://openaccess.thecvf.com/content/CVPR2022/papers/Song_Talking_Face_Generation_With_Multilingual_TTS_CVPR_2022_paper.pdf) | CVPR 2022 |  |  | - |
| 2021 | [One-shot Talking Face Generation from Single-speaker Audio-Visual Correlation Learning](http://arxiv.org/abs/2112.02749) | AAAI 2022 |  |  | one-shot, audio-visual correlation, keypoint-based motion, lip sync |
| 2021 | [Imitating Arbitrary Talking Style for Realistic Audio-Driven Talking Face Synthesis](https://arxiv.org/abs/2111.00203) | ACM MM 2021 |  |  | - |
| 2021 | [Talking Head Generation with Audio and Speech Related Facial Action Units](https://arxiv.org/abs/2110.09951.pdf) | BMVC 2021 |  |  | AU |
| 2021 | [Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion](http://arxiv.org/abs/2107.09293) | ArXiv 2021 |  |  | Audio-driven, Talking-head, Head Motion, Keypoint-based Motion |
| 2021 | [3D-TalkEmo: Learning to Synthesize 3D Emotional Talking Head](http://arxiv.org/abs/2104.12051) | ArXiv 2021 |  |  | 3D Talking Head, Emotion, Geometry Map, Audio-driven |
| 2021 | [PC-AVS: Pose-Controllable Talking Face Generation by Implicitly Modularized Audio-Visual Representation](https://arxiv.org/abs/2104.11116) | CVPR 2021 |  |  | - |
| 2021 | [MakeItTalk: Speaker-Aware Talking-Head Animation](http://arxiv.org/abs/2004.12992) | SIGGRAPH Asia 2020 |  |  | Speaker-Aware, Audio-Driven, Facial Landmarks, Photorealistic |
| 2021 | [Speech2Talking-Face: Inferring and Driving a Face with Synchronized Audio-Visual Representation](https://www.ijcai.org/proceedings/2021/0141.pdf) | IJCAI 2021 |  |  | - |
| 2021 | [Audio-Driven Emotional Video Portraits](https://openaccess.thecvf.com/content/CVPR2021/papers/Ji_Audio-Driven_Emotional_Video_Portraits_CVPR_2021_paper.pdf) | CVPR 2021 |  |  | Emotion |
| 2021 | [IATS: Imitating Arbitrary Talking Style for Realistic Audio-Driven Talking Face Synthesis](https://dl.acm.org/doi/pdf/10.1145/3474085.3475280) | ACM Multimedia 2021 |  |  | - |
| 2020 | [Multi Modal Adaptive Normalization for Audio to Video Generation](http://arxiv.org/abs/2012.07304) | ArXiv 2020 |  |  | Audio-to-Video, Multi-Modal Adaptive Normalization, Facial Video Generation, Keypoint Heatmap |
| 2020 | [A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild](http://arxiv.org/abs/2008.10010.pdf) | ACM Multimedia 2020 |  |  | - |
| 2020 | [Talking-head Generation with Rhythmic Head Motion](https://arxiv.org/abs/2007.08547.pdf) | ECCV 2020 |  |  | - |
| 2020 | [Speaker-Aware Talking-Head Animation](https://arxiv.org/abs/2006.09661.pdf) | SIGGRAPH Asia 2020 |  |  | - |
| 2020 | [Neural Voice Puppetry: Audio-driven Facial Reenactment](https://arxiv.org/abs/1912.05566.pdf) | ECCV 2020 |  |  | - |
| 2020 | [Realistic Speech-Driven Facial Animation with GANs](https://arxiv.org/abs/1906.06337.pdf) | IJCV 2020 |  |  | - |
| 2020 | [A Large-scale Audio-visual Dataset for Emotional Talking-face Generation](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123660698.pdf) | ECCV 2020 |  |  | - |
| 2019 | [Talking Face Generation by Adversarially Disentangled Audio-Visual Representation](https://arxiv.org/abs/1807.07860.pdf) | AAAI 2019 |  |  | - |
| 2019 | [Hierarchical Cross-modal Talking Face Generation with Dynamic Pixel-wise Loss](https://www.cs.rochester.edu/~cxu22/p/cvpr2019_facegen_paper.pdf) | CVPR 2019 |  |  | - |
| 2018 | [Audio-Driven Animator-Centric Speech Animation](https://arxiv.org/abs/1805.09488.pdf) | SIGGRAPH 2018 |  |  | - |
| 2018 | [Lip Movements Generation at a Glance](https://openaccess.thecvf.com/content_ECCV_2018/papers/Lele_Chen_Lip_Movements_Generation_ECCV_2018_paper.pdf) | ECCV 2018 |  |  | - |
| 2017 | [You Said That? Synthesising Talking Faces From Audio](https://arxiv.org/abs/1705.02966) | BMVC 2019 |  |  | - |
| 2017 | [Synthesizing Obama: Learning Lip Sync From Audio](https://grail.cs.washington.edu/projects/AudioToObama/siggraph17_obama.pdf) | SIGGRAPH 2017 |  |  | - |
| 2017 | [Audio-Driven Facial Animation by Joint End-to-End Learning of Pose and Emotion](https://users.aalto.fi/~laines9/publications/karras2017siggraph_paper.pdf) | SIGGRAPH 2017 |  |  | - |
| 2017 | [A Deep Learning Approach for Generalized Speech Animation](https://home.ttic.edu/~taehwan/taylor_etal_siggraph2017.pdf) | SIGGRAPH 2017 |  |  | - |

---



## Portrait Animation

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [MMFace-DiT: A Dual-Stream Diffusion Transformer for High-Fidelity Multimodal Face Generation](https://arxiv.org/abs/2603.29029) | CVPR 2026 | [Code](https://github.com/Bharath-K3/MMFace-DiT) | [Project](https://vcbsl.github.io/MMFace-DiT/) | Diffusion Transformer, Multimodal, Face Generation |
| 2026 | [FG-Portrait: 3D Flow Guided Editable Portrait Animation](https://arxiv.org/abs/2603.23381) | CVPR 2026 |  |  | portrait animation, 3D flow, CVPR |
| 2026 | [MoCha:End-to-End Video Character Replacement without Structural Guidance](https://arxiv.org/abs/2601.08587) | ArXiv 2026 |  |  | Talking Head |
| 2025 | [Knot Forcing: Taming Autoregressive Video Diffusion Models for Real-time Infinite Interactive Portrait Animation](https://arxiv.org/abs/2512.21734) | ArXiv 2025 | [Code](https://github.com/HumanAIGC/knot_forcing) | [Project](https://humanaigc.github.io/knot_forcing_demo_page/) | Diffusion, Real-time, Portrait Animation, Attention |
| 2025 | [SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation](https://arxiv.org/abs/2512.17331) | ArXiv 2025 |  |  | Portrait Animation, ICASSP, Attention |
| 2025 | [FlashPortrait: 6x Faster Infinite Portrait Animation with Adaptive Latent Prediction](https://arxiv.org/abs/2512.16900) | ArXiv 2025 |  |  | Portrait Animation, Transformer, Latent |
| 2025 | [DeX-Portrait: Disentangled and Expressive Portrait Animation via Explicit and Latent Motion Representations](https://arxiv.org/abs/2512.15524) | ArXiv 2025 |  | [Project](https://syx132.github.io/DeX-Portrait) | Portrait Animation, Disentangled, Expressive |
| 2025 | [FactorPortrait: Controllable Portrait Animation via Disentangled Expression, Pose, and Viewpoint](https://arxiv.org/abs/2512.11645) | ArXiv 2025 |  | [Project](https://tangjiapeng.github.io/FactorPortrait/) | Portrait Animation, Transformer, Latent |
| 2025 | [PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://arxiv.org/abs/2512.11253) | ArXiv 2025 |  |  | Streaming, Portrait Animation |
| 2025 | [Beat on Gaze: Learning Stylized Generation of Gaze and Head Dynamics](http://arxiv.org/abs/2509.17168) | ArXiv 2025 |  |  | Gaze Control, Head Motion, Style-Aware, 3D |
| 2025 | [Navigating Large-Pose Challenge for High-Fidelity Face Reenactment with Video Diffusion Model](https://arxiv.org/abs/2507.16341) | ArXiv 2025 |  |  | Face Reenactment, Large-Pose, Video Diffusion |
| 2025 | [Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](http://arxiv.org/abs/2503.22225) | ArXiv 2025 |  |  |  |
| 2025 | [HunyuanPortrait: Implicit Condition Control for Enhanced Portrait Animation](https://arxiv.org/abs/2503.18860) | CVPR 2025 |  |  | Hunyuan |
| 2025 | [Playmate: Flexible Control of Portrait Animation via 3D-Implicit Space Guided Diffusion](http://arxiv.org/abs/2502.07203) | ArXiv 2025 | [Code](https://github.com/Playmate111/Playmate) |  | Diffusion, 3D |
| 2025 | [MobilePortrait: Real-Time One-Shot Neural Head Avatars on Mobile Devices](http://arxiv.org/abs/2407.05712) | CVPR 2025 |  |  | 100+fps |
| 2025 | [GOES: 3D Gaussian-based One-shot Head Animation with Any Emotion and Any Style](https://dl.acm.org/doi/abs/10.1145/3746027.3755001) | ACM MM 2025 |  |  | One-Shot, 3DGS |
| 2024 | [GoHD: Gaze-oriented and Highly Disentangled Portrait Animation with Rhythmic Poses and Realistic Expression](http://arxiv.org/abs/2412.09296) | AAAI 2025 |  |  | Gaze-oriented |
| 2024 | [Avatar Concept Slider: Manipulate Concepts In Your Human Avatar With Fine-grained Control](http://arxiv.org/abs/2408.13995) | ArXiv 2024 |  |  |  |
| 2024 | [G3FA: Geometry-guided GAN for Face Animation](http://arxiv.org/abs/2408.13049) | BMVC 2024 |  |  |  |
| 2024 | [Anchored Diffusion for Video Face Reenactment](https://arxiv.org/abs/2407.15153) | ArXiv 2024 |  |  | Face Reenactment, Anchored Diffusion |
| 2024 | [One-Shot Pose-Driving Face Animation Platform](http://arxiv.org/abs/2407.08949) | ArXiv 2024 |  |  | One-Shot, Pose-Driving, Face Animation, Talking Head |
| 2024 | [V-Express: Conditional Dropout for Progressive Training of Portrait Video Generation](https://arxiv.org/abs/2406.02511) | Tech Report |  |  | 🔥EMO, Diffusion, Open-source |
| 2024 | [EMOPortraits: Emotion-enhanced Multimodal One-shot Head Avatars](http://arxiv.org/abs/2404.19110) | ArXiv 2024 |  |  | EMO |
| 2024 | [FSRT: Facial Scene Representation Transformer for Face Reenactment from Factorized Appearance, Head-pose, and Facial Expression Features](https://arxiv.org/abs/2404.09736) | CVPR 2024 |  |  | Face Reenactment, Transformer |
| 2024 | [DiffusionAct: Controllable Diffusion Autoencoder for One-shot Face Reenactment](https://arxiv.org/abs/2403.17217) | ArXiv 2024 | [Code](https://github.com/StelaBou/Diffusion-Act) | [Project](https://stelabou.github.io/diffusionact) | face reenactment, diffusion autoencoder, one-shot, controllable |
| 2024 | [One-shot Neural Face Reenactment via Finding Directions in GAN's Latent Space](https://arxiv.org/abs/2402.03553) | IJCV |  |  | face reenactment, GAN, one-shot, latent space |
| 2024 | [CVTHead: One-shot Controllable Head Avatar with Vertex-feature Transformer](https://arxiv.org/abs/2311.06443) | WACV 2024 |  |  |  |
| 2024 | [VLOGGER: Multimodal Diffusion for Embodied](https://enriccorona.github.io/vlogger/paper.pdf) | ArXiv 2024 |  |  | Embodied |
| 2023 | [MaskRenderer: 3D-Infused Multi-Mask Realistic Face Reenactment](https://arxiv.org/abs/2309.05095) | ArXiv 2023 |  |  | face reenactment, 3D-infused, multi-mask, real-time |
| 2023 | [Controllable One-Shot Face Video Synthesis With Semantic Aware Prior](http://arxiv.org/abs/2304.14471) | ArXiv 2023 |  |  | One-shot Talking Head, Semantic Aware Prior, Controllable Generation, Pose Alignment |

---



## Text-driven

| Year | Title | Conference/Journal | Code/Proj |
| ---- | ---- | ---- | ---- |
| 2026 | [Text-Driven Emotionally Continuous Talking Face Generation](https://arxiv.org/abs/2603.06071) | ArXiv 2026 |  |
| 2026 | [Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars](http://arxiv.org/abs/2602.01538) | ArXiv 2026 | [Code](https://github.com/angzong/InteractAvatar) [Project](https://interactavatar.github.io) |
| 2026 | [ActAvatar: Temporally-Aware Precise Action Control for Talking Avatars](http://arxiv.org/abs/2512.19546) | CVPR 2026 | [Project](https://ziqiaopeng.github.io/ActAvatar/) |
| 2025 | [KeyframeFace: From Text to Expressive Facial Keyframes](https://arxiv.org/abs/2512.11321) | ArXiv 2025 | [Code](https://github.com/wjc12345123/KeyframeFace) [Project](https://github.com/wjc12345123/KeyframeFace) |
| 2025 | [Text2Lip: Progressive Lip-Synced Talking Face Generation from Text via Viseme-Guided Rendering](http://arxiv.org/abs/2508.02362) | ArXiv 2025 | [Project](https://plyon1.github.io/Text2Lip/) |
| 2025 | [Think-Before-Draw: Decomposing Emotion Semantics & Fine-Grained Controllable Expressive Talking Head Generation](http://arxiv.org/abs/2507.12761) | ArXiv 2025 |  |
| 2025 | [OmniTalker: Real-Time Text-Driven Talking Head Generation with In-Context Audio-Visual Style Replication](http://arxiv.org/abs/2504.02433) | ArXiv 2025 | [Project](https://humanaigc.github.io/omnitalker/) |
| 2025 | [When Words Smile: Generating Diverse Emotional Facial Expressions from Text](https://arxiv.org/abs/2412.02508) | EMNLP 2025 | [Code](https://github.com/WalkerMitty/EmoAva) [Project](https://walkermitty.github.io/EmoAva/) |
| 2024 | [GenCA: A Text-conditioned Generative Model for Realistic and Drivable Codec Avatars](http://arxiv.org/abs/2408.13674) | ArXiv 2024 |  |
| 2024 | [InstructAvatar: Text-Guided Emotion and Motion Control for Avatar Generation](http://arxiv.org/abs/2405.15758) | ArXiv 2024 | [Code](https://github.com/wangyuchi369/InstructAvatar) [Project](https://wangyuchi369.github.io/InstructAvatar) |
| 2024 | [FT2TF: First-Person Statement Text-To-Talking Face Generation](http://arxiv.org/abs/2312.05430) | WACV 2025 |  |
| 2024 | [Text-Driven Talking Face Synthesis by Reprogramming Audio-Driven Models](https://arxiv.org/abs/2306.16003) | ICASSP 2024 |  |
| 2024 | [HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04681.pdf) | ECCV 2024 | [Code](https://github.com/ZhenglinZhou/HeadStudio) [Project](https://zhenglinzhou.github.io/HeadStudio-ProjectPage/) |
| 2023 | [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](http://arxiv.org/abs/2312.06613) | ArXiv 2023 |  |
| 2023 | [AgentAvatar: Disentangling Planning, Driving and Rendering for Photorealistic Avatar Agents](http://arxiv.org/abs/2311.17465) | ArXiv 2023 | [Code](https://github.com/Dorniwang/AgentAvatar) [Project](https://dorniwang.github.io/AgentAvatar_project) |
| 2023 | [Text-to-Video: A Two-stage Framework for Zero-shot Identity-agnostic Talking-head Generation](https://arxiv.org/abs/2308.06457) | ArXiv | [Code](https://github.com/ZhichaoWang970201/Text-to-Video/tree/main) |
| 2023 | [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](https://arxiv.org/abs/2306.03504) | ICML 2023 Workshop |  |
| 2023 | [TalkCLIP: Talking Head Generation with Text-Guided Expressive Speaking Styles](https://arxiv.org/abs/2304.00334.pdf) | ArXiv |  |
| 2022 | [Text2Video: Text-driven Talking-head Video Synthesis with Phonetic Dictionary](https://arxiv.org/abs/2104.14631) | ICASSP 2022 | [Code](https://github.com/sibozhang/Text2Video) [Project](https://sites.google.com/view/sibozhang/text2video) |
| 2021 | [Txt2vid: Ultra-low bitrate compression of talking-head videos via text](https://arxiv.org/abs/2106.14014) | ArXiv | [Code](https://github.com/tpulkit/txt2vid) |
| 2021 | [Write-a-speaker: Text-based Emotional and Rhythmic Talking-head Generation](https://arxiv.org/abs/2104.07995) | AAAI | [Code](https://github.com/FuxiVirtualHuman/Write-a-Speaker) |

---



## NeRF & 3D Head Avatar

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782) | ArXiv 2026 | [Code](https://github.com/YuanSun-XJTU/CompHairHead) | [Project](https://yuansun-xjtu.github.io/CompHairHead.io) | 3D, avatar, head avatar, hair, one-shot, compositional |
| 2026 | [Giving Faces Their Feelings Back: Explicit Emotion Control for Feedforward Single-Image 3D Head Avatars](https://arxiv.org/abs/2604.14541) | ArXiv 2026 |  |  | 3D, avatar, emotion, head avatar |
| 2026 | [3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171) | ArXiv 2026 |  | [Project](https://jalees018.github.io/3DRealHead) | 3D, avatar, head avatar, few-shot |
| 2026 | [PerformRecast: Expression and Head Pose Disentanglement for Portrait Video Editing](https://arxiv.org/abs/2603.19731) | CVPR 2026 |  | [Project](https://youku-aigc.github.io/PerformRecast) | Portrait Editing, Expression Control, Head Pose Disentanglement |
| 2026 | [TDMM-LM: Bridging Facial Understanding and Animation via Language Models](https://arxiv.org/abs/2603.16936) | ArXiv 2026 |  | [Project](https://songluchuan.github.io/TDMM-LM) | Facial Animation, Language Models, Text-guided |
| 2026 | [NBAvatar: Neural Billboards Avatars with Realistic Hand-Face Interaction](https://arxiv.org/abs/2603.12063) | ArXiv 2026 |  |  | Hand-Face Interaction, Neural Billboards, Avatar |
| 2026 | [Motion Manipulation via Unsupervised Keypoint Positioning in Face Animation](https://arxiv.org/abs/2603.04302) | ArXiv 2026 |  |  | Face Animation, Unsupervised Keypoint, Motion Manipulation |
| 2026 | [Skullptor: High Fidelity 3D Head Reconstruction in Seconds with Multi-View Normal Prediction](https://arxiv.org/abs/2602.21100) | ArXiv 2026 |  | [Project](https://ubisoft-laforge.github.io/character/skullptor/) | 3D Head Reconstruction, Multi-View Normal, Feed-forward |
| 2026 | [Toward Fine-Grained Facial Control in 3D Talking Head Generation](https://arxiv.org/abs/2602.09736) | ArXiv 2026 |  |  | 3D, Talking Head |
| 2026 | [Ex-Omni: Enabling 3D Facial Animation Generation for Omni-modal Large Language Models](http://arxiv.org/abs/2602.07106) | ArXiv 2026 |  |  | 3D Facial Animation, Speech-Driven, Omni-modal LLMs, Token-as-query Fusion |
| 2026 | [From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122) | 3DV 2026 | [Code](https://github.com/humansensinglab/super-head) | [Project](https://humansensinglab.github.io/super-head/) | 3D, Talking Head, 3DV, Latent |
| 2026 | [Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference](https://arxiv.org/abs/2601.21269) | ArXiv 2026 |  |  | 3D, Talking Head |
| 2026 | [GAT-NeRF: Geometry-Aware-Transformer Enhanced Neural Radiance Fields for High-Fidelity 4D Facial Avatars](https://arxiv.org/abs/2601.14875) | ArXiv 2026 |  |  | NeRF, Geometry-Aware Transformer, 4D Facial Avatar |
| 2026 | [REFA: Real-time Egocentric Facial Animations for Virtual Reality](https://arxiv.org/abs/2601.03507) | ArXiv 2026 |  |  | Egocentric, Facial Animation, VR, Real-time |
| 2026 | [MANGO:Natural Multi-speaker 3D Talking Head Generation via 2D-Lifted Enhancement](https://arxiv.org/abs/2601.01749) | ArXiv 2026 |  |  | 3D, Talking Head, Transformer |
| 2025 | [FlexAvatar: Learning Complete 3D Head Avatars with Partial Supervision](http://arxiv.org/abs/2512.15599) | ArXiv 2025 |  | [Project](https://tobias-kirschstein.github.io/flexavatar/) | 3D head avatar, partial supervision, transformer, monocular training |
| 2025 | [PESTalk: Speech-Driven 3D Facial Animation with Personalized Emotional Styles](https://arxiv.org/abs/2512.05121) | ArXiv 2025 |  |  | 3D facial animation, speech-driven, emotion |
| 2025 | [Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?](https://arxiv.org/abs/2511.07940) | ArXiv 2025 |  |  | Talking Head, Attention |
| 2025 | [Capturing Head Avatar with Hand Contacts from a Monocular Video](http://arxiv.org/abs/2510.17181) | ICCV 2025 |  |  | Head Avatar, Hand Contacts, Monocular Video, 3D Reconstruction |
| 2025 | [HRM²Avatar: High-Fidelity Real-Time Mobile Avatars from Monocular Phone Scans](http://arxiv.org/abs/2510.13587) | SIGGRAPH Asia 2025 | [Code](https://github.com/alibaba/Taobao3D/tree/main/HRM2Avatar) | [Project](https://acennr-engine.github.io/HRM2Avatar) | Mobile, Real-Time, Monocular, Avatar |
| 2025 | [MVP4D: Multi-View Portrait Video Diffusion for Animatable 4D Avatars](http://arxiv.org/abs/2510.12785) | ArXiv 2025 |  |  | Multi-View, Portrait Video, Diffusion, 4D Avatar |
| 2025 | [3DiFACE: Synthesizing and Editing Holistic 3D Facial Animation](http://arxiv.org/abs/2509.26233) | ArXiv 2025 | [Code](https://github.com/bala1144/3DiFACE) | [Project](https://balamuruganthambiraja.github.io/3DiFACE) | 3D Facial Animation, Diffusion, Editing, Speech-Driven |
| 2025 | [SIE3D: Single-image Expressive 3D Avatar generation via Semantic Embedding and Perceptual Expression Loss](http://arxiv.org/abs/2509.24004) | ArXiv 2025 |  | [Project](https://blazingcrystal1747.github.io/SIE3D/) | Expressive, Text-Driven, Single Image |
| 2025 | [Hyper Diffusion Avatars: Dynamic Human Avatar Generation using Network   Weight Space Diffusion](http://arxiv.org/abs/2509.04145) | ArXiv 2025 |  |  | Dynamic Avatar, Weight-Space Diffusion |
| 2025 | [TeRA: Rethinking Text-guided Realistic 3D Avatar Generation](http://arxiv.org/abs/2509.02466) | ICCV 2025 |  |  | Text-to-Avatar, Latent Diffusion |
| 2025 | [DevilSight: Augmenting Monocular Human Avatar Reconstruction through a   Virtual Perspective](http://arxiv.org/abs/2509.00403) | ArXiv 2025 |  |  | Avatar Reconstruction, Video Generation |
| 2025 | [EPSilon: Efficient Point Sampling for Lightening of Hybrid-based 3D Avatar Generation](http://arxiv.org/abs/2507.13648) | ArXiv 2025 | [Code](https://github.com/seungjun-moon/epsilon) |  | Efficient Point Sampling, Hybrid 3D Avatar |
| 2025 | [VisualSpeaker: Visually-Guided 3D Avatar Lip Synthesis](http://arxiv.org/abs/2507.06060) | ICCV 2025 Workshop |  |  | Visually-Guided, 3D Avatar, Lip Synthesis |
| 2025 | [Generative Head-Mounted Camera Captures for Photorealistic Avatars](http://arxiv.org/abs/2507.05620) | SIGGRAPH Asia 2025 |  | [Project](https://shawn615.github.io/genhmc/) | Head-Mounted Camera, Photorealistic, Avatar |
| 2025 | [AvatarMakeup: Realistic Makeup Transfer for 3D Animatable Head Avatars](http://arxiv.org/abs/2507.02419) | ArXiv 2025 |  |  | 3D Makeup Transfer, Avatar |
| 2025 | [Bind-Your-Avatar: Multi-Talking-Character Video Generation with Dynamic 3D-mask-based Embedding Router](http://arxiv.org/abs/2506.19833) | ArXiv 2025 |  |  | Multi-Character, 3D-mask |
| 2025 | [Controllable Expressive 3D Facial Animation via Diffusion in a Unified Multimodal Space](http://arxiv.org/abs/2506.10007) | ICME 2025 |  | [Project](https://kangweiiliu.github.io/Control_3D_Animation) | 3D, Diffusion, Multimodal |
| 2025 | [SmartAvatar: Text- and Image-Guided Human Avatar Generation with VLM AI Agents](http://arxiv.org/abs/2506.04606) | ArXiv 2025 |  |  | Text-Guided, VLM Agents |
| 2025 | [UMA: Ultra-detailed Human Avatars via Multi-level Surface Alignment](http://arxiv.org/abs/2506.01802) | ArXiv 2025 |  |  | Ultra-detailed, Surface Alignment |
| 2025 | [Total-Editing: Head Avatar with Editable Appearance, Motion, and Lighting](http://arxiv.org/abs/2505.20582) | ArXiv 2025 |  |  | Neural Radiance Fields, Intrinsic Decomposition, Portrait Editing, Motion Control |
| 2025 | [AniCrafter: Customizing Realistic Human-Centric Animation via Avatar-Background Conditioning in Video Diffusion Models](http://arxiv.org/abs/2505.20255) | ArXiv 2025 | [Code](https://github.com/MyNiuuu/AniCrafter) |  | Avatar, Human-Centric Animation |
| 2025 | [Eye-See-You: Reverse Pass-Through VR and Head Avatars](http://arxiv.org/abs/2505.18869) | IJCAI 2025 |  |  | VR, Head Avatars, Pass-Through |
| 2025 | [MAGE:A Multi-stage Avatar Generator with Sparse Observations](http://arxiv.org/abs/2505.06411) | ArXiv 2025 |  |  | Avatar, AR/VR |
| 2025 | [MagicPortrait: Temporally Consistent Face Reenactment with 3D Geometric Guidance](http://arxiv.org/abs/2504.21497) | ArXiv 2025 | [Code](https://github.com/weimengting/MagicPortrait) |  | Latent Diffusion, FLAME, 3D Geometric Guidance, Face Reenactment |
| 2025 | [Supervising 3D Talking Head Avatars with Analysis-by-Audio-Synthesis](http://arxiv.org/abs/2504.13386) | ArXiv 2025 |  | [Project](https://thunder.is.tue.mpg.de/) | 3D, Avatar, Audio-Synthesis |
| 2025 | [EmoDiffusion: Enhancing Emotional 3D Facial Animation with Latent Diffusion Models](http://arxiv.org/abs/2503.11028) | ArXiv 2025 |  | [Project](https://cyk990422.github.io/HoloGest.github.io/) | 3D facial animation, latent diffusion, emotional expression, speech-driven |
| 2025 | [Better Together: Unified Motion Capture and 3D Avatar Reconstruction](http://arxiv.org/abs/2503.09293) | ArXiv 2025 |  |  |  |
| 2025 | [Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](http://arxiv.org/abs/2503.01610) | CVPR 2025 | [Code](https://github.com/MoyGcc/vid2avatar) | [Project](https://moygcc.github.io/vid2avatar-pro/) |  |
| 2025 | [LUCAS: Layered Universal Codec Avatars](http://arxiv.org/abs/2502.19739) | ArXiv 2025 |  |  |  |
| 2025 | [GAS: Generative Avatar Synthesis from a Single Image](http://arxiv.org/abs/2502.06957) | ICCV 2025 | [Code](https://github.com/humansensinglab/GAS) | [Project](https://humansensinglab.github.io/GAS/) | Single Image, 3D Avatar, NeRF, Diffusion |
| 2025 | [MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning](http://arxiv.org/abs/2502.02372) | AAAI 2025 |  |  | NeRF |
| 2025 | [Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](http://arxiv.org/abs/2501.13335) | ArXiv 2025 |  |  | Motion Blur, Animatable Avatars |
| 2025 | [TalkingEyes: Pluralistic Speech-Driven 3D Eye Gaze Animation](https://arxiv.org/abs/2501.09921) | ArXiv 2025 | [Code](https://github.com/LKJKJOIUIU/TalkingEyes) | [Project](https://lkjkjoiuiu.github.io/TalkingEyes_Home) | 3D Eye Gaze, Speech-Driven, Pluralistic |
| 2025 | [Arc2Avatar: Generating Expressive 3D Avatars from a Single Image via ID Guidance](http://arxiv.org/abs/2501.05379) | ArXiv 2025 | [Code](https://github.com/dimgerogiannis/Arc2Avatar) | [Project](https://arc2avatar.github.io/) | Avatars, Single Image |
| 2025 | [Disentangled Clothed Avatar Generation with Layered Representation](http://arxiv.org/abs/2501.04631) | ICCV 2025 (Highlight) | [Code](https://github.com/olivia23333/LayerAvatar) | [Project](https://olivia23333.github.io/LayerAvatar/) |  |
| 2025 | [L3D-Pose: Lifting Pose for 3D Avatars from a Single Camera in the Wild](http://arxiv.org/abs/2501.01174) | ICASSP 2025 |  | [Project](https://soumyaratnadebnath.github.io/L3D-Pose/) |  |
| 2025 | [Barbie: Text to Barbie-Style 3D Avatars](http://arxiv.org/abs/2408.09126) | ArXiv 2025 | [Code](https://github.com/XiaokunSun/Barbie) | [Project](https://xiaokunsun.github.io/Barbie.github.io) | Text to Avatar, Barbie-Style |
| 2025 | [Hybrid Explicit Representation for Ultra-Realistic Head Avatars](http://arxiv.org/abs/2403.11453) | ArXiv 2025 |  |  |  |
| 2024 | [Joint Co-Speech Gesture and Expressive Talking Face Generation using Diffusion with Adapters](http://arxiv.org/abs/2412.14333) | ArXiv 2024 |  |  | Co-speech |
| 2024 | [CAP4D: Creating Animatable 4D Portrait Avatars with Morphable Multi-View Diffusion Models](http://arxiv.org/abs/2412.12093) | ArXiv 2024 | [Code](https://github.com/felixtaubner/cap4d/) | [Project](https://felixtaubner.github.io/cap4d/) | Multi-View Diffusion |
| 2024 | [StrandHead: Text to Strand-Disentangled 3D Head Avatars Using Hair Geometric Priors](http://arxiv.org/abs/2412.11586) | ICCV | [Code](https://github.com/XiaokunSun/StrandHead) | [Project](https://xiaokunsun.github.io/StrandHead.github.io) |  |
| 2024 | [SimAvatar: Simulation-Ready Avatars with Layered Hair and Clothing](http://arxiv.org/abs/2412.09545) | ArXiv 2024 |  | [Project](https://nvlabs.github.io/SimAvatar/) | NVIDIA, Hair and Clothing |
| 2024 | [DynamicAvatars: Accurate Dynamic Facial Avatars Reconstruction and Precise Editing with Diffusion Models](http://arxiv.org/abs/2411.15732) | ArXiv 2024 |  |  |  |
| 2024 | [ConsistentAvatar: Learning to Diffuse Fully Consistent Talking Head Avatar with Temporal Guidance](http://arxiv.org/abs/2411.15436) | ArXiv 2024 | [Code](https://github.com/njust-yang/ConsistentAvatar) | [Project](https://njust-yang.github.io/ConsistentAvatar.github.io/) |  |
| 2024 | [DanceFusion: A Spatio-Temporal Skeleton Diffusion Transformer for Audio-Driven Dance Motion Reconstruction](https://arxiv.org/abs/2411.04646) | ArXiv 2024 |  | [Project](https://th-mlab.github.io/DanceFusion/) |  |
| 2024 | [InstantGeoAvatar: Effective Geometry and Appearance Modeling of Animatable Avatars from Monocular Video](http://arxiv.org/abs/2411.01512) | ACCV 2024 | [Code](https://github.com/alvaro-budria/InstantGeoAvatar) |  |  |
| 2024 | [EgoAvatar: Egocentric View-Driven and Photorealistic Full-body Avatars](http://arxiv.org/abs/2410.01835) | ArXiv 2024 |  |  |  |
| 2024 | [Towards Native Generative Model for 3D Head Avatar](http://arxiv.org/abs/2410.01226) | ArXiv 2024 |  |  |  |
| 2024 | [Stable Video Portraits](http://arxiv.org/abs/2409.18083) | ECCV 2024 |  | [Project](https://svp.is.tue.mpg.de/) | Diffusion |
| 2024 | [LightAvatar: Efficient Head Avatar as Dynamic Neural Light Field](http://arxiv.org/abs/2409.18057) | ECCV'24 CADL | [Code](https://github.com/MingSun-Tse/LightAvatar-TensorFlow) |  |  |
| 2024 | [FreeAvatar: Robust 3D Facial Animation Transfer by Learning an Expression Foundation Model](http://arxiv.org/abs/2409.13180) | ArXiv 2024 |  |  | 3D Facial Animation, Expression Transfer, Foundation Model, Video-driven |
| 2024 | [KMTalk: Speech-Driven 3D Facial Animation with Key Motion Embedding](https://arxiv.org/abs/2409.01113) | ECCV 2024 | [Code](https://github.com/ffxzh/KMTalk) |  | 3D Facial Animation, Key Motion, Speech-Driven |
| 2024 | [Subjective and Objective Quality Assessment of Rendered Human Avatar Videos in Virtual Reality](http://arxiv.org/abs/2408.07041) | IEEE 2024 |  |  |  |
| 2024 | [PAV: Personalized Head Avatar from Unstructured Video Collection](http://arxiv.org/abs/2407.21047) | ECCV 2024 |  | [Project](https://akincaliskan3d.github.io/PAV) |  |
| 2024 | [XHand: Real-time Expressive Hand Avatar](http://arxiv.org/abs/2407.21002) | ArXiv 2024 | [Code](https://github.com/agnJason/XHand) |  | Hand |
| 2024 | [Bridging the Gap: Studio-like Avatar Creation from a Monocular Phone Capture](http://arxiv.org/abs/2407.19593) | ECCV 2024 |  | [Project](http://shahrukhathar.github.io/2024/07/22/Bridging.html) |  |
| 2024 | [Universal Facial Encoding of Codec Avatars from VR Headsets](http://arxiv.org/abs/2407.13038) | SIGGRAPH 2024 |  |  | Facial Encoding, VR Headset, Real-time Animation, 3D Avatar |
| 2024 | [CanonicalFusion: Generating Drivable 3D Human Avatars from Multiple Images](http://arxiv.org/abs/2407.04345) | ECCV 2024 | [Code](https://github.com/jsshin98/CanonicalFusion) |  |  |
| 2024 | [WildAvatar: Web-scale In-the-wild Video Dataset for 3D Avatar Creation](http://arxiv.org/abs/2407.02165) | ArXiv 2024 | [Code](https://github.com/wildavatar/WildAvatar_Toolbox) | [Project](https://wildavatar.github.io) | Dataset |
| 2024 | [AniFaceDiff: Animating Stylized Avatars via Parametric Conditioned Diffusion Models](http://arxiv.org/abs/2406.13272) | ArXiv 2024 |  |  |  |
| 2024 | [Human-3Diffusion: Realistic Avatar Creation via Explicit 3D Consistent Diffusion Models](http://arxiv.org/abs/2406.08475) | NIPS 2024 | [Code](https://github.com/YuxuanSnow/Human3Diffusion) | [Project](https://yuxuan-xue.com/human-3diffusion/) | Diffusion |
| 2024 | [Instant 3D Human Avatar Generation using Image Diffusion Models](http://arxiv.org/abs/2406.07516) | ArXiv 2024 |  | [Project](https://www.nikoskolot.com/avatarpopup/) |  |
| 2024 | [Representing Animatable Avatar via Factorized Neural Fields](http://arxiv.org/abs/2406.00637) | ArXiv 2024 |  |  |  |
| 2024 | [Stratified Avatar Generation from Sparse Observations](http://arxiv.org/abs/2405.20786) | CVPR 2024 (Oral) |  |  |  |
| 2024 | [E3Gen: Efficient, Expressive and Editable Avatars Generation](http://arxiv.org/abs/2405.19203) | ArXiv 2024 | [Code](https://github.com/olivia23333/E3Gen) | [Project](https://olivia23333.github.io/E3Gen) |  |
| 2024 | [X-Oscar: A Progressive Framework for High-quality Text-guided 3D Animatable Avatar Generation](http://arxiv.org/abs/2405.00954) | ICML 2024 | [Code](https://github.com/LinZhekai/X-Oscar) | [Project](https://xmu-xiaoma666.github.io/Projects/X-Oscar/) |  |
| 2024 | [GeneAvatar: Generic Expression-Aware Volumetric Head Avatar Editing from a Single Image](https://arxiv.org/abs/2404.02152) | CVPR 2024 | [Code](https://github.com/zju3dv/GeneAvatar) | [Project](https://zju3dv.github.io/geneavatar/) | Editing |
| 2024 | [Efficient 3D Implicit Head Avatar with Mesh-anchored Hash Table Blendshapes](http://arxiv.org/abs/2404.01543) | CVPR 2024 |  | [Project](https://augmentedperception.github.io/monoavatar-plus/) | Blendshapes |
| 2024 | [MagicMirror: Fast and High-Quality Avatar Generation with a Constrained Search Space](https://arxiv.org/abs/2404.01296) | ArXiv 2024 |  | [Project](https://syntec-research.github.io/MagicMirror/) |  |
| 2024 | [MI-NeRF: Learning a Single Face NeRF from Multiple Identities](https://arxiv.org/abs/2403.19920) | ArXiv 2024 |  | [Project](https://aggelinacha.github.io/MI-NeRF/) | NeRF, Multi-Identity, Face Modeling |
| 2024 | [NECA: Neural Customizable Human Avatar](http://arxiv.org/abs/2403.10335) | CVPR 2024 | [Code](https://github.com/iSEE-Laboratory/NECA) |  |  |
| 2024 | [Magic-Me: Identity-Specific Video Customized Diffusion](http://arxiv.org/abs/2402.09368) | ArXiv 2024 | [Code](https://github.com/Zhen-Dong/Magic-Me) | [Project](https://magic-me-webpage.github.io/) |  |
| 2024 | [ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields](http://arxiv.org/abs/2402.00864) | NIPS 2023 | [Code](https://github.com/Dongjiahua/VICA-NeRF) | [Project](https://dongjiahua.github.io/VICA-NeRF/) | 3D Edit |
| 2024 | [Sketch2NeRF: Multi-view Sketch-guided Text-to-3D Generation](http://arxiv.org/abs/2401.14257) | ArXiv 2024 |  |  | Text to 3D |
| 2024 | [UltrAvatar: A Realistic Animatable 3D Avatar Diffusion Model with Authenticity Guided Textures](http://arxiv.org/abs/2401.11078) | ArXiv 2024 |  | [Project](http://usrc-sea.github.io/UltrAvatar/) | Diffusion, Avatar |
| 2024 | [High-Quality Mesh Blendshape Generation from Face Videos via Neural Inverse Rendering](https://arxiv.org/abs/2401.08398) | ArXiv 2024 | [Code](https://github.com/grignarder/high-quality-blendshape-generation) |  | mesh blendshape, neural inverse rendering, face reconstruction |
| 2024 | [FED-NeRF: Achieve High 3D Consistency and Temporal Coherence for Face Video Editing on Dynamic NeRF](http://arxiv.org/abs/2401.02616) | ArXiv 2024 | [Code](https://github.com/ZHANG1023/FED-NeRF) |  | 4D face video editor |
| 2024 | [Learning Dense Correspondence for NeRF-Based Face Reenactment](http://arxiv.org/abs/2312.10422) | AAAI 2024 |  |  | one-shot multi-view face reenactmen |
| 2024 | [VAST: Vivify Your Talking Avatar via Zero-Shot Expressive Facial Style Transfer](http://arxiv.org/abs/2308.04830) | ICCV2023 |  |  |  |
| 2024 | [AvatarPose: Avatar-guided 3D Pose Estimation of Close Human Interaction from Sparse Multi-view Videos](https://feichilu.github.io/AvatarPose/assets/paper.pdf) | ECCV 2024 | [Code](https://github.com/feichilu/AvatarPose) | [Project](https://feichilu.github.io/AvatarPose/) |  |
| 2024 | [What You See Is What You GAN: Rendering Every Pixel for High-Fidelity Geometry in 3D GANs](https://research.nvidia.com/labs/nxp/wysiwyg/media/WYSIWYG.pdf) | ArXiv 2024 |  | [Project](https://research.nvidia.com/labs/nxp/wysiwyg/) |  |
| 2023 | [INFAMOUS-NeRF: ImproviNg FAce MOdeling Using Semantically-Aligned Hypernetworks with Neural Radiance Fields](https://arxiv.org/abs/2312.16197) | ArXiv 2023 |  |  | NeRF, Face Modeling, Hypernetworks, Semantically-Aligned |
| 2023 | [AvatarStudio: High-fidelity and Animatable 3D Avatar Creation from Text](http://arxiv.org/abs/2311.17917) | ArXiv 2023 |  | [Project](http://jeff95.me/projects/avatarstudio.html) | Text-to-3D, NeRF, SMPL, Diffusion Model |
| 2023 | [3D Face Style Transfer with a Hybrid Solution of NeRF and Mesh Rasterization](https://arxiv.org/abs/2311.13168) | ArXiv 2023 |  |  | 3D Face, Style Transfer, NeRF, Mesh |
| 2023 | [HAvatar: High-fidelity Head Avatar via Facial Model Conditioned Neural Radiance Field](http://arxiv.org/abs/2309.17128) | ArXiv 2023 |  |  | Neural Radiance Field, Facial Model Conditioning, 3D Head Avatar, Expression Control |
| 2023 | [NOFA: NeRF-based One-shot Facial Avatar Reconstruction](https://arxiv.org/abs/2307.03441) | ArXiv 2023 |  |  | NeRF, One-shot, Facial Avatar |
| 2023 | [Instruct-NeuralTalker: Editing Audio-Driven Talking Radiance Fields with Instructions](https://arxiv.org/abs/2306.10813) | ArXiv 2023 |  |  |  |
| 2023 | [MA-NeRF: Motion-Assisted Neural Radiance Fields for Face Synthesis from Sparse Images](https://arxiv.org/abs/2306.10350) | ArXiv 2023 |  |  | NeRF, Motion-Assisted, Face Synthesis |
| 2023 | [GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation](https://arxiv.org/abs/2305.00787) | ArXiv 2023 | [Code](https://github.com/yerfor/GeneFacePlusPlus) | [Project](https://genefaceplusplus.github.io/) | - |
| 2023 | [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](https://arxiv.org/abs/2301.13430) | ICLR 2023 | [Code](https://github.com/yerfor/GeneFace) | [Project](https://geneface.github.io/) | - |
| 2023 | [SD-NeRF: Towards Lifelike Talking Head Animation via Spatially-adaptive Dual-driven NeRFs](https://ieeexplore.ieee.org/document/10229247) | IEEE 2023 |  |  |  |
| 2022 | [NeRFInvertor: High Fidelity NeRF-GAN Inversion for Single-shot Real Image Animation](https://arxiv.org/abs/2211.17235.pdf) | ArXiv 2022 | [Code](https://github.com/YuYin1/NeRFInvertor) | [Project](https://yuyin1.github.io/NeRFInvertor_Homepage/) | - |
| 2022 | [RAD-NeRF: Real-time Neural Talking Portrait Synthesis](https://arxiv.org/abs/2211.12368.pdf) | ArXiv 2022 | [Code](https://github.com/ashawkey/RAD-NeRF) | [Project](https://ashawkey.github.io/radnerf/) | InstantNGP |
| 2022 | [Next3D: Generative Neural Texture Rasterization for 3D-Aware Head Avatars](https://arxiv.org/abs/2211.11208.pdf) | ArXiv 2022 | [Code](https://mrtornado24.github.io/Next3D/) | [Project](https://mrtornado24.github.io/Next3D/) | - |
| 2022 | [FNeVR: Neural Volume Rendering for Face Animation](https://arxiv.org/abs/2209.10340) | ArXiv 2022 | [Code](https://github.com/zengbohan0217/FNeVR) |  | - |
| 2022 | [3DFaceShop: Explicitly Controllable 3D-Aware Portrait Generation](https://arxiv.org/abs/2209.05434) | ArXiv 2022 | [Code](https://github.com/junshutang/3DFaceShop) | [Project](https://junshutang.github.io/control/index.html) | - |
| 2022 | [DFRF：Learning Dynamic Facial Radiance Fields for Few-Shot Talking Head Synthesis](https://arxiv.org/abs/2207.11770) | ECCV 2022 | [Code](https://github.com/sstzal/DFRF) | [Project](https://sstzal.github.io/DFRF/) |  |
| 2022 | [ROME: Realistic One-shot Mesh-based Head Avatars](https://arxiv.org/abs/2206.08343.pdf) | ECCV 2022 | [Code](https://github.com/SamsungLabs/rome) | [Project](https://samsunglabs.github.io/rome/) | - |
| 2022 | [Semantic-Aware Implicit Neural Audio-Driven Video Portrait Generation](https://arxiv.org/abs/2201.07786.pdf) | ArXiv 2022 | [Code](https://github.com/alvinliu0/SSP-NeRF) | [Project](https://alvinliu0.github.io/projects/SSP-NeRF) | - |
| 2022 | [IMavatar: Implicit Morphable Head Avatars from Videos](https://openaccess.thecvf.com/content/CVPR2022/papers/Zheng_I_M_Avatar_Implicit_Morphable_Head_Avatars_From_Videos_CVPR_2022_paper.pdf) | CVPR 2022 | [Code](https://ait.ethz.ch/projects/2022/IMavatar/) | [Project](https://ait.ethz.ch/projects/2022/IMavatar/) | - |
| 2022 | [HeadNeRF: A Real-time NeRF-based Parametric Head Model](https://openaccess.thecvf.com/content/CVPR2022/papers/Grassal_Neural_Head_Avatars_From_Monocular_RGB_Videos_CVPR_2022_paper.pdf) | CVPR 2022 | [Code](https://github.com/CrisHY1995/headnerf) | [Project](https://hy1995.top/HeadNeRF-Project/) | - |
| 2021 | [DFA-NeRF: Personalized Talking Head Generation via Disentangled Face Attributes Neural Rendering](https://arxiv.org/abs/2201.00791.pdf) | ArXiv 2021 | [Code](https://github.com/ShunyuYao/DFA-NeRF) |  | - |
| 2021 | [AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis](https://arxiv.org/abs/2103.11078) | ICCV 2021 | [Code](https://github.com/YudongGuo/AD-NeRF) | [Project](https://yudongguo.github.io/ADNeRF/) | - |
| 2021 | [NerFACE: Dynamic Neural Radiance Fields for Monocular 4D Facial Avatar Reconstruction](https://arxiv.org/abs/2012.03065) | CVPR 2021 Oral | [Code](https://github.com/gafniguy/4D-Facial-Avatars) | [Project](https://gafniguy.github.io/4D-Facial-Avatars/) | - |

---



## 3D Gaussian Splatting

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [F3G-Avatar : Face Focused Full-body Gaussian Avatar](https://arxiv.org/abs/2604.09835) | CVPRW 2026 | [Code](https://github.com/wjmenu/F3G-avatar) |  | full-body avatar, face-focused, gaussian splatting, multi-view |
| 2026 | [Structure-Aware Fine-Grained Gaussian Splatting for Expressive Avatar Reconstruction](https://arxiv.org/abs/2604.09324) | ArXiv 2026 | [Code](https://github.com/Su245811YZ/SFGS) |  | fine-grained, structure-aware, gaussian splatting, expressive avatar |
| 2026 | [PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467) | CVPR 2026 |  | [Project](https://phys-head.github.io) | 3D Gaussian, Head Avatar, Physics Simulation |
| 2026 | [AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787) | CVPR 2026 | [Code](https://github.com/KumapowerLIU/AvatarPointillist) | [Project](https://kumapowerliu.github.io/AvatarPointillist/) | 4D Gaussian, Autoregressive, Avatar |
| 2026 | [Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars](https://arxiv.org/abs/2604.01447) | ArXiv 2026 | [Code](https://github.com/dcaustin33/better_rigs_not_bigger_networks) |  | Body Model, Gaussian Avatars, Ablation |
| 2026 | [Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928) | ArXiv 2026 |  | [Project](https://steimich96.github.io/AAP-3DGA/) | 3D Gaussian, Autoregressive, Appearance Prediction |
| 2026 | [DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003) | ArXiv 2026 |  |  | 3D Head Avatar, Gaussian Splatting, Monocular Video, Personalized |
| 2026 | [FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar](https://arxiv.org/abs/2603.23345) | ArXiv 2026 |  |  | Face-and-Hair Avatar, 3D Gaussian, Composable Reconstruction |
| 2026 | [ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2603.16447) | CVPR 2026 |  | [Project](https://ustc3dv.github.io/ProgressiveAvatars/) | 3D Gaussian, Progressive, Animatable Avatars |
| 2026 | [Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811) | ArXiv 2026 |  | [Project](https://malteprinzler.github.io/projects/match) | Gaussian Registration, Head Avatar, Feed-forward |
| 2026 | [Retrieval-Augmented Gaussian Avatars: Improving Expression Generalization](http://arxiv.org/abs/2603.08645) | ArXiv 2026 |  |  | Gaussian Splatting, Expression Generalization, Retrieval Augmentation, 3D Avatars |
| 2026 | [Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On](https://arxiv.org/abs/2603.04290) | 3DV 2026 | [Code](https://github.com/eth-ait/GaussianWardrobe) | [Project](https://eth-ait.github.io/GaussianWardrobe/) | 3D Gaussian, Compositional Avatar, Virtual Try-On |
| 2026 | [LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](http://arxiv.org/abs/2603.02129) | ArXiv 2026 |  |  | Kinematic-Space Completion, Expression Control, 3D Gaussian Splatting, Video Diffusion |
| 2026 | [OMG-Avatar: One-shot Multi-LOD Gaussian Head Avatar](http://arxiv.org/abs/2603.01506) | ArXiv 2026 |  | [Project](https://human3daigc.github.io/OMGAvatar_project_page/) | 3D Gaussian, One-Shot, Head Avatar |
| 2026 | [GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](http://arxiv.org/abs/2602.24161) | ArXiv 2026 | [Code](https://github.com/lyxcc127/GeoDiff4D) | [Project](https://lyxcc127.github.io/geodiff4d) | Geometry-Aware Diffusion, 4D Avatar Reconstruction, 3D Gaussian Splatting, Surface Normals |
| 2026 | [OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](http://arxiv.org/abs/2602.11693) | ArXiv 2026 |  | [Project](https://omega-avatar.github.io/OMEGA-Avatar/) | One-Shot Avatar, 360° Full-Head, 3D Gaussian Splatting, Multi-View Feature Splatting |
| 2026 | [OFERA: Blendshape-driven 3D Gaussian Control for Occluded Facial Expression to Realistic Avatars in VR](http://arxiv.org/abs/2602.01748) | ArXiv 2026 | [Code](https://github.com/ysshwan147/OFERA) | [Project](https://ysshwan147.github.io/projects/ofera/) | Blendshape Control, Gaussian Avatars, VR Telepresence, Real-time Expression |
| 2026 | [VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674) | ArXiv 2026 | [Code](https://github.com/hailsong/VRGaussianAvatar) | [Project](https://vrgaussianavatar.github.io) | 3D Gaussian, VR Avatar, Integration |
| 2026 | [The Gaussian-Head OFL Family: One-Shot Federated Learning from Client Global Statistics](https://arxiv.org/abs/2602.01186) | the International Conference on Learning Representations (ICLR) 2026 |  |  | Gaussian-Head, Federated Learning, One-Shot |
| 2026 | [Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting](https://arxiv.org/abs/2601.18633) | ArXiv 2026 | [Code](https://github.com/stonewalking/Splat-portrait) | [Project](https://github.com/stonewalking/Splat-portrait) | Gaussian Splatting, 3DGS, Portrait Animation, Talking Head |
| 2026 | [GlassesGB: Controllable 2D GAN-Based Eyewear Personalization for 3D Gaussian Blendshapes Head Avatars](https://arxiv.org/abs/2601.17088) | IEEE VR 2026 |  | [Project](https://ruiyangju.github.io/GlassesGB) | gaussian blendshapes, virtual try-on, eyewear, head avatar |
| 2026 | [CAG-Avatar: Cross-Attention Guided Gaussian Avatars for High-Fidelity Head Reconstruction](http://arxiv.org/abs/2601.14844) | ArXiv 2026 |  |  | 3D Gaussian Splatting, cross-attention, head reconstruction, drivable avatars |
| 2026 | [FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation](http://arxiv.org/abs/2601.13837) | ICLR 2026 |  |  | 3D Gaussian Splatting, Head Avatars, Real-Time Animation, Few-Shot Learning |
| 2026 | [Generalizable and Animatable 3D Full-Head Gaussian Avatar from a Single Image](http://arxiv.org/abs/2601.12770) | ArXiv 2026 | [Code](https://github.com/ShaelynZ/fhavatar) | [Project](https://shaelynz.github.io/fhavatar) | 3D full-head avatar, Gaussian primitives, UV space, single-image reconstruction |
| 2026 | [ELITE: Efficient Gaussian Head Avatar from a Monocular Video via Learned Initialization and TEst-time Generative Adaptation](http://arxiv.org/abs/2601.10200) | ArXiv 2026 | [Code](https://github.com/kaist-ami/elite) | [Project](https://kim-youwang.github.io/elite) | Gaussian Avatar, Test-time Adaptation, Diffusion, Monocular Video |
| 2026 | [UIKA: Fast Universal Head Avatar from Pose-Free Images](http://arxiv.org/abs/2601.07603) | ArXiv 2026 | [Code](https://github.com/Zijian-Wu/uika) | [Project](https://zijian-wu.github.io/uika-page/) | Gaussian Splatting, UV Mapping, Head Avatar, Feed-forward |
| 2026 | [LayerGS: Decomposition and Inpainting of Layered 3D Human Avatars via 2D Gaussian Splatting](https://arxiv.org/abs/2601.05853) | ArXiv 2026 | [Code](https://github.com/RockyXu66/LayerGS) |  | 2D Gaussian Splatting, Layered Avatar, Decomposition |
| 2026 | [GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511) | ArXiv 2026 |  |  | 3D Gaussian Splatting, Face Swapping, Animatable |
| 2026 | [RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](http://arxiv.org/abs/2601.03357) | ArXiv 2026 |  |  | 3D Gaussian Splatting, relightable avatars, single-image fitting, cross-subject generalization |
| 2026 | [CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature](https://arxiv.org/abs/2601.03319) | ArXiv 2026 | [Code](https://github.com/eldad929/caricatureGS) | [Project](https://c4ricaturegs.github.io) | 3D Gaussian Splatting, Caricature, Gaussian Curvature |
| 2026 | [GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](http://arxiv.org/abs/2512.09162) | Eurographics 2026 | [Code](https://github.com/KelianB/GTAvatar) | [Project](https://kelianb.github.io/GTAvatar) | Gaussian Splatting, Texture Mapping, Relightable Avatars, 3D Reconstruction |
| 2026 | [STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](http://arxiv.org/abs/2511.19854) | CVPR 2026 | [Code](https://github.com/LCFAW/STAvatar) | [Project](https://jiankuozhao.github.io/STAvatar) | Gaussian Splatting, 3D Head Avatars, Soft Binding, Temporal Density Control |
| 2025 | [TexAvatars: Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars](http://arxiv.org/abs/2512.21099) | ArXiv 2025 | [Code](https://github.com/summertight/TexAvatars_repo) | [Project](https://summertight.github.io/TexAvatars) | 3D Gaussian Splatting, hybrid representation, analytic rigging, UV space |
| 2025 | [FlexAvatar: Flexible Large Reconstruction Model for Animatable Gaussian Head Avatars with Detailed Deformation](http://arxiv.org/abs/2512.17717) | ArXiv 2025 |  | [Project](https://pengc02.github.io/flexavatar) | 3D avatar, Gaussian Splatting, deformation, reconstruction |
| 2025 | [Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893) | ArXiv 2025 |  |  | 3D, Gaussian Splatting, Avatar, Attention |
| 2025 | [Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](http://arxiv.org/abs/2512.15711) | Tech Report 2025 |  |  | Gaussian Splatting, head avatar, hybrid representation, efficient rendering |
| 2025 | [AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars](http://arxiv.org/abs/2512.06438) | ArXiv 2025 | [Code](https://github.com/ramazan793/agora) | [Project](https://ramazan793.github.io/AGORA/) | 3D Gaussian Splatting, Animatable Avatars, FLAME, Real-time Rendering |
| 2025 | [EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head](https://arxiv.org/abs/2512.05991) | ArXiv 2025 |  |  | 3D, Diffusion, Emotional, Talking Head |
| 2025 | [AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827) | ArXiv 2025 | [Code](https://github.com/miraymen/aha_codebase) | [Project](https://miraymen.github.io/aha/) | Gaussian Splatting, Human Avatar, Scene Animation |
| 2025 | [Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks](http://arxiv.org/abs/2511.02830) | ArXiv 2025 | [Code](https://github.com/diddone/densemarks) | [Project](https://diddone.github.io/densemarks/) | Head Correspondence, Canonical Embedding, Tracking, Avatar |
| 2025 | [STG-Avatar: Animatable Human Avatars via Spacetime Gaussian](http://arxiv.org/abs/2510.22140) | IROS 2025 | [Code](https://github.com/jiangguangan/STG-Avatar) | [Project](https://github.com/jiangguangan/STG-Avatar) | Spacetime Gaussian, Animatable Avatar, 3DGS |
| 2025 | [Capture, Canonicalize, Splat: Zero-Shot 3D Gaussian Avatars from Unstructured Phone Images](http://arxiv.org/abs/2510.14081) | ICCV 2025 |  |  | Zero-Shot, 3D Gaussian Avatars, Phone Images |
| 2025 | [Instant Skinned Gaussian Avatars for Web, Mobile and VR Applications](http://arxiv.org/abs/2510.13978) | SUI 2025 | [Code](https://github.com/naruya/gaussian-vrm) | [Project](https://gaussian-vrm.github.io/) | Real-Time, Cross-Platform, 3D Avatar, Gaussian Splatting |
| 2025 | [Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided Framework](http://arxiv.org/abs/2510.10492) | ArXiv 2025 |  |  | 3D Gaussian, Human Avatar, Compression |
| 2025 | [ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars](http://arxiv.org/abs/2510.05488) | ArXiv 2025 |  |  | 3D Gaussian Head Avatars, Level of Detail Control, Continuous LOD |
| 2025 | [MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust Physics-Based Dynamics](http://arxiv.org/abs/2510.01619) | NeurIPS 2025 | [Code](https://github.com/KAISTChangmin/MPMAvatar) | [Project](https://KAISTChangmin.github.io/MPMAvatar/) | Physics-Based, 3DGS, Garments |
| 2025 | [FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction](https://arxiv.org/abs/2509.14739) | ArXiv 2025 |  |  | 2D Gaussian, Mesh-Guided, Avatar |
| 2025 | [Dream3DAvatar: Text-Controlled 3D Avatar Reconstruction from a Single Image](http://arxiv.org/abs/2509.13013) | ArXiv 2025 |  |  | Text-Driven, Single Image, 3DGS |
| 2025 | [PanoLAM: Large Avatar Model for Gaussian Full-Head Synthesis from One-shot Unposed Image](http://arxiv.org/abs/2509.07552) | ArXiv 2025 |  | [Project](https://panolam.github.io/) | Gaussian, Full-Head Synthesis, One-shot |
| 2025 | [GaussianGAN: Real-Time Photorealistic controllable Human Avatars](http://arxiv.org/abs/2509.01681) | FG 2025 |  |  | 3DGS, Real-Time, Photorealistic |
| 2025 | [Im2Haircut: Single-view Strand-based Hair Reconstruction for Human   Avatars](http://arxiv.org/abs/2509.01469) | ArXiv 2025 | [Code](https://github.com/Vanessik/Im2Haircut) | [Project](https://im2haircut.is.tue.mpg.de) | Hair Reconstruction, Gaussian Splatting |
| 2025 | [AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View Images](http://arxiv.org/abs/2508.20623) | ArXiv 2025 |  |  | 3D Gaussian Splatting, Back-Head Generation, Avatar Reconstruction, Spatial Alignment |
| 2025 | [FastAvatar: Instant 3D Gaussian Splatting for Faces from Single Unconstrained Poses](https://arxiv.org/abs/2508.18389) | ArXiv 2025 | [Code](https://github.com/hliang2/FastAvatar) | [Project](https://hliang2.github.io/FastAvatar) | 3DGS, Instant, Single Image |
| 2025 | [EAvatar: Expression-Aware Head Avatar Reconstruction with Generative Geometry Priors](http://arxiv.org/abs/2508.13537) | ArXiv 2025 |  |  | 3D Gaussian Splatting, expression-aware, deformation-aware, generative priors |
| 2025 | [SVG-Head: Hybrid Surface-Volumetric Gaussians for High-Fidelity Head Reconstruction and Real-Time Editing](http://arxiv.org/abs/2508.09597) | ArXiv 2025 | [Code](https://github.com/heyy-sun/SVG-Head) | [Project](https://heyy-sun.github.io/SVG-Head) | Gaussian Splatting, 3D Avatar, Texture Editing, FLAME |
| 2025 | [MoGaFace: Momentum-Guided and Texture-Aware Gaussian Avatars for Consistent Facial Geometry](http://arxiv.org/abs/2508.01218) | ArXiv 2025 |  |  | Gaussian Avatars, FLAME Meshes, Geometry Refinement |
| 2025 | [MoGA: 3D Generative Avatar Prior for Monocular Gaussian Avatar Reconstruction](http://arxiv.org/abs/2507.23597) | ICCV 2025 | [Code](https://github.com/zj-dong/MoGA) | [Project](https://zj-dong.github.io/MoGA/) | 3D Generative Avatar, Monocular Reconstruction |
| 2025 | [HairCUP: Hair Compositional Universal Prior for 3D Gaussian Avatars](http://arxiv.org/abs/2507.19481) | ArXiv 2025 |  | [Project](https://bjkim95.github.io/haircup) | 3D Gaussian Avatars, Hair Compositionality, Disentangled Prior, Few-shot Fine-tuning |
| 2025 | [GeoAvatar: Adaptive Geometrical Gaussian Splatting for 3D Head Avatar](http://arxiv.org/abs/2507.18155) | ArXiv 2025 | [Code](https://github.com/seungjun-moon/geoavatar) | [Project](https://hahminlew.github.io/geoavatar) | Adaptive Gaussian Splatting, 3D Head Avatar, Mouth Structure, Deformation Strategy |
| 2025 | [StreamME: Simplify 3D Gaussian Avatar within Live Stream](http://arxiv.org/abs/2507.17029) | ArXiv 2025 | [Code](https://github.com/Songluchuan/StreamMEcode) | [Project](https://songluchuan.github.io/StreamME/) | 3D Gaussian Splatting, avatar reconstruction, on-the-fly training |
| 2025 | [ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](http://arxiv.org/abs/2507.10542) | SIGGRAPH 2025 |  | [Project](https://shivangi-aneja.github.io/projects/scaffoldavatar/) | High-Fidelity, Gaussian Avatars, Patch Expressions |
| 2025 | [HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity Animatable Face Avatars](http://arxiv.org/abs/2507.02803) | ArXiv 2025 | [Code](https://github.com/gserifi/HyperGaussians) | [Project](https://gserifi.github.io/HyperGaussians) | High-Dimensional, Gaussian Splatting |
| 2025 | [BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](http://arxiv.org/abs/2506.06271) | ArXiv 2025 | [Code](https://github.com/jonathsch/becominglit) | [Project](https://jonathsch.github.io/becominglit/) | 3DGS, Relightable, Neural Shading |
| 2025 | [EVA: Expressive Virtual Avatars from Multi-view Videos](http://arxiv.org/abs/2505.15385) | SIGGRAPH 2025 |  | [Project](https://vcai.mpi-inf.mpg.de/projects/EVA/) | Avatar, 3D Gaussian |
| 2025 | [ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072) | IEEE VR 2026 | [Code](https://github.com/RuiyangJu/ToonifyGB) | [Project](https://ruiyangju.github.io/ToonifyGB) | gaussian blendshapes, stylization, toonify, head avatar |
| 2025 | [TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head   Modeling](http://arxiv.org/abs/2505.05672) | SIGGRAPH 2025 |  | [Project](https://syntec-research.github.io/UVGA/) | 3DGS, Avatar, High-Resolution |
| 2025 | [SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with   Video Diffusion and Data Augmentation](http://arxiv.org/abs/2505.05475) | CVPRW 2025 | [Code](https://github.com/yc4ny/SVAD) | [Project](https://yc4ny.github.io/SVAD/) | Single Image, 3D Avatar, 3DGS, Video Diffusion |
| 2025 | [GUAVA: Generalizable Upper Body 3D Gaussian Avatar](http://arxiv.org/abs/2505.03351) | ICCV 2025 | [Code](eastbeanzhang.github.io/GUAVA/) | [Project](https://eastbeanzhang.github.io/GUAVA/) | 3D Gaussian Avatar, Upper Body, SMPLX |
| 2025 | [DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar   Relighting](http://arxiv.org/abs/2504.10486) | ICCV 2025 | [Code](https://github.com/jzr99/DNF-Avatar) | [Project](https://jzr99.github.io/DNF-Avatar/) | Relightable Avatar, 2DGS Distillation |
| 2025 | [TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](http://arxiv.org/abs/2503.17032) | CVPR 2025(Highlight🚀) |  | [Project](https://pixelai-team.github.io/TaoAvatar/) | AR |
| 2025 | [RGBAvatar: Reduced Gaussian Blendshapes for Online Modeling of Head Avatars](https://arxiv.org/abs/2503.12886) | ArXiv 2025 | [Code](https://github.com/gapszju/RGBAvatar) |  | gaussian blendshapes, real-time, compact, animatable |
| 2025 | [2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](http://arxiv.org/abs/2503.02452) | ICVRV 2024 |  |  | 2DGS |
| 2025 | [Avat3r: Large Animatable Gaussian Reconstruction Model for High-fidelity 3D Head Avatars](http://arxiv.org/abs/2502.20220) | ArXiv 2025 |  | [Project](https://tobias-kirschstein.github.io/avat3r/) |  |
| 2025 | [LAM: Large Avatar Model for One-shot Animatable Gaussian Head](http://arxiv.org/abs/2502.17796) | ArXiv 2025 | [Code](https://github.com/lam-avatar/lam) | [Project](https://lam-avatar.github.io/lam/) |  |
| 2025 | [Relightable Full-Body Gaussian Codec Avatars](http://arxiv.org/abs/2501.14726) | ArXiv 2025 |  | [Project](https://neuralbodies.github.io/RFGCA) | Full-Body, Avatars |
| 2025 | [PERSE: Personalized 3D Generative Avatars from A Single Portrait](http://arxiv.org/abs/2412.21206) | CVPR 2025 | [Code](https://github.com/snuvclab/perse) | [Project](https://hyunsoocha.github.io/perse/) | Personalized, 3DGS, Single Image |
| 2025 | [Generating Editable Head Avatars with 3D Gaussian GANs](http://arxiv.org/abs/2412.19149) | ArXiv 2025 | [Code](https://github.com/liguohao96/EGG3D) | [Project](https://liguohao96.github.io/EGG3D/) | 3DGS |
| 2025 | [FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D   Reconstruction](http://arxiv.org/abs/2412.09573) | ArXiv 2025 |  | [Project](https://bluestyle97.github.io/projects/freesplatter/) | Pose-free, Sparse-view, 3DGS |
| 2025 | [Interactive Rendering of Relightable and Animatable Gaussian Avatars](http://arxiv.org/abs/2407.10707) | ArXiv 2025 | [Code](https://github.com/1231234zhan/InteractRAGA) | [Project](https://gapszju.github.io/InteractRAGA) | Gaussian Splatting, Relightable Avatars, Interactive Rendering, Pose-driven Animation |
| 2024 | [GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](http://arxiv.org/abs/2412.13983) | AAAI 2025 | [Code](https://github.com/ucwxb/GraphAvatar) |  | GNN-Generated, 3DGS |
| 2024 | [3D$^2$-Actor: Learning Pose-Conditioned 3D-Aware Denoiser for Realistic Gaussian Avatar Modeling](http://arxiv.org/abs/2412.11599) | AAAI 2025 | [Code](https://github.com/silence-tang/GaussianActor) | [Project](https://github.com/silence-tang/GaussianActor) | 3DGS |
| 2024 | [GAF: Gaussian Avatar Reconstruction from Monocular Videos via Multi-view Diffusion](http://arxiv.org/abs/2412.10209) | ArXiv 2024 | [Code](https://github.com/tangjiapeng/GAF) | [Project](https://tangjiapeng.github.io/projects/GAF) | Diffusion |
| 2024 | [GASP: Gaussian Avatars with Synthetic Priors](http://arxiv.org/abs/2412.07739) | ArXiv 2024 |  | [Project](https://microsoft.github.io/GASP/) |  |
| 2024 | [MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](http://arxiv.org/abs/2412.04955) | ArXiv 2024 |  | [Project](https://chenvoid.github.io/MGA/) | 3DGS, 2D-3D |
| 2024 | [PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](http://arxiv.org/abs/2412.04433) | ArXiv 2024 |  |  | Clothed Avatar |
| 2024 | [GAST: Sequential Gaussian Avatars with Hierarchical Spatio-temporal Context](http://arxiv.org/abs/2411.16768) | ArXiv 2024 | [Code](https://github.com/zezeaaa/SeqAvatar) | [Project](https://zezeaaa.github.io/projects/SeqAvatar) |  |
| 2024 | [Bundle Adjusted Gaussian Avatars Deblurring](http://arxiv.org/abs/2411.16758) | CVPR | [Code](https://github.com/MyNiuuu/BAGA) |  |  |
| 2024 | [FATE: Full-head Gaussian Avatar with Textural Editing from Monocular Video](http://arxiv.org/abs/2411.15604) | CVPR | [Code](https://github.com/zjwfufu/FateAvatar) | [Project](https://zjwfufu.github.io/FATE-page/) |  |
| 2024 | [DAGSM: Disentangled Avatar Generation with GS-enhanced Mesh](http://arxiv.org/abs/2411.15205) | CVPR |  |  |  |
| 2024 | [DreamWaltz-G: Expressive 3D Gaussian Avatars from Skeleton-Guided 2D Diffusion](http://arxiv.org/abs/2409.17145) | ArXiv 2024 | [Code](https://github.com/yukun-huang/DreamWaltz-G) | [Project](https://yukun-huang.github.io/DreamWaltz-G/) |  |
| 2024 | [Gaussian Déjà-vu: Creating Controllable 3D Gaussian Head-Avatars with Enhanced Generalization and Personalization Abilities](http://arxiv.org/abs/2409.16147) | WACV 2025 | [Code](https://github.com/PeizhiYan/gaussian-dejavu) | [Project](https://peizhiyan.github.io/docs/dejavu/) |  |
| 2024 | [GaussianHeads: End-to-End Learning of Drivable Gaussian Head Avatars from Coarse-to-fine Representations](http://arxiv.org/abs/2409.11951) | SIGGRAPH Asia 2024 | [Code](https://github.com/Kartik-Teotia/GaussianHeads) | [Project](https://vcai.mpi-inf.mpg.de/projects/GaussianHeads/) | 🔥Gaussian Splatting |
| 2024 | [DEGAS: Detailed Expressions on Full-Body Gaussian Avatars](http://arxiv.org/abs/2408.10588) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [Topology-aware Human Avatars with Semantically-guided Gaussian Splatting](http://arxiv.org/abs/2408.09665) | ArXiv 2024 |  |  |  |
| 2024 | [CHASE: 3D-Consistent Human Avatars with Sparse Inputs via Gaussian Splatting and Contrastive Learning](http://arxiv.org/abs/2408.09663) | ArXiv 2024 |  |  |  |
| 2024 | [Expressive Whole-Body 3D Gaussian Avatar](http://arxiv.org/abs/2407.21686) | ECCV 2024 | [Code](https://github.com/mks0601/ExAvatar_RELEASE) | [Project](https://mks0601.github.io/ExAvatar/) |  |
| 2024 | [Gaussian Eigen Models for Human Heads](http://arxiv.org/abs/2407.04545) | CVPR 2025 | [Code](https://github.com/Zielon/GEM) | [Project](https://zielon.github.io/gem/) |  |
| 2024 | [Expressive Gaussian Human Avatars from Monocular RGB Video](http://arxiv.org/abs/2407.03204) | ArXiv 2024 | [Code](https://github.com/evahuman/EVA_Official) | [Project](https://evahuman.github.io/) |  |
| 2024 | [NPGA: Neural Parametric Gaussian Avatars](http://arxiv.org/abs/2405.19331) | ArXiv 2024 |  | [Project](https://simongiebenhain.github.io/NPGA/) |  |
| 2024 | [GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting Editing with Image Prompting](http://arxiv.org/abs/2405.07472) | On going work |  |  | Try-ON |
| 2024 | [3D Gaussian Blendshapes for Head Avatar Animation](http://arxiv.org/abs/2404.19398) | ACM SIGGRAPH 2024 |  |  | Gaussian splatting, blendshapes, head avatar, real-time rendering |
| 2024 | [MeGA: Hybrid Mesh-Gaussian Head Avatar for High-Fidelity Rendering and Head Editing](http://arxiv.org/abs/2404.19026) | ArXiv 2024 | [Code](https://github.com/conallwang/MeGA) | [Project](https://conallwang.github.io/MeGA_Pages/) | 🔥Gaussian Splatting |
| 2024 | [Dynamic Gaussians Mesh: Consistent Mesh Reconstruction from Monocular Videos](http://arxiv.org/abs/2404.12379) | ArXiv 2024 | [Code](https://github.com/Isabella98Liu/DG-Mesh) | [Project](https://www.liuisabella.com/DG-Mesh/) | 🔥Gaussian Splatting |
| 2024 | [HAHA: Highly Articulated Gaussian Human Avatars with Textured Mesh Prior](https://arxiv.org/abs/2404.01053) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [UV Gaussians: Joint Learning of Mesh Deformation and Gaussian Textures for Human Avatar Modeling](http://arxiv.org/abs/2403.11589) | ArXiv 2024 |  | [Project](https://alex-jyj.github.io/UV-Gaussians/ ) | 🔥Gaussian Splatting |
| 2024 | [DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization](http://arxiv.org/abs/2403.06912) | CVPR 2024 | [Code](https://github.com/Fictionarry/DNGaussian) | [Project](https://fictionarry.github.io/DNGaussian/) | 🔥Gaussian Splatting, Sparse-View |
| 2024 | [V3D: Video Diffusion Models are Effective 3D Generators](http://arxiv.org/abs/2403.06738) | ArXiv 2024 | [Code](https://github.com/heheyas/V3D) | [Project](https://heheyas.github.io/V3D/) | 🔥Gaussian Splatting, Video |
| 2024 | [SplattingAvatar: Realistic Real-Time Human Avatars with Mesh-Embedded Gaussian Splatting](https://arxiv.org/abs/2403.05087) | CVPR 2024 | [Code](https://github.com/initialneil/SplattingAvatar) | [Project](https://initialneil.github.io/SplattingAvatar) | 🔥Gaussian Splatting |
| 2024 | [GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video](http://arxiv.org/abs/2402.16607) | ArXiv 2024 |  | [Project](https://3d-aigc.github.io/GEA/) | 🔥Gaussian Splatting, Avatar |
| 2024 | [Consolidating Attention Features for Multi-view Image Editing](https://arxiv.org/abs/2402.14792) | ArXiv 2024 |  | [Project](https://qnerf-consolidation.github.io/qnerf-consolidation) | 🔥Gaussian Splatting, Edit |
| 2024 | [GaussianHair: Hair Modeling and Rendering with Light-aware Gaussians](https://arxiv.org/abs/2402.10483) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [ImplicitDeepfake: Plausible Face-Swapping through Implicit Deepfake Generation using NeRF and Gaussian Splatting](https://arxiv.org/abs/2402.06390) | ArXiv 2024 |  |  | 🔥Gaussian Splatting, Deepfake |
| 2024 | [HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting](https://arxiv.org/abs/2402.06149) | ECCV | [Code](https://github.com/ZhenglinZhou/HeadStudio) |  | 🔥Gaussian Splatting, Avatar |
| 2024 | [Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos](http://arxiv.org/abs/2402.03723) | ArXiv 2024 |  | [Project](http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html) | Portraits |
| 2024 | [4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes](http://arxiv.org/abs/2402.03307) | ArXiv 2024 |  |  | Dynamic Scenes |
| 2024 | [PSAvatar: A Point-based Shape Model for Real-Time Head Avatar Animation with 3D Gaussian Splatting](http://arxiv.org/abs/2401.12900) | ArXiv 2024 |  |  | 3D Gaussian Splatting, Head Avatar Animation, Point-based Shape Model, Real-time Rendering |
| 2024 | [GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting](http://arxiv.org/abs/2401.09720) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [Gaussian Shadow Casting for Neural Characters](http://arxiv.org/abs/2401.06116) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians with Dual Feature Fusion](http://arxiv.org/abs/2401.05925) | ArXiv 2024 | [Code](https://github.com/David-Dou/CoSSegGaussians) | [Project](https://david-dou.github.io/CoSSegGaussians) | Segmentic |
| 2024 | [AGG: Amortized Generative 3D Gaussians for Single Image to 3D](http://arxiv.org/abs/2401.04099) | ArXiv 2024 |  | [Project](https://ir1d.github.io/AGG/) | 🔥Gaussian Splatting |
| 2024 | [4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency](http://arxiv.org/abs/2312.17225) | ArXiv 2024 | [Code](https://github.com/VITA-Group/4DGen) | [Project](https://vita-group.github.io/4DGen/ ) | 🔥Gaussian Splatting |
| 2024 | [Human101: Training 100+FPS Human Gaussians in 100s from 1 View](http://arxiv.org/abs/2312.15258) | ArXiv 2024 | [Code](https://github.com/longxiang-ai/Human101) | [Project](https://longxiang-ai.github.io/Human101/) | 🔥Gaussian Splatting |
| 2024 | [Deformable 3D Gaussian Splatting for Animatable Human Avatars](http://arxiv.org/abs/2312.15059) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |
| 2024 | [3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting](http://arxiv.org/abs/2312.09228) | ArXiv 2024 | [Code](https://github.com/mikeqzy/3dgs-avatar-release) | [Project](https://neuralbodies.github.io/3DGS-Avatar) | 🔥Gaussian Splatting |
| 2024 | [HHAvatar: Gaussian Head Avatar with Dynamic Hairs](http://arxiv.org/abs/2312.03029) | ArXiv 2024 | [Code](https://github.com/YuelangX/Gaussian-Head-Avatar) | [Project](https://liaozhanfeng.github.io/HHAvatar/) | Hair |
| 2024 | [HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting](http://arxiv.org/abs/2312.02902) | ECCV |  |  | 🔥Gaussian Splatting |
| 2024 | [GaussianAvatars: Photorealistic Head Avatars with Rigged 3D Gaussians](http://arxiv.org/abs/2312.02069) | CVPR 2024 | [Code](https://github.com/ShenhanQian/GaussianAvatars) | [Project](https://shenhanqian.github.io/gaussian-avatars) | 🔥Gaussian Splatting |
| 2024 | [GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field](https://arxiv.org/abs/2312.01632) | ArXiv 2024 | [Code](https://github.com/chiehwangs/gaussian-head) |  | 🔥Gaussian Splatting |
| 2024 | [MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar](https://arxiv.org/abs/2312.00846) | ArXiv 2024 |  |  | 🔥Gaussian Splatting |

---



## Conversational & Dialogue

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367) | ArXiv 2026 |  | [Project](https://warmcongee.github.io/beyond-monologue) | talking-listening, interactive, full-duplex, conversational |
| 2026 | [PolySLGen: Online Multimodal Speaking-Listening Reaction Generation in Polyadic Interaction](https://arxiv.org/abs/2604.08125) | ArXiv 2026 | [Code](https://github.com/zylinzy/PolySLGen) |  | polyadic interaction, speaking-listening, multimodal reaction |
| 2026 | [GDPO-Listener: Expressive Interactive Head Generation via Auto-Regressive Flow Matching and Group reward-Decoupled Policy Optimization](https://arxiv.org/abs/2603.25020) | ArXiv 2026 |  |  | listener, interactive, flow matching, RLHF |
| 2026 | [ECHO: Towards Emotionally Appropriate and Contextually Aware Interactive Head Generation](https://arxiv.org/abs/2603.17427) | ArXiv 2026 |  | [Project](https://xk0720.github.io/ECHO) | Interactive Head, Emotion, Context-Aware, Dialogue |
| 2026 | [ReactMotion: Generating Reactive Listener Motions from Speaker Utterance](https://arxiv.org/abs/2603.15083) | ArXiv 2026 | [Code](https://github.com/awakening-ai/ReactMotion) | [Project](https://reactmotion.github.io) | listener motion, reactive, body motion, speaker utterance |
| 2026 | [Talking Together: Synthesizing Co-Located 3D Conversations from Audio](https://arxiv.org/abs/2603.08674) | CVPR 2026 |  |  | 3D, Conversations, Talking Head, CVPR |
| 2026 | [A²-LLM: An End-to-end Conversational Audio Avatar Large Language Model](https://arxiv.org/abs/2602.04913) | ArXiv 2026 | [Code](https://github.com/Hooyoung-for-AI/A2-LLM) |  | Conversational, Avatar, LLM |
| 2026 | [HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction](http://arxiv.org/abs/2601.13801) | ArXiv 2026 |  |  | lip-synced avatars, real-time conversational AI, multimodal pipeline |
| 2026 | [RSATalker: Realistic Socially-Aware Talking Head Generation for Multi-Turn Conversation](https://arxiv.org/abs/2601.10606) | ArXiv 2026 |  |  | Multi-Turn Conversation, Talking Head |
| 2026 | [Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation](http://arxiv.org/abs/2601.00664) | ArXiv 2026 | [Code](https://github.com/TaekyungKi/AvatarForcing) | [Project](https://taekyungki.github.io/AvatarForcing) | Interactive avatar, Diffusion forcing, Real-time, Preference optimization |
| 2025 | [ALIVE: An Avatar-Lecture Interactive Video Engine with Content-Aware Retrieval for Real-Time Interaction](http://arxiv.org/abs/2512.20858) | ArXiv 2025 |  |  | neural talking-head synthesis, content-aware retrieval, real-time interaction, LLM |
| 2025 | [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](http://arxiv.org/abs/2512.20296) | ArXiv 2025 |  |  | text-driven, audio-visual, interactive dialogue, cross-modal mappers |
| 2025 | [ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body](http://arxiv.org/abs/2512.14234) | ArXiv 2025 | [Code](https://github.com/Juzezhang/ViBES) | [Project](https://ai.stanford.edu/~juze/ViBES/) | conversational agent, 3D avatar, multimodal interaction, joint language-motion |
| 2025 | [Towards Interactive Intelligence for Digital Humans](http://arxiv.org/abs/2512.13674) | ArXiv 2025 |  |  | interactive intelligence, digital human, multimodal embodiment, real-time interaction |
| 2025 | [Hi-Reco: High-Fidelity Real-Time Conversational Digital Humans](https://arxiv.org/abs/2511.12662) | CGI 2025 |  |  | real-time, conversational, high-fidelity, 3D avatar |
| 2025 | [Think Before You Talk: Enhancing Meaningful Dialogue Generation in Full-Duplex Speech Language Models with Planning-Inspired Text Guidance](http://arxiv.org/abs/2508.07375) | ArXiv 2025 | [Code](https://github.com/dreamtheater123/TurnGuide) | [Project](https://dreamtheater123.github.io/TurnGuide-Demo/) | Dialogue Generation, Speech Language Models |
| 2025 | [UniTalker: Conversational Speech-Visual Synthesis](http://arxiv.org/abs/2508.04585) | ACM MM 2025 |  |  | Conversational, Multimodal, Emotion |
| 2025 | [Real-time Generation of Various Types of Nodding for Avatar Attentive Listening System](http://arxiv.org/abs/2507.23298) | ICMI 2025 | [Code](https://github.com/MaAI-Kyoto/MaAI) |  | Real-time, Nodding Generation, Avatar Interaction |
| 2025 | [MultiTalk: Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation](http://arxiv.org/abs/2505.22647) | ArXiv 2025 | [Code](https://github.com/MeiGen-AI/MultiTalk) | [Project](https://meigen-ai.github.io/multi-talk) | Multi-Person, Conversational |
| 2025 | [DualTalk: Dual-Speaker Interaction for 3D Talking Head Conversations](http://arxiv.org/abs/2505.18096) | CVPR 2025 | [Code](https://github.com/ziqiaopeng/DualTalk) | [Project](https://ziqiaopeng.github.io/dualtalk) | 3D, Interaction, Dual-Speaker, Conversations, FLAME |
| 2025 | [VividListener: Expressive and Controllable Listener Dynamics Modeling for Multi-Modal Responsive Interaction](http://arxiv.org/abs/2504.21718) | ArXiv 2025 |  |  | Listener dynamics, 3D dyadic conversation, Expressive control, Multi-modal conditions |
| 2024 | [INFP: Audio-Driven Interactive Head Generation in Dyadic Conversations](http://arxiv.org/abs/2412.04037) | ArXiv 2024 |  | [Project](https://grisoon.github.io/INFP) | Dyadic Conversations |
| 2024 | [Talk With Human-like Agents: Empathetic Dialogue Through Perceptible Acoustic Reception and Reaction](http://arxiv.org/abs/2406.12707) | ACL 2024 | [Code](https://github.com/Haoqiu-Yan/PerceptiveAgent) |  | Empathetic Dialogue |
| 2024 | [MultiDialog: Let's Go Real Talk: Spoken Dialogue Model for Face-to-Face Conversation](http://arxiv.org/abs/2406.07867) | ACL 2024 | [Code](https://huggingface.co/datasets/IVLLab/MultiDialog) | [Project](https://huggingface.co/datasets/IVLLab/MultiDialog) | Dialogue, Face-to-Face Conversation |
| 2023 | [Emotional Listener Portrait: Realistic Listener Motion Simulation in Conversation](https://openaccess.thecvf.com/content/ICCV2023/papers/Song_Emotional_Listener_Portrait_Neural_Listener_Head_Generation_with_Emotion_ICCV_2023_paper.pdf) | ICCV 2023 |  |  | Emotion, LHG |
| 2022 | [DialogueNeRF: Towards Realistic Avatar Face-to-face Conversation Video Generation](https://arxiv.org/abs/2203.07931.pdf) | ArXiv 2022 |  |  | Dialogue, Face-to-face Conversation |

---



## Talking Body & Avatar

| Year | Title | Conference/Journal | Code | Project | Keywords |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2026 | [Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953) | FG 2026 |  | [Project](https://prompt-to-gesture.github.io) | gesture generation |
| 2026 | [Efficient Emotion-Aware Iconic Gesture Prediction for Robot Co-Speech](https://arxiv.org/abs/2604.11417) | ArXiv 2026 |  |  | co-speech gesture, robot, iconic gesture, emotion-aware |
| 2026 | [LiveGesture Streamable Co-Speech Gesture Generation Model](https://arxiv.org/abs/2604.10927) | ArXiv 2026 |  | [Project](https://m-usamasaleem.github.io/publication/LiveGesture/LiveGesture.html) | co-speech gesture, streaming, full-body, real-time |
| 2026 | [SentiAvatar: Towards Expressive and Interactive Digital Humans](https://arxiv.org/abs/2604.02908) | ArXiv 2026 | [Code](https://github.com/SentiAvatar/SentiAvatar) | [Project](https://sentiavatar.github.io) | Digital Human, Expressive, Interactive, Sentiment |
| 2026 | [HolisticSemGes: Semantic Grounding of Holistic Co-Speech Gesture Generation with Contrastive Flow-Matching](https://arxiv.org/abs/2603.26553) | ArXiv 2026 | [Code](https://github.com/marcos452/HoliticSemGes) | [Project](https://marcos452.github.io/HoliticSemGes) | Co-Speech Gesture, Semantic Grounding, Flow-Matching |
| 2026 | [Empathetic Motion Generation for Humanoid Educational Robots via Reasoning-Guided Vision-Language-Motion Diffusion](https://arxiv.org/abs/2603.18771) | ArXiv 2026 |  |  | Empathetic Motion, Humanoid Robot, Gesture Generation |
| 2026 | [MIBURI: Towards Expressive Interactive Gesture Synthesis](http://arxiv.org/abs/2603.03282) | CVPR 2026 | [Code](https://github.com/m-hamza-mughal/miburi/) | [Project](https://vcai.mpi-inf.mpg.de/projects/MIBURI/) | Gesture Synthesis, Real-Time, LLM-Conditioned, Whole-Body |
| 2026 | [DyaDiT: A Multi-Modal Diffusion Transformer for Socially Favorable Dyadic Gesture Generation](https://arxiv.org/abs/2602.23165) | ArXiv 2026 |  | [Project](https://puckikk1202.github.io/dyadit_hp) | Dyadic Gesture, Diffusion Transformer, Multi-Modal, Social Interaction |
| 2026 | [3DGesPolicy: Phoneme-Aware Holistic Co-Speech Gesture Generation Based on Action Control](http://arxiv.org/abs/2601.18451) | ArXiv 2026 |  |  | co-speech gesture, diffusion policy, phoneme-aware, holistic motion |
| 2026 | [SmoothSync: Dual-Stream Diffusion Transformers for Jitter-Robust Beat-Synchronized Gesture Generation from Quantized Audio](http://arxiv.org/abs/2601.04236) | ArXiv 2026 |  |  | Gesture generation, Diffusion Transformer, Beat synchronization, Jitter suppression |
| 2026 | [Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints](http://arxiv.org/abs/2511.10076) | AAAI 2026 | [Code](https://github.com/Xiangyue-Zhang/GlobalDiff) | [Project](https://xiangyue-zhang.github.io/GlobalDiff) | co-speech motion, global rotation diffusion, multi-level constraints, error accumulation |
| 2025 | [StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars](http://arxiv.org/abs/2512.22065) | ArXiv 2025 |  | [Project](https://streamavatar.github.io/) | Real-Time Avatar, Streaming Diffusion, Interactive Human Avatars, Autoregressive Distillation |
| 2025 | [Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots](http://arxiv.org/abs/2512.17183) | ArXiv 2025 |  |  | co-speech gestures, humanoid robot, real-time control, semantic synthesis |
| 2025 | [Evaluation of Generative Models for Emotional 3D Animation Generation in VR](http://arxiv.org/abs/2512.16081) | ArXiv 2025 |  | [Project](https://emotional3dhumans.github.io) | speech-driven animation, emotional expression, 3D avatar, VR evaluation |
| 2025 | [Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation](https://arxiv.org/abs/2512.13495) | ArXiv 2025 | [Code](https://github.com/zhangzjn/Soul) | [Project](https://zhangzjn.github.io/projects/Soul) | digital human, multimodal animation, lip sync, full-body, long-term |
| 2025 | [Towards Unified Co-Speech Gesture Generation via Hierarchical Implicit Periodicity Learning](http://arxiv.org/abs/2512.13131) | IEEE Transactions on Image Processing |  |  | co-speech gesture generation, 3D motion, hierarchical periodicity, audio-driven |
| 2025 | [InteracTalker: Prompt-Based Human-Object Interaction with Co-Speech Gesture Generation](https://arxiv.org/abs/2512.12664) | ArXiv 2025 |  |  | Co-Speech Gesture, Human-Object Interaction, Prompt-Based |
| 2025 | [Co-speech Gesture Video Generation via Motion-Based Graph Retrieval](https://arxiv.org/abs/2512.02576) | ArXiv 2025 |  |  | Co-Speech Gesture, Video Generation, Graph Retrieval |
| 2025 | [fMRI2GES: Co-speech Gesture Reconstruction from fMRI Signal with Dual Brain Decoding Alignment](https://arxiv.org/abs/2512.01189) | TCSVT 2025 |  |  | Co-Speech Gesture, fMRI, Brain Decoding |
| 2025 | [CoordSpeaker: Exploiting Gesture Captioning for Coordinated Caption-Empowered Co-Speech Gesture Generation](https://arxiv.org/abs/2511.22863) | ArXiv 2025 |  |  | Co-Speech Gesture, Gesture Captioning, Coordinated Generation |
| 2025 | [Towards Reliable Human Evaluations in Gesture Generation: Insights from a Community-Driven State-of-the-Art Benchmark](https://arxiv.org/abs/2511.01233) | ArXiv 2025 |  |  | Gesture Generation, Human Evaluation, Benchmark |
| 2025 | [Lookahead Anchoring: Preserving Character Identity in Audio-Driven Human Animation](http://arxiv.org/abs/2510.23581) | ArXiv 2025 | [Code](https://github.com/j0seo/lookahead-anchoring) | [Project](https://lookahead-anchoring.github.io) | Character Identity, Audio-Driven, Human Animation |
| 2025 | [Conveying Meaning through Gestures: An Investigation into Semantic Co-Speech Gesture Generation](https://arxiv.org/abs/2510.17599) | ArXiv 2025 |  |  | Gesture, Meaning, Co-Speech |
| 2025 | [Social Agent: Mastering Dyadic Nonverbal Behavior Generation via Conversational LLM Agents](http://arxiv.org/abs/2510.04637) | ArXiv 2025 |  | [Project](https://pku-mocca.github.io/Social-Agent-Page) | Dyadic Interaction, Gesture Generation, LLM-driven |
| 2025 | [SIG-Chat: Spatial Intent-Guided Conversational Gesture Generation Involving How, When and Where](https://arxiv.org/abs/2509.23852) | ArXiv 2025 |  |  | Conversational Gesture, Spatial Intent |
| 2025 | [CPEP: Contrastive Pose-EMG Pre-training Enhances Gesture Generalization on EMG Signals](https://arxiv.org/abs/2509.04699) | 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Foundation Models for the Brain and Body |  |  | Gesture, EMG, Contrastive Pre-training |
| 2025 | [InfinityHuman: Towards Long-Term Audio-Driven Human](http://arxiv.org/abs/2508.20210) | ArXiv 2025 |  | [Project](https://infinityhuman.github.io/) | Long-Term, Hand Motion, Pose-Guided |
| 2025 | [OmniHuman-1.5: Instilling an Active Mind in Avatars via Cognitive Simulation](http://arxiv.org/abs/2508.19209) | ArXiv 2025 |  | [Project](https://omnihuman-lab.github.io/v1_5/) | Cognitive Simulation, Avatar, Multimodal |
| 2025 | [Ges-QA: A Multidimensional Quality Assessment Dataset for Audio-to-3D Gesture Generation](https://arxiv.org/abs/2508.12020) | ArXiv 2025 |  |  | Gesture QA, Dataset, 3D Gesture |
| 2025 | [Preview WB-DH: Towards Whole Body Digital Human Bench for the Generation of Whole-body Talking Avatar Videos](http://arxiv.org/abs/2508.08891) | ICCV 2025 Workshop |  | [Project](https://github.com/deepreasonings/WholeBodyBenchmark) | Whole-Body Avatar, Benchmark |
| 2025 | [GestureHYDRA: Semantic Co-speech Gesture Synthesis via Hybrid Modality Diffusion Transformer and Cascaded-Synchronized Retrieval-Augmented Generation](http://arxiv.org/abs/2507.22731) | ICCV 2025 |  | [Project](https://mumuwei.github.io/GestureHYDRA/) | Co-speech Gesture Synthesis, Hybrid Modality Diffusion Transformer, Retrieval-Augmented Generation |
| 2025 | [JWB-DH-V1: Benchmark for Joint Whole-Body Talking Avatar and Speech Generation Version 1](http://arxiv.org/abs/2507.20987) | ICCV 2025 Workshop |  | [Project](https://github.com/deepreasonings/WholeBodyBenchmark) | Whole-Body Avatar, Benchmark |
| 2025 | [Democratizing High-Fidelity Co-Speech Gesture Video Generation](http://arxiv.org/abs/2507.06812) | ICCV 2025 | [Code](https://github.com/MPI-Lab/Democratizing-High-Fidelity-Co-Speech-Gesture-Video-Generation) | [Project](https://mpi-lab.github.io/Democratizing-CSG/) | Diffusion Model, Skeleton-Audio Fusion, Co-Speech Gesture, Video Generation |
| 2025 | [EchoMimicV3: 1.3B Parameters are All You Need for Unified Multi-Modal and Multi-Task Human Animation](http://arxiv.org/abs/2507.03905) | ArXiv 2025 |  |  | Multi-Modal, Multi-Task, Human Animation |
| 2025 | [MirrorMe: Towards Realtime and High Fidelity Audio-Driven Halfbody Animation](http://arxiv.org/abs/2506.22065) | ArXiv 2025 |  |  | Real-time, Half-body Animation |
| 2025 | [OmniAvatar: Efficient Audio-Driven Avatar Video Generation with Adaptive Body Animation](http://arxiv.org/abs/2506.18866) | ArXiv 2025 | [Code](https://github.com/Omni-Avatar/OmniAvatar) | [Project](https://omni-avatar.github.io) | Audio-Driven, Body Animation |
| 2025 | [Co-Speech Gesture and Facial Expression Generation for Non-Photorealistic 3D Characters](http://arxiv.org/abs/2506.16159) | SIGGRAPH 2025 Poster |  |  | co-speech generation, non-photorealistic characters, facial expressions, gestures |
| 2025 | [AlignHuman: Improving Motion and Fidelity via Timestep-Segment Preference Optimization for Audio-Driven Human Animation](http://arxiv.org/abs/2506.11144) | ArXiv 2025 |  | [Project](https://alignhuman.github.io) | Preference Optimization, Human Animation |
| 2025 | [HunyuanVideo-HOMA: Generic Human-Object Interaction in Multimodal Driven Human Animation](http://arxiv.org/abs/2506.08797) | ArXiv 2025 |  |  | Human-Object Interaction, Human Animation |
| 2025 | [TRiMM: Transformer-Based Rich Motion Matching for Real-Time multi-modal Interaction in Digital Humans](http://arxiv.org/abs/2506.01077) | ArXiv 2025 | [Code](https://github.com/teroon/TRiMM-Transformer-Based-Rich-Motion-Matching) |  | Co-speech Gesture, Real-time, Transformer, Digital Humans |
| 2025 | [HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters](http://arxiv.org/abs/2505.20156) | ArXiv 2025 |  |  | Multi-Character, Human Animation |
| 2025 | [Intentional Gesture: Deliver Your Intentions with Gestures for Speech](http://arxiv.org/abs/2505.15197) | ArXiv 2025 | [Code](https://github.com/andypinxinliu/Intentional-Gesture) | [Project](https://andypinxinliu.github.io/Intentional-Gesture) | co-speech gesture, communicative intention, motion tokenizer, BEAT-2 |
| 2025 | [AsynFusion: Towards Asynchronous Latent Consistency Models for Decoupled Whole-Body Audio-Driven Avatars](http://arxiv.org/abs/2505.15058) | ArXiv 2025 |  |  | Whole-Body, Diffusion, Avatar |
| 2025 | [M3G: Multi-Granular Gesture Generator for Audio-Driven Full-Body Human Motion Synthesis](http://arxiv.org/abs/2505.08293) | NeurIPS 2025 |  |  | Gesture, Full-Body |
| 2025 | [PAHA: Parts-Aware Audio-Driven Human Animation with Diffusion Model](http://arxiv.org/abs/2505.03603) | ArXiv 2025 |  |  | Parts-Aware, Diffusion, Human Animation |
| 2025 | [Co3Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion](http://arxiv.org/abs/2505.01746) | ICLR 2025 Spotlight |  | [Project](https://mattie-e.github.io/Co3/) | Concurrent co-speech gesture, Interactive diffusion, Two-person interaction, 3D gesture dataset |
| 2025 | [EchoMask: Speech-Queried Attention-based Mask Modeling for Holistic Co-Speech Motion Generation](http://arxiv.org/abs/2504.09209) | ArXiv 2025 |  |  | Co-Speech Motion, Masked Modeling, Speech-Queried Attention |
| 2025 | [EasyGenNet: An Efficient Framework for Audio-Driven Gesture Video Generation Based on Diffusion Model](http://arxiv.org/abs/2504.08344) | ArXiv 2025 |  |  | Audio-Driven Video, Diffusion Model, Gesture Synthesis |
| 2025 | [ReCoM: Realistic Co-Speech Motion Generation with Recurrent Embedded Transformer](http://arxiv.org/abs/2503.21847) | ArXiv 2025 |  | [Project](https://yong-xie-xy.github.io/ReCoM/) | Co-Speech Motion, Transformer, Gesture Generation, Speech Synchronization |
| 2025 | [SARGes: Semantically Aligned Reliable Gesture Generation via Intent Chain](http://arxiv.org/abs/2503.20202) | ArXiv 2025 |  |  | Gesture Generation, LLM, Intent Chain, Co-speech |
| 2025 | [PRIMAL: Physically Reactive and Interactive Motor Model for Avatar Learning](http://arxiv.org/abs/2503.17544) | ICCV 2025 | [Code](https://github.com/yz-cnsdqz/primal-release) | [Project](https://yz-cnsdqz.github.io/eigenmotion/PRIMAL) | Avatar, Whole-Body, Motion Generation |
| 2025 | [DIDiffGes: Decoupled Semi-Implicit Diffusion Models for Real-time Gesture Generation from Speech](http://arxiv.org/abs/2503.17059) | AAAI 2025 | [Code](https://github.com/cyk990422/Efficient-Audio-Gesture) | [Project](https://cyk990422.github.io/DIDiffGes) | Gesture Generation, Diffusion Models, Real-time, Speech-driven |
| 2025 | [Large Language Models for Virtual Human Gesture Selection](http://arxiv.org/abs/2503.14408) | AAMAS 2025 |  |  | Gesture Selection, Large Language Models, Virtual Agents, Co-speech |
| 2025 | [Cosh-DiT: Co-Speech Gesture Video Synthesis via Hybrid Audio-Visual Diffusion Transformers](http://arxiv.org/abs/2503.09942) | ArXiv 2025 |  | [Project](https://sunyasheng.github.io/projects/COSH-DIT) | Co-speech gesture, Diffusion Transformers, VQ-VAEs, Audio-visual synthesis |
| 2025 | [Versatile Multimodal Controls for Whole-Body Talking Human Animation](http://arxiv.org/abs/2503.08714) | ArXiv 2025 |  |  | Whole-Body, Multimodal |
| 2025 | [HOP: Heterogeneous Topology-based Multimodal Entanglement for Co-Speech Gesture Generation](http://arxiv.org/abs/2503.01175) | ArXiv 2025 | [Code](https://github.com/Chenghyyy/HOP-Heterogeneous-Topology-based-Multimodal-Entanglement-for-Co-Speech-Gesture-Generation) | [Project](https://star-uu-wang.github.io/HOP/) | Co-speech gesture, Multimodal entanglement, Spatiotemporal graph, Audio-text semantic |
| 2025 | [OmniHuman-1: Rethinking the Scaling-Up of One-Stage Conditioned Human Animation Models](http://arxiv.org/abs/2502.01061) | ICCV 2025 |  | [Project](https://omnihuman-lab.github.io) | Human Animation, Scaling |
| 2025 | [EMO2: End-Effector Guided Audio-Driven Avatar Video Generation](http://arxiv.org/abs/2501.10687) | ArXiv 2025 |  |  | Audio-driven, Gesture Generation, Diffusion Model, End-effector Guidance |
| 2025 | [One Shot, One Talk: Whole-body Talking Avatar from a Single Image](https://arxiv.org/abs/2412.01106) | ICCV 2025 |  | [Project](https://ustc3dv.github.io/OneShotOneTalk/) | Whole-body, Talking Avatar, Single Image, 3D Gaussian |
| 2025 | [EchoMimicV2: Towards Striking, Simplified, and Semi-Body Human Animation](https://arxiv.org/abs/2411.10061) | CVPR 2025 |  |  | Semi-Body, Human Animation |
| 2025 | [CoCoGesture: Toward Coherent Co-speech 3D Gesture Generation in the Wild](http://arxiv.org/abs/2405.16874) | ArXiv 2025 |  | [Project](https://mattie-e.github.io/GES-X/) | 3D Gesture Generation, Diffusion Model, Audio-Driven |
| 2024 | [ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196) | ArXiv 2024 |  | [Project](https://exbody2.github.io) | humanoid, expressive, whole-body control, motion imitation |
| 2024 | [Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796) | ArXiv 2024 | [Code](https://github.com/chengxuxin/expressive-humanoid) | [Project](https://expressive-humanoid.github.io) | humanoid, expressive motion, whole-body control |
| 2024 | [Weakly-Supervised Emotion Transition Learning for Diverse 3D Co-speech Gesture Generation](http://arxiv.org/abs/2311.17532) | CVPR 2024 |  | [Project](https://xingqunqi-lab.github.io/Emo-Transition-Gesture/) | 3D Co-speech Gesture, Emotion Transition, Weakly-Supervised Learning, Virtual Avatar Animation |
| 2023 | [Speech-Gesture GAN: Gesture Generation for Robots and Embodied Agents](https://arxiv.org/abs/2309.09346) | RO-MAN 2023 |  |  | co-speech gesture, GAN, robot, embodied agent |
| 2023 | [C2G2: Controllable Co-speech Gesture Generation with Latent Diffusion Model](http://arxiv.org/abs/2308.15016) | ArXiv 2023 | [Code](https://github.com/C2G2-Gesture/C2G2) | [Project](https://c2g2-gesture.github.io/c2_gesture) | Co-speech Gesture, Latent Diffusion, Temporal Dependency |
| 2022 | [Freeform Body Motion Generation from Speech](http://arxiv.org/abs/2203.02291) | ArXiv 2022 | [Code](https://github.com/TheTempAccount/Co-Speech-Motion-Generation) |  | co-speech motion, pose modes, rhythmic dynamics, speech prosody |
| 2018 | [Robots Learn Social Skills: End-to-End Learning of Co-Speech Gesture Generation for Humanoid Robots](https://arxiv.org/abs/1810.12541) | ArXiv 2018 |  |  | co-speech gesture, end-to-end, robot, deep learning |

---



## Metrics

| Metrics                                             | Paper                                                        | Link                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| PSNR (peak signal-to-noise ratio)                   | -                                                            |                                                              |
| SSIM (structural similarity index measure)          | Image quality assessment: from error visibility to structural similarity. |                                                              |
| CPBD(cumulative probability of blur detection)      | A no-reference image blur metric based on the cumulative probability of blur detection |                                                              |
| LPIPS (Learned Perceptual Image Patch Similarity) - | The Unreasonable Effectiveness of Deep Features as a Perceptual Metric | [paper](https://arxiv.org/pdf/1801.03924.pdf)                |
| NIQE (Natural Image Quality Evaluator)              | Making a ‘Completely Blind’ Image Quality Analyzer           | [paper](http://live.ece.utexas.edu/research/Quality/niqe_spl.pdf) |
| FID (Fréchet inception distance)                    | GANs trained by a two time-scale update rule converge to a local nash equilibrium |                                                              |
| LMD (landmark distance error)                       | Lip Movements Generation at a Glance                         |                                                              |
| LRA (lip-reading accuracy)                          | Talking Face Generation by Conditional Recurrent Adversarial Network | [paper](https://arxiv.org/pdf/1804.04786.pdf)                |
| WER(word error rate)                                | Lipnet: end-to-end sentencelevel lipreading.                 |                                                              |
| LSE-D (Lip Sync Error - Distance)                   | Out of time: automated lip sync in the wild                  |                                                              |
| LSE-C (Lip Sync Error - Confidence)                 | Out of time: automated lip sync in the wild                  |                                                              |
| ACD(Average content distance)                       | Facenet: a unified embedding for face recognition and clustering. |                                                              |
| CSIM(cosine similarity)                             | Arcface: additive angular margin loss for deep face recognition. |                                                              |
| EAR(eye aspect ratio)                               | Real-time eye blink detection using facial landmarks. In: Computer Vision Winter Workshop |                                                              |
| ESD(emotion similarity distance)                    | What comprises a good talking-head video generation?: A Survey and Benchmark |                                                              |

### Related Papers on Metrics

| Year | Paper | Conference | Keywords |
|------|-------|------------|----------|
| 2025 | [NTIRE 2025 XGC Quality Assessment Challenge: Methods and Results](http://arxiv.org/abs/2506.02875) | ArXiv 2025 | quality assessment, talking head, challenge, THQA-NTIRE |

---



## Tools & Software

| Tool/Resource                                                | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [LUCIA](https://sourceforge.net/projects/lucia/)             | Development of a MPEG-4 Talking Head Engine. 💻               |
| [Yepic Studio](https://www.g2.com/products/yepic-studio/reviews) | Create and dub talking head-style videos in minutes without expensive equipment. 🎥 |
| [Mel McGee's Talkbots](https://sourceforge.net/projects/talkbots/) | A complete multi-browser, multi-platform talking head application in SVG suitable for web sites or as an avatar. 🗣️ |
| [face3D_chung](https://sourceforge.net/projects/face3dchung/) | Create 3D character avatar head objects with texture from a single photo for your games. 🎮 |
| [CrazyTalk](https://www.g2.com/products/crazytalk/reviews)   | Exciting features for 3D head creation and automation. 🤪     |
| [tts avatar free download - SourceForge](https://sourceforge.net/directory/?q=tts%20avatar) | Mel McGee's Talkbots is a complete multi-browser, multi-platform talking head. (🔧👄) |
| [Verbatim AI - Product Information, Latest Updates, and Reviews 2023](https://www.producthunt.com/products/verbatim-ai) | A simple yet powerful API to generate AI "talking head" videos in near real-time with Verbatim AI. Add interest, intrigue, and dynamism to your chat bots! (🔧👄) |
| [Best Open Source BASIC 3D Modeling Software](https://sourceforge.net/directory/3d-modeling/basic/) | Includes talk3D_chung, a small example using obj models created with face3D_chung, and speak3D_chung_dll, a dll to load and display face3D_chung talking avatars. (🛠️🎭) |
| [DVDStyler / Discussion / Help: ffmpeg-vbr or internal](https://sourceforge.net/p/dvdstyler/discussion/318795/thread/82dcb647/) | Talking heads would get a bitrate which is unnecessarily high while using DVDStyler. (🛠️👄) |
| [puffin web browser free download - SourceForge](https://sourceforge.net/directory/lisp/?q=puffin+web+browser) | Mel McGee's Talkbots is a complete multi-browser, multi-platform talking head. (🔧👄) |
| [12 best AI video generators to use in 2023 Free and paid \|Product ...](https://www.producthunt.com/stories/best-ai-video-generators-free) | Whether you’re an entrepreneur, small business owner, or run a large company, AI video generators make it super easy to create high-quality videos from scratch. (🔧🎥) |

---



## Slides & Presentations

| Presentation Title                                           | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Few-Shot Adversarial Learning of Realistic Neural Talking Head Models](https://www.slideshare.net/ssuserc9d82a/paper-reviewfewshot-adversarial-learning-of-realistic-neural-talking-head-models) | Presentation reviewing the few-shot adversarial learning of realistic neural talking head models. |
| [Nethania Michelle's Character](https://www.slideshare.net/ZULHICZARARIETINARBU/nethania-michelles-character) | PPT: Presentation discussing the improvement of a 3D talking head for use in an avatar of a virtual meeting room. |
| [Presenting you: Top tips on presenting with Prezi Video – Prezi](https://support.prezi.com/hc/en-us/articles/360036679953-Presenting-you-Top-tips-on-presenting-with-Prezi-Video) | Article providing top tips for presenting with Prezi Video.  |
| [Research Presentation](https://pt.slideshare.net/willg_36/research-presentation-presentation-956726) | PPT: Resident Research Presentation Slide Deck.              |
| [Adding narration to your presentation (using Prezi Video) – Prezi](https://support.prezi.com/hc/en-us/articles/360038281894-Adding-narration-to-your-presentation-using-Prezi-Video-) | Learn how to add narration to your Prezi presentation with Prezi Video. |

---



## References

| Website                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [arXiv](https://arxiv.org/)                                  | Provides preprints in various academic fields, serving as an important platform for accessing the latest research findings. |
| [CVF Open Access](https://openaccess.thecvf.com/)            | The Computer Vision Foundation's open-access platform, offering open-access papers from top conferences such as CVPR, ICCV, ECCV, and more. |
| [Papers with Code](https://paperswithcode.com/)              | A platform that aggregates research papers with accompanying code implementations, making it convenient to find the latest research findings and their corresponding implementations. |
| [ICCV - International Conference on Computer Vision](https://dblp.uni-trier.de/db/conf/eccv/index.html) | The International Conference on Computer Vision, gathering the latest research findings in the field of computer vision. |
| [ECCV - European Conference on Computer Vision](http://www.informatik.uni-trier.de/~ley/db/conf/eccv/index.html) | The European Conference on Computer Vision, providing the latest research results and related information in the field of computer vision. |
| [CVPR - Conference on Computer Vision and Pattern Recognition](http://dblp.uni-trier.de/db/conf/cvpr/index.html) | The Conference on Computer Vision and Pattern Recognition, one of the top conferences in computer vision, showcasing numerous important research findings. |

---



## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Kedreamix/Awesome-Talking-Head-Synthesis&type=Date)](https://star-history.com/#Kedreamix/Awesome-Talking-Head-Synthesis&Date)



[1]: https://github.com/YunjinPark/awesome_talking_face_generation
[2]: https://github.com/LTT-O/Awesome-Talking-Head-Generation

[3]: https://github.com/JosephPai/Awesome-Talking-Face "Greate Project"

[4]: https://github.com/weishida01/Awesome-Talking-Face-Generation
[5]: https://github.com/harlanhong/awesome-talking-head-generation "nice job"
[6]:https://github.com/Curated-Awesome-Lists/awesome-ai-talking-heads "full of tools"
