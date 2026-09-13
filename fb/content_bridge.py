from pathlib import Path
import json


class ContentBridge:
    """Lightning Expo → OPER AI → Facebook 內容橋接"""

    def __init__(self, source_root):
        self.source_root = Path(source_root)

    def read_markdown(self, filename):
        path = self.source_root / filename

        if not path.exists():
            raise FileNotFoundError(f"找不到文件：{path}")

        return path.read_text(encoding="utf-8")

    def build_post(self, source_text, topic="OPER AI"):
        return {
            "topic": topic,
            "source": "Lightning-Expo-2026-Taichung",
            "content": source_text,
            "status": "draft",
            "requires_human_review": True,
        }

    def save_draft(self, post, output="data/fb_draft.json"):
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(post, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        return str(path)
        from pathlib import Path
import json


class ContentBridge:
    """Lightning Expo → OPER AI → Facebook 內容橋接"""

    def __init__(self, source_root):
        self.source_root = Path(source_root)

    def read_markdown(self, filename):
        path = self.source_root / filename

        if not path.exists():
            raise FileNotFoundError(f"找不到文件：{path}")

        return path.read_text(encoding="utf-8")

    def build_post(self, source_text, topic="OPER AI"):
        return {
            "topic": topic,
            "source": "Lightning-Expo-2026-Taichung",
            "content": source_text,
            "status": "draft",
            "requires_human_review": True,
        }

    def save_draft(self, post, output="data/fb_draft.json"):
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(post, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        return str(path)
# fb/content_bridge.py
import re

def markdown_to_fb_post(md_content: str) -> str:
    """將 Markdown 內容轉換為 Facebook 貼文格式"""
    
    # 移除 YAML front matter
    md_content = re.sub(r'^---[\s\S]*?---\n', '', md_content)
    
    # 移除圖片語法，保留 alt 文字
    md_content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', md_content)
    
    # 轉換連結為 "文字 (網址)" 格式
    md_content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'\1 (\2)', md_content)
    
    # 移除標題符號，轉為大寫
    md_content = re.sub(r'^#{1,6}\s+(.+)$', lambda m: m.group(1).upper(), md_content, flags=re.MULTILINE)
    
    # 轉換粗體
    md_content = re.sub(r'\*\*(.+?)\*\*', r'\1', md_content)
    md_content = re.sub(r'\*(.+?)\*', r'\1', md_content)
    
    # 移除程式碼區塊標記
    md_content = re.sub(r'```[\s\S]*?```', '', md_content)
    md_content = re.sub(r'`(.+?)`', r'\1', md_content)
    
    # 壓縮多餘空行
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    return md_content.strip()

def extract_title(md_content: str) -> str:
    """從 Markdown 中提取第一個標題作為貼文標題"""
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    return match.group(1) if match else "無標題"

def extract_hashtags(md_content: str) -> list:
    """提取或生成適合的 Hashtag"""
    tags = ["#OPER", "#AI", "#技術自主"]
    if "台中" in md_content or "Taichung" in md_content:
        tags.extend(["#台中", "#LightningExpo2026"])
    if "防災" in md_content or "能源" in md_content:
        tags.append("#防災科技")
    return tags

def build_fb_post(md_content: str) -> str:
    """組合完整的 Facebook 貼文"""
    title = extract_title(md_content)
    body = markdown_to_fb_post(md_content)
    hashtags = " ".join(extract_hashtags(md_content))
    return f"【{title}】\n\n{body}\n\n{hashtags}"
