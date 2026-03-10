#!/usr/bin/env python3
"""
将新论文添加到 README.md
"""

import re

# 负向过滤关键词（排除不相关的论文）
EXCLUDE_KEYWORDS = [
    # Deepfake 检测相关
    'deepfake detection', 'deepfake generator', 'deepfake challenge',
    'face forgery detection', 'manipulation detection',
    # 语音处理相关（非视觉）
    'voice conversion', 'voice cloning', 'voice anonymization', 'voice synthesis',
    'speaker verification', 'speaker recognition', 'speaker identification',
    'speech recognition', 'asr', 'automatic speech recognition', 'lip reading',
    'text-to-speech', 'tts ', 'speech synthesis',
    'audio watermarking', 'audio adversarial',
    # 其他非 talking head 任务
    'gesture generation', 'co-speech gesture', 'body motion', 'hand gesture',
    'video-to-speech', 'voice2speech',
    'biometric', 'anti-spoofing', 'spoofing detection', 'face anti-spoofing',
    'alzheimer', 'suicide risk', 'health detection', 'disease detection',
    # 评测/基准论文
    'benchmark', 'evaluation of', 'assessing', 'quality assessment',
    'perceptual quality', 'user study', 'survey', 'review',
    # 非生成任务
    'emotion recognition', 'affect recognition', 'latency benchmark',
    'pedagogical', 'educational framework', 'therapy', 'post-stroke',
    'sense of agency', 'narrativity', 'virtual reality study',
    # 其他不相关
    'privacy policies', 'older adults', 'child welfare', 'voice assistant',
    'drone interaction', 'garment reconstruction', 'suicide', 'dementia',
    'diagrammatic learning', 'policy debating', 'location inference',
    'crisis microblogs', 'fake narratives', 'hateful stories',
    'floorplan generation', 'virtual try-on', 'clothing tryer',
    'speech-to-action', 'spoken descriptions', '3d scenes',
    'diagrammatic learning', 'proactive agentic', 'whiteboards',
    # 额外排除
    'dense caption', 'spoken descriptions', 'healthcare applications',
    'self-extension', 'virtual reality', 'interactive intelligence'
]

# 核心关键词
CORE_KEYWORDS = [
    'talking head', 'talking face', 'talking portrait', 'talking avatar',
    'talking human', 'talking body',
    'face animation', 'facial animation', 'portrait animation',
    'lip sync', 'lip-sync', 'lipsync', 'lip-synchronization',
    'avatar animation', 'avatar video',
    'human animation', 'head animation',
    'face generation', 'facial generation', 'portrait generation',
    'voice2face', 'voice-to-face', 'audio-to-face',
    'audio-driven', 'speech-driven', '3dgs', 'gaussian splatting', 'nerf'
]

def should_exclude(title_lower):
    """判断论文是否应该排除"""
    for kw in EXCLUDE_KEYWORDS:
        if kw in title_lower:
            return True
    return False

def is_core_paper(title_lower):
    """判断是否是核心 talking head 论文"""
    # 检查是否包含核心关键词
    for kw in CORE_KEYWORDS:
        if kw in title_lower:
            return True
    return False

def extract_existing_titles(readme_content, section_name):
    """从指定 section 中提取论文标题"""
    titles = set()
    section_pattern = rf'## {re.escape(section_name)}\n(.*?)(?=\n## |\Z)'
    section_match = re.search(section_pattern, readme_content, re.DOTALL)
    if not section_match:
        return titles
    section_content = section_match.group(1)
    paper_pattern = r'\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]'
    for match in re.finditer(paper_pattern, section_content):
        title = match.group(2).lower()
        titles.add(title)
    return titles

def read_new_papers(filename):
    """读取新论文"""
    papers = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('| 20'):
                papers.append(line)
    return papers

def filter_papers(papers, existing_titles):
    """过滤论文，返回需要添加的论文"""
    to_add = []
    for line in papers:
        # 提取标题
        match = re.match(r'\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]', line)
        if not match:
            continue
        title = match.group(2).lower()

        # 跳过已存在的论文
        if title in existing_titles:
            continue

        # 跳过排除的论文
        if should_exclude(line.lower()):
            print(f"排除 (不相关): {line[:80]}...")
            continue

        # 只保留核心论文
        if not is_core_paper(line.lower()):
            print(f"排除 (非核心): {line[:80]}...")
            continue

        to_add.append(line)

    return to_add

def insert_papers(readme_content, section_name, new_papers):
    """将新论文插入到指定 section"""
    if not new_papers:
        return readme_content

    # 找到 section 的表格头
    section_pattern = rf'(## {re.escape(section_name)}\n\n\| Year \| Title \|.*?\| Keywords.*?\|\n\| ---- \|.*?\|\n)'
    match = re.search(section_pattern, readme_content)
    if not match:
        print(f"未找到 section: {section_name}")
        return readme_content

    header_end = match.end()

    # 获取 header 后的内容
    rest_content = readme_content[header_end:]

    # 找到第一个论文行的位置
    first_paper_match = re.search(r'\n\|\s*(\d{4})\s*\|', rest_content)
    if first_paper_match:
        # 在 header 和第一个论文之间插入
        insert_pos = header_end + first_paper_match.start()
    else:
        # 如果没有论文，直接在 header 后插入
        insert_pos = header_end

    # 构建要插入的内容
    papers_text = '\n'.join(new_papers)

    # 插入论文
    new_content = readme_content[:insert_pos] + '\n' + papers_text + '\n' + readme_content[insert_pos:]

    return new_content

def main():
    # 读取 README
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # 提取已有的论文标题
    audio_existing = extract_existing_titles(readme_content, 'Audio-driven')
    nerf_existing = extract_existing_titles(readme_content, 'NeRF & 3D & Gaussian Splatting')

    print(f"Audio-driven 已有 {len(audio_existing)} 篇论文")
    print(f"NeRF & 3D & Gaussian Splatting 已有 {len(nerf_existing)} 篇论文")

    # 读取新论文
    audio_new = read_new_papers('new_papers_audio.txt')
    nerf_new = read_new_papers('new_papers_3dgs.txt')

    print(f"\nAudio-driven 新论文文件中有 {len(audio_new)} 篇")
    print(f"NeRF & 3D & Gaussian Splatting 新论文文件中有 {len(nerf_new)} 篇")

    # 过滤论文
    print("\n过滤 Audio-driven 论文:")
    audio_to_add = filter_papers(audio_new, audio_existing)
    print(f"\nAudio-driven 待添加：{len(audio_to_add)} 篇")

    print("\n过滤 NeRF & 3D & Gaussian Splatting 论文:")
    nerf_to_add = filter_papers(nerf_new, nerf_existing)
    print(f"\nNeRF & 3D & Gaussian Splatting 待添加：{len(nerf_to_add)} 篇")

    # 插入论文
    readme_content = insert_papers(readme_content, 'Audio-driven', audio_to_add)
    readme_content = insert_papers(readme_content, 'NeRF & 3D & Gaussian Splatting', nerf_to_add)

    # 保存
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("\n添加完成！")

if __name__ == '__main__':
    main()
