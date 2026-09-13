# fb/ad_manager.py
import os
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

load_dotenv()

class FacebookAdManager:
    def __init__(self):
        FacebookAdsApi.init(
            access_token=os.getenv("FB_ACCESS_TOKEN"),
            app_id=os.getenv("FB_APP_ID"),
            app_secret=os.getenv("FB_APP_SECRET")
        )
        self.ad_account_id = os.getenv("FB_AD_ACCOUNT_ID")

    def create_campaign(self, name: str, objective: str = "OUTCOME_TRAFFIC",
                        daily_budget: int = 200, status: str = "PAUSED"):
        """建立廣告活動（預設 PAUSED，避免意外消費）"""
        account = AdAccount(f"act_{self.ad_account_id}")
        params = {
            "name": name,
            "objective": objective,
            "status": status,
            "daily_budget": daily_budget,
            "special_ad_categories": []
        }
        campaign = account.create_campaign(params=params)
        print(f"✅ 廣告活動建立成功：{campaign.get('id')}")
        return campaign

    def get_campaign_insights(self, campaign_id: str):
        """取得廣告活動成效數據"""
        campaign = Campaign(campaign_id)
        insights = campaign.get_insights(
            fields=["impressions", "clicks", "spend", "ctr", "cpc"]
        )
        return insights
