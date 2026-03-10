#!/usr/bin/env python3
"""
检查 README 中已存在的论文，找出需要添加的新论文
"""

import re

def extract_paper_titles(readme_content, section_name):
    """从指定 section 中提取论文标题"""
    titles = set()

    # 找到 section 的内容
    section_pattern = rf'## {re.escape(section_name)}\n(.*?)(?=\n## |\Z)'
    section_match = re.search(section_pattern, readme_content, re.DOTALL)

    if not section_match:
        return titles

    section_content = section_match.group(1)

    # 提取所有论文行 (以 | 20 开头的行)
    paper_pattern = r'\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]'
    for match in re.finditer(paper_pattern, section_content):
        year = match.group(1)
        title = match.group(2).lower()
        # 只保留标题的主要部分 (冒号前或主标题)
        titles.add(title)

    return titles

def extract_new_papers(filename):
    """从新论文文件中提取论文"""
    papers = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('| 20'):
                # 提取年份和标题
                match = re.match(r'\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]', line)
                if match:
                    year = match.group(1)
                    title = match.group(2).lower()
                    papers.append((year, title, line))
    return papers

def main():
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # 提取 README 中已有的论文标题
    audio_titles = extract_paper_titles(readme_content, 'Audio-driven')
    nerf_titles = extract_paper_titles(readme_content, 'NeRF & 3D & Gaussian Splatting')

    print(f"Audio-driven 部分已有 {len(audio_titles)} 篇论文")
    print(f"NeRF & 3D & Gaussian Splatting 部分已有 {len(nerf_titles)} 篇论文")

    # 检查新论文
    audio_new_papers = extract_new_papers('new_papers_audio.txt')
    nerf_new_papers = extract_new_papers('new_papers_3dgs.txt')

    # 找出需要添加的论文
    audio_to_add = []
    for year, title, line in audio_new_papers:
        if title not in audio_titles:
            audio_to_add.append((year, line))

    nerf_to_add = []
    for year, title, line in nerf_new_papers:
        if title not in nerf_titles:
            nerf_to_add.append((year, line))

    print(f"\nAudio-driven 需要添加 {len(audio_to_add)} 篇论文:")
    for year, line in sorted(audio_to_add, reverse=True):
        print(f"  {year}: {line[:100]}...")

    print(f"\nNeRF & 3D & Gaussian Splatting 需要添加 {len(nerf_to_add)} 篇论文:")
    for year, line in sorted(nerf_to_add, reverse=True):
        print(f"  {year}: {line[:100]}...")

    return audio_to_add, nerf_to_add

if __name__ == '__main__':
    main()
