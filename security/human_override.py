"""
Lightning 人類最終控制鏈（Human Override Chain）
符合：人類 → 金鑰 → AI → 機器人
並實作緊急停止（E-Stop）機制
"""
import hashlib
import time
from typing import Dict, List, Optional

class HumanOverrideChain:
    def __init__(self, master_key_hash: str):
        self.master_key_hash = master_key_hash
        self.authorized_humans = {
            "Wshao777": {
                "role": "OPS_CENTER",
                "key_hash": master_key_hash,
                "estop_enabled": True
            }
        }
        self.audit_log = []
        self.estop_triggered = False
        self.estop_timestamp = None

    def authenticate_human(self, human_id: str, provided_key: str) -> bool:
        provided_hash = hashlib.sha256(provided_key.encode()).hexdigest()
        if human_id in self.authorized_humans:
            if self.authorized_humans[human_id]["key_hash"] == provided_hash:
                self.audit_log.append(f"[✅ AUTH] {human_id} 驗證成功 @ {time.ctime()}")
                return True
        self.audit_log.append(f"[🚫 AUTH_FAIL] {human_id} 驗證失敗 @ {time.ctime()}")
        return False

    def human_approve_action(self, human_id: str, action: str, key: str) -> bool:
        if not self.authenticate_human(human_id, key):
            raise PermissionError(f"⛔ 人類 [{human_id}] 未授權，無法核准 [{action}]")
        self.audit_log.append(f"[✅ APPROVED] {human_id} 核准了 [{action}] @ {time.ctime()}")
        return True

    def trigger_estop(self, human_id: str, key: str) -> bool:
        if not self.authenticate_human(human_id, key):
            raise PermissionError(f"⛔ 未授權人類 [{human_id}] 試圖觸發 E-Stop")
        self.estop_triggered = True
        self.estop_timestamp = time.ctime()
        self.audit_log.append(f"[🛑 ESTOP] 由 {human_id} 觸發緊急停止 @ {self.estop_timestamp}")
        print("🚨 緊急停止已觸發！所有機器人動作凍結。")
        return True

    def check_estop(self) -> bool:
        if self.estop_triggered:
            self.audit_log.append(f"[⛔ BLOCKED] 動作因 E-Stop 阻擋 @ {time.ctime()}")
        return self.estop_triggered

    def reset_estop(self, human_id: str, key: str) -> bool:
        if not self.authenticate_human(human_id, key):
            raise PermissionError(f"⛔ 未授權人類 [{human_id}] 試圖重置 E-Stop")
        self.estop_triggered = False
        self.audit_log.append(f"[✅ RESET] {human_id} 重置緊急停止 @ {time.ctime()}")
        return True

# 使用範例
if __name__ == "__main__":
    MASTER_KEY = "Wshao777_Ops_Center_Key_2026"
    chain = HumanOverrideChain(hashlib.sha256(MASTER_KEY.encode()).hexdigest())

    chain.human_approve_action("Wshao777", "啟動風力模擬演練", MASTER_KEY)
    chain.trigger_estop("Wshao777", MASTER_KEY)

    if chain.check_estop():
        print("⛔ AI 無法執行，E-Stop 生效中。")

    chain.reset_estop("Wshao777", MASTER_KEY)
    print("\n".join(chain.audit_log))
