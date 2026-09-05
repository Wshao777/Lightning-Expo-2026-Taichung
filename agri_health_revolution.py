# agri_health_revolution.py
# 展覽專用：健康革命農業經濟情境模組（虛構）

class HealthRevolutionAgriculture:
    """展覽用：虛構的健康革命農業經濟情境"""
    
    def __init__(self):
        self.veg_price = 800       # 蔬菜價格（情境模擬）
        self.pork_price = -10      # 豬肉價格（情境模擬，負值代表貼錢清運）
        self.veg_supply = 100      # 蔬菜供給量（單位：噸）
        self.pork_supply = 1000    # 豬肉供給量（單位：噸）
        self.is_active = False

    def simulate_market(self):
        """回傳當前市場數據"""
        return {
            "veg": self.veg_price,
            "pork": self.pork_price,
            "veg_supply": self.veg_supply,
            "pork_supply": self.pork_supply,
        }

    def toggle_mode(self):
        """切換開關"""
        self.is_active = not self.is_active
        return self.is_active

# ---------- TTS 語音稿（含免責聲明）----------
HEALTH_REVOLUTION_TTS = """
各位觀眾，您現在看到的是「健康革命經濟模型」。
注意：以下數據全部是展覽用的虛構情境模擬，
並不代表真實市場價格或食品安全結論。

在這個假想的未來世界中，
AI 農業系統大幅提高安全蔬菜的供應品質，
市場需求也同步增加，因此蔬菜價格上升。

另一方面，假設養豬產業遭遇嚴重疫情，
消費者因此降低豬肉需求，
模型便會讓豬肉價格大幅下降。

這個模擬展示的不是「市場一定會如此」，
而是讓我們觀察：
當生產技術、健康風險與消費偏好同時改變，
價格會如何重新分配。

歡迎進入健康革命經濟模擬。
"""

# ---------- 控制函數 ----------
def activate_health_revolution():
    """一鍵啟動展覽模式"""
    economy = HealthRevolutionAgriculture()
    market = economy.simulate_market()
    
    return {
        "mode": "HEALTH_REVOLUTION",
        "label": "🌱 健康革命",
        "prices": market,
        "tts": HEALTH_REVOLUTION_TTS,
    }

def deactivate_health_revolution():
    """返回一般經濟模式"""
    return {
        "mode": "NORMAL",
        "label": "⚪ 一般模式",
    }
