# ai/oper_ai.py
import os
import requests

def generate_oper_content(topic: str, md_content: str = None) -> str:
    """呼叫 AI 生成 OPER 品牌風格的貼文"""
    api_key = os.getenv("OPENAI_API_KEY")  # 或其他 AI 服務
    if not api_key:
        # 無 AI Key 時使用 Markdown 直接轉換
        from fb.content_bridge import build_fb_post
        return build_fb_post(md_content) if md_content else topic

    prompt = f"""你是「元才」品牌的 AI 內容總監。品牌核心：技術自主 (Sovereign Core)、
拒絕依賴、民間技術交流。
請根據以下主題撰寫一篇 Facebook 貼文（200-300 字，繁體中文）：
主題：{topic}
"""
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]
