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
