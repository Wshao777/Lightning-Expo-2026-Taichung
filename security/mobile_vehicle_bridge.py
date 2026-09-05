# mobile_vehicle_bridge.py
# 手機連線 + TTS 整合伺服器 (FastAPI + WebSocket)

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import asyncio
import json
import uuid
from datetime import datetime

app = FastAPI()

# ========== 車載 TTS 模擬 ==========
class VehicleTTS:
    @staticmethod
    async def speak(text: str, emotion: str = "normal"):
        print(f"🔊 車載語音: {text} (情緒: {emotion})")
        # 未來可接入 ElevenLabs / 百度 API
        return {"status": "spoken", "text": text}

# ========== 配備檢測 ==========
class HardwareDetector:
    @staticmethod
    async def scan_all():
        return {
            "cameras": {"status": "online", "count": 4},
            "lidar": {"status": "online", "distance_range": "200m"},
            "drones": {"status": "ready", "count": 10},
            "battery": {"level": 87, "charging": False},
            "microphone": {"status": "online"},
            "speaker": {"status": "online"}
        }

# ========== WebSocket 管理 ==========
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.device_id = "GODZILLA-TESLA-001"

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for conn in self.active_connections:
            try:
                await conn.send_text(message)
            except:
                pass

manager = ConnectionManager()

# ========== 手機控制網頁 (HTML) ==========
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🦖 哥吉拉車控</title>
    <style>
        body { font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding: 20px; }
        .card { background: #16213e; padding: 20px; border-radius: 20px; margin: 10px 0; }
        button { background: #e94560; border: none; padding: 15px 30px; margin: 8px; border-radius: 50px; color: white; font-size: 18px; cursor: pointer; }
        .status-online { color: #00ff88; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    </style>
</head>
<body>
    <h1>🦖 哥吉拉超級特斯拉</h1>
    <div class="card" id="statusCard">🔗 連線中 ...</div>
    
    <div class="grid">
        <button onclick="sendCmd('navigate', '台中市政府')">🧭 導航</button>
        <button onclick="sendCmd('mode', 'sport')">🏎️ 運動模式</button>
        <button onclick="sendCmd('mode', 'beast')">🔥 怪獸模式</button>
        <button onclick="sendCmd('drone', 'formation_circle')">✈️ 無人機編隊</button>
        <button onclick="sendCmd('speak', '你好，我是哥吉拉')">🗣️ 語音測試</button>
        <button onclick="sendCmd('scan', 'hardware')">📡 掃描配備</button>
    </div>

    <div class="card" id="hardwareInfo">
        <h3>📋 配備狀態</h3>
        <div id="hwList">點擊「掃描配備」更新</div>
    </div>

    <div class="card" id="logArea" style="height:150px; overflow-y:scroll; text-align:left; font-size:14px;">
        📝 系統日誌...
    </div>

    <script>
        let ws;
        function connect() {
            ws = new WebSocket(`ws://${window.location.host}/ws`);
            ws.onopen = () => document.getElementById('statusCard').innerHTML = '✅ 已連線至車輛';
            ws.onclose = () => document.getElementById('statusCard').innerHTML = '❌ 斷線，重新連線中...';
            ws.onmessage = (e) => {
                const data = JSON.parse(e.data);
                if (data.type === 'log') {
                    document.getElementById('logArea').innerHTML += `<br>🟢 ${data.msg}`;
                    document.getElementById('logArea').scrollTop = document.getElementById('logArea').scrollHeight;
                }
                if (data.type === 'hardware_scan') {
                    let html = '';
                    for (let [k, v] of Object.entries(data.data)) {
                        html += `<p>${k}: <span class="status-online">${v.status}</span> (${v.count || v.level || ''})</p>`;
                    }
                    document.getElementById('hwList').innerHTML = html;
                }
            };
        }
        window.onload = connect;

        function sendCmd(action, payload) {
            if (ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({ action, payload }));
            } else {
                alert('車輛未連線');
            }
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get_mobile_panel():
    return HTMLResponse(HTML_PAGE)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await websocket.send_json({"type": "log", "msg": "手機已連線，系統就緒"})
    
    try:
        while True:
            data = await websocket.receive_text()
            cmd = json.loads(data)
            action = cmd.get("action")
            payload = cmd.get("payload")

            # ---------- 處理指令 ----------
            if action == "navigate":
                await VehicleTTS.speak(f"導航至 {payload}")
                await manager.broadcast(json.dumps({"type": "log", "msg": f"🧭 導航中: {payload}"}))

            elif action == "mode":
                await VehicleTTS.speak(f"切換至 {payload} 模式")
                await manager.broadcast(json.dumps({"type": "log", "msg": f"🚗 模式切換: {payload}"}))

            elif action == "speak":
                await VehicleTTS.speak(payload, emotion="excited")
                await manager.broadcast(json.dumps({"type": "log", "msg": f"🗣️ TTS播報: {payload}"}))

            elif action == "scan":
                hw = await HardwareDetector.scan_all()
                await websocket.send_json({"type": "hardware_scan", "data": hw})
                await manager.broadcast(json.dumps({"type": "log", "msg": "📡 配備掃描完成"}))

            elif action == "drone":
                await VehicleTTS.speak(f"無人機 {payload}")
                await manager.broadcast(json.dumps({"type": "log", "msg": f"✈️ 無人機指令: {payload}"}))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(json.dumps({"type": "log", "msg": "📱 手機已斷線"}))

# ========== 啟動 ==========
if __name__ == "__main__":
    import uvicorn
    print("🦖 哥吉拉車載伺服器啟動中...")
    print("📱 請在同一網段用手機瀏覽器打開: http://<你的IP>:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
