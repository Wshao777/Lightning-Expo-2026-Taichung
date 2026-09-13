import os
import requests


class MetaPublisher:
    """
    Meta 官方 API 發布介面。

    不保存密碼。
    不模擬瀏覽器。
    不製造假互動。
    """

    def __init__(self):
        self.page_id = os.getenv("FB_PAGE_ID")
        self.access_token = os.getenv("FB_PAGE_ACCESS_TOKEN")

        if not self.page_id or not self.access_token:
            raise RuntimeError(
                "未設定 Meta Page ID / Access Token。"
            )

    def publish(self, message):
        url = f"https://graph.facebook.com/vXX.X/{self.page_id}/feed"

        response = requests.post(
            url,
            data={
                "message": message,
                "access_token": self.access_token,
            },
            timeout=30,
        )

        response.raise_for_status()
        return response.json()
# fb/publisher.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FacebookPublisher:
    def __init__(self):
        self.page_id = os.getenv("FB_PAGE_ID")
        self.access_token = os.getenv("FB_PAGE_ACCESS_TOKEN")
        if not self.page_id or not self.access_token:
            raise ValueError("❌ 請在 .env 中設定 FB_PAGE_ID 與 FB_PAGE_ACCESS_TOKEN")
        self.base_url = "https://graph.facebook.com/v19.0"

    def publish_text(self, message: str, link: str = None):
        """發布純文字或帶連結的貼文"""
        url = f"{self.base_url}/{self.page_id}/feed"
        payload = {"message": message, "access_token": self.access_token}
        if link:
            payload["link"] = link
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ 發布成功！貼文 ID: {result.get('id')}")
            return result
        else:
            print(f"❌ 發布失敗：{response.text}")
            return None

    def get_post_insights(self, post_id: str):
        """取得貼文洞察數據"""
        metrics = ["post_impressions", "post_engaged_users", "post_reactions_by_type_total"]
        url = f"{self.base_url}/{post_id}/insights"
        params = {"metric": ",".join(metrics), "access_token": self.access_token}
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None
