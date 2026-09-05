#!/usr/bin/env python3
"""
展覽申請自助產生器 (Exhibition Application Assistant)
用途：產生「AI × OPER × BOT 技術展示」展覽申請草稿
"""

import datetime

def generate_application_draft():
    print("⚡ 展覽申請資料產生器 (草稿)")
    print("=" * 50)

    # 1. 基本資訊
    print("\n--- 1. 活動基本資訊 ---")
    event_name = "AI × OPER × BOT Technology Expo 2026"
    organizer = "Lightning Empire / 你的法人名稱"
    contact_person = "Wshao777"
    contact_email = "Wshao777opscenter@gmail.com"
    start_date = "2026-09-08"
    end_date = "2026-09-13"

    print(f"活動名稱：{event_name}")
    print(f"主辦單位：{organizer}")
    print(f"聯絡人：{contact_person}")
    print(f"聯絡信箱：{contact_email}")
    print(f"展覽日期：{start_date} 至 {end_date}")

    # 2. 展示內容與技術簡介
    print("\n--- 2. 展示內容與技術簡介 ---")
    description = """
    本展示為「技術研究與概念驗證（PoC）」活動，旨在呈現多智能體協作、AI治理與Bot控制的前沿技術。
    展示內容包含：
    - GPT系列AI能力展示 (公開技術介紹)
    - OPER AI協作、治理與驗證架構
    - xAI、Tesla AI公開技術資訊介紹 (均為公開資料展示，無未授權宣稱)
    - 合法取得或自有的機器人(BOT)原型Demo
    - 多AI模型比較與協作概念演示
    - 風力/災害模擬系統 (DISASTER AI)
    - 安全權限、審計日誌與人類確認機制

    **核心原則**：AI 建議 → 人類確認 → 授權 BOT 執行
    **活動屬性**：全場為模擬展示 (SIMULATION ONLY / DEMO)，不對外控制任何第三方機器人或系統。
    """
    print(description)

    # 3. 場地與設備需求
    print("\n--- 3. 場地與設備需求 ---")
    equipment = """
    - 展覽面積需求：約 2-4 個標準攤位 (或依實際規劃)
    - 電力需求：一般110V/220V插座，需獨立電源迴路
    - 網路需求：穩定Wi-Fi或有線網路
    - 桌椅需求：展示桌2-4張、椅子4-6張
    """
    print(equipment)

    # 4. 安全與責任聲明
    print("\n--- 4. 安全與責任聲明 ---")
    safety_statement = """
    1. 活動全程遵守TICEC場地管理規範及中華民國相關法律。
    2. 所有動態展示均設有安全防護措施與人員操作。
    3. **明確聲明**：本活動不直接控制或連接任何第三方機器人、車輛或基礎設施，所有互動均為預設腳本或模擬模式。
    4. 活動已規劃相應之公共意外責任保險。
    """
    print(safety_statement)

    # 5. 申請文件清單
    print("\n--- 5. 應備申請文件清單 ---")
    print("請務必向TICEC官方確認最新規定，以下為常見文件：")
    checklist = [
        "1. 展覽場地預約申請表 (向TICEC索取最新版)",
        "2. 詳細活動企劃書 (含展示內容、流程、場地規劃)",
        "3. 公司/法人登記證明文件",
        "4. 活動安全計畫書",
        "5. 保險證明文件",
        "6. 展場攤位配置圖 (初步規劃)"
    ]
    for item in checklist:
        print(f"- {item}")

    print("\n" + "=" * 50)
    print("✅ 草稿產生完成！")
    print("請將以上資訊填入正式申請表，並聯繫TICEC官方確認申請細節。")

if __name__ == "__main__":
    generate_application_draft()
