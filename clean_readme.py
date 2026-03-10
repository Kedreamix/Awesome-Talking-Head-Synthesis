#!/usr/bin/env python3
"""
清理 README.md，移除不相关的论文
"""

# 需要排除的关键词（不相关的论文）
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
    'diagrammatic learning', 'proactive agentic', 'whiteboards'
]

# 必须包含的核心关键词
CORE_KEYWORDS = [
    'talking head', 'talking face', 'talking portrait', 'talking avatar',
    'talking human', 'talking body',
    'face animation', 'facial animation', 'portrait animation',
    'lip sync', 'lip-sync', 'lipsync', 'lip-synchronization',
    'avatar animation', 'avatar video',
    'human animation', 'head animation',
    'face generation', 'facial generation', 'portrait generation',
    'voice2face', 'voice-to-face', 'audio-to-face',
    'audio-driven', 'speech-driven'
]

def should_exclude(title_lower):
    """判断论文是否应该排除"""
    for kw in EXCLUDE_KEYWORDS:
        if kw in title_lower:
            return True
    return False

def is_core_paper(title_lower):
    """判断是否是核心 talking head 论文"""
    for kw in CORE_KEYWORDS:
        if kw in title_lower:
            return True
    return False

def clean_section(content, section_name):
    """清理指定部分"""
    lines = content.split('\n')
    cleaned_lines = []
    in_section = False
    excluded_count = 0
    kept_count = 0

    for line in lines:
        # 检查是否进入目标 section
        if line.startswith(f'## {section_name}'):
            in_section = True
            cleaned_lines.append(line)
            continue

        # 检查是否进入下一个 section
        if line.startswith('## ') and in_section:
            in_section = False
            cleaned_lines.append(line)
            continue

        if in_section and line.startswith('| 20'):
            title_lower = line.lower()

            # 跳过排除的论文
            if should_exclude(title_lower):
                excluded_count += 1
                continue

            # 只保留核心 talking head 论文
            if is_core_paper(title_lower):
                cleaned_lines.append(line)
                kept_count += 1
            else:
                excluded_count += 1
        else:
            cleaned_lines.append(line)

    print(f"{section_name}: 保留了 {kept_count} 篇论文，排除了 {excluded_count} 篇论文")
    return '\n'.join(cleaned_lines)

def main():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 清理 Audio-driven 部分
    content = clean_section(content, 'Audio-driven')

    # 清理 NeRF & 3D & Gaussian Splatting 部分
    content = clean_section(content, 'NeRF & 3D & Gaussian Splatting')

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("清理完成！")

if __name__ == '__main__':
    main()
