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
