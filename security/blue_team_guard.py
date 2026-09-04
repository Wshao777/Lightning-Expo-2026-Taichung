"""
Lightning 藍軍判別器（Blue Team Guard）
僅允許經人類核准的「藍軍節點」執行敏感操作
紅軍（未授權外部連線）一律阻擋
"""
import hashlib
from typing import Dict, List

# 藍軍白名單（由 Wshao777 核准）
BLUE_TEAM_WHITELIST = [
    "LightningEmperor_bot",
    "DonLightning_Bot",
    "FurThunderBoss_bot",
    "flash_ultimate2025_bot",
    "ThunderFlash77_Bot",
    "LoanIntegration_bot",
    "lightinggithub_bot",
    "Lightninggithu_bot",
    "stormcar820_bot",
    "Electric_SparkBot_01bot",
    "AIThunderBot",
    "Grok_Analyzer_Bot",
    "Fazerrr4_bot",
    "LightningEmpire_bot",
    "grokai_bot",
    "Commandertetris_bot",
    "Phantom_Sparks_TetrisBot",
    "Lightning_tetris_bot",
    "Thundertetris_bot",
    "lightning_empire2025_bot",
    # 四大核心（風火水火星）
    "Wind_Core",
    "Fire_Core",
    "Water_Core",
    "Mars_Core",
    # 人類最終節點
    "Wshao777_OPS_CENTER"
]

class BlueTeamGuard:
    def __init__(self):
        self.whitelist = set(BLUE_TEAM_WHITELIST)
        self.audit_log = []

    def is_blue_team(self, node_id: str) -> bool:
        """檢查節點是否為藍軍（合法內部節點）"""
        return node_id in self.whitelist

    def enforce_blue_only(self, node_id: str, action: str) -> bool:
        """強制僅允許藍軍執行敏感動作"""
        if self.is_blue_team(node_id):
            self.audit_log.append(f"[✅ BLUE_ALLOW] {node_id} -> {action}")
            return True
        else:
            self.audit_log.append(f"[🚫 RED_BLOCK] {node_id} 試圖執行 {action}，已阻擋")
            raise PermissionError(f"⛔ 紅軍節點 [{node_id}] 無權執行 [{action}]。僅限藍軍節點。")

    def get_audit_report(self) -> List[str]:
        """回傳稽核紀錄"""
        return self.audit_log

# 使用範例
if __name__ == "__main__":
    guard = BlueTeamGuard()
    try:
        guard.enforce_blue_only("LightningEmperor_bot", "啟動風力模擬")
        guard.enforce_blue_only("unknown_china_bot", "讀取風機座標")  # 這會失敗
    except PermissionError as e:
        print(e)
    print(guard.get_audit_report())
