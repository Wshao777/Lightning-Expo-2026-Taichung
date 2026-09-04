# Lightning-Expo-2026-Taichung
AI-OPER-BOT-Expo-2026
好的，收到。你現在要為這個公開展覽建立一個專門的 GitHub 倉庫，用來存放所有展示相關的文件、程式碼與企劃書。

根據你的要求，我幫你整理了一份完整的倉庫命名與文件結構建議，你可以直接沿用或修改：

---我已經為你的 Lightning-Expo-2026-Taichung 倉庫準備好了「本對話最終程式碼」的完整補全方案。

以下是這次新增的完整檔案結構與內容說明，你可以直接複製貼上到你的 GitHub 倉庫中。

⚡ 新增檔案總對，懂了。你要的是後台控制程式碼 + 前台 HTML 按鈕自動化，不是把程式碼拿給觀眾看。

可以做成這個架構好的，我完全理解你的需求。你要的是一个后台控制面板——也就是展场工作人员（你）操作的核心界面。观众看到的是展示效果，而你看到的是这个带按钮、能触发自动化流程的控制台。

下面是你要的后台控制程序代码，它是一个可以直接运行的 HTML 文件，包含了：

1. 核心流程按钮：一键触发"AI 建议 → OPER AI 协同 → 等待人类确认 → BOT 执行 → 显示结果"的完整演示。
2. 实时状态显示：展示每个步骤的执行状态和审计日志。
3. 全屏自适应：适合在展场的大屏幕上操作。

你可以直接把下面的代码保存为 control_panel.html，放在你的 Lightning-Expo-2026-Taichung 仓库根目录下，和 index.html 并列。这样你就有"观众看的展示页"和"工作人员用的控制页"两个界面了。

---

⚡ 后台控制程序代码 (control_panel.html)

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ 后台控制面板 · Lightning Expo 2026</title>
    <style>
        /* 簡潔、科技感的控制台樣式 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: #0b0e14;
            color: #e0e6f0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .panel {
            max-width: 1000px;
            width: 100%;
            background: #141a24;
            border: 1px solid #2a3444;
            border-radius: 24px;
            padding: 40px 35px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        }
        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f5a623;
            padding-bottom: 16px;
            margin-bottom: 30px;
        }
        .panel-header h1 {
            font-size: 1.8rem;
            font-weight: 600;
            color: #f5a623;
            letter-spacing: 1px;
        }
        .panel-header .badge {
            background: #1e2636;
            color: #a0b4c8;
            padding: 6px 16px;
            border-radius: 30px;
            font-size: 0.8rem;
            border: 1px solid #2e3a4e;
        }
        .status-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        .status-item {
            background: #0f131c;
            padding: 16px 20px;
            border-radius: 12px;
            border-left: 4px solid #2e3a4e;
        }
        .status-item .label {
            font-size: 0.75rem;
            text-transform: uppercase;
            color: #7a8fa3;
            letter-spacing: 0.5px;
        }
        .status-item .value {
            font-size: 1.1rem;
            font-weight: 500;
            margin-top: 4px;
            font-family: 'Courier New', monospace;
        }
        .status-item .value.idle { color: #7a8fa3; }
        .status-item .value.running { color: #f5a623; }
        .status-item .value.done { color: #4caf50; }
        .status-item .value.error { color: #f44336; }

        .flow-visual {
            background: #0f131c;
            border-radius: 16px;
            padding: 24px 20px;
            margin-bottom: 30px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
            gap: 8px 12px;
            border: 1px solid #1e2636;
        }
        .flow-step {
            background: #1a212e;
            padding: 10px 18px;
            border-radius: 40px;
            font-size: 0.9rem;
            font-weight: 500;
            color: #a0b4c8;
            border: 1px solid #2a3444;
            transition: all 0.3s;
        }
        .flow-step.active {
            border-color: #f5a623;
            color: #f5a623;
            background: #1e2636;
            box-shadow: 0 0 12px rgba(245, 166, 35, 0.15);
        }
        .flow-step.done {
            border-color: #4caf50;
            color: #4caf50;
        }
        .flow-arrow {
            color: #3a4a5e;
            font-weight: 300;
            font-size: 1.2rem;
        }

        .action-area {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 25px;
        }
        .btn {
            background: #1e2636;
            border: none;
            color: #e0e6f0;
            padding: 14px 32px;
            border-radius: 40px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid #2a3444;
            flex: 1 1 auto;
        }
        .btn:hover:not(:disabled) {
            background: #2a3444;
            border-color: #f5a623;
        }
        .btn:disabled {
            opacity: 0.4;
            cursor: not-allowed;
        }
        .btn-primary {
            background: #f5a623;
            color: #0b0e14;
            border-color: #f5a623;
        }
        .btn-primary:hover:not(:disabled) {
            background: #e0961a;
            border-color: #e0961a;
        }
        .btn-danger {
            border-color: #f44336;
            color: #f44336;
        }
        .btn-danger:hover:not(:disabled) {
            background: #f44336;
            color: #0b0e14;
        }

        .log-area {
            background: #0a0d12;
            border-radius: 12px;
            padding: 16px 20px;
            max-height: 160px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            line-height: 1.7;
            border: 1px solid #1a1f2e;
            margin-top: 10px;
        }
        .log-area .log-entry {
            color: #7a8fa3;
            border-bottom: 1px solid #141a24;
            padding: 4px 0;
        }
        .log-area .log-entry .time {
            color: #3a4a5e;
            margin-right: 14px;
        }
        .log-area .log-entry .ok { color: #4caf50; }
        .log-area .log-entry .warn { color: #f5a623; }
        .log-area .log-entry .err { color: #f44336; }

        .footnote {
            margin-top: 20px;
            text-align: center;
            font-size: 0.75rem;
            color: #3a4a5e;
            border-top: 1px solid #1a1f2e;
            padding-top: 18px;
        }

        /* RWD */
        @media (max-width: 700px) {
            .panel { padding: 24px 16px; }
            .status-grid { grid-template-columns: 1fr; }
            .action-area { flex-direction: column; }
            .flow-visual { gap: 4px 8px; }
            .flow-step { font-size: 0.75rem; padding: 6px 12px; }
        }
    </style>
</head>
<body>

<div class="panel">
    <!-- 標頭 -->
    <div class="panel-header">
        <h1>⚡ 後台控制 · OPER AI</h1>
        <span class="badge">展覽模式 · v1.0</span>
    </div>

    <!-- 即時狀態 -->
    <div class="status-grid">
        <div class="status-item">
            <div class="label">🤖 當前階段</div>
            <div class="value idle" id="phaseDisplay">待命</div>
        </div>
        <div class="status-item">
            <div class="label">✅ 最後確認</div>
            <div class="value idle" id="confirmDisplay">—</div>
        </div>
        <div class="status-item">
            <div class="label">⏱️ 流程狀態</div>
            <div class="value idle" id="statusDisplay">就緒</div>
        </div>
        <div class="status-item">
            <div class="label">📋 授權模式</div>
            <div class="value idle" id="authDisplay">👤 人類核准</div>
        </div>
    </div>

    <!-- 視覺化流程 -->
    <div class="flow-visual" id="flowVisual">
        <span class="flow-step" id="stepAI">🧠 AI 建議</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step" id="stepOPER">⚙️ OPER 協作</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step" id="stepHuman">👤 人類確認</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step" id="stepBOT">🤖 授權 BOT</span>
        <span class="flow-arrow">→</span>
        <span class="flow-step" id="stepResult">✅ Demo 結果</span>
    </div>

    <!-- 操作按鈕 -->
    <div class="action-area">
        <button class="btn btn-primary" id="btnStart">🚀 啟動自動化流程</button>
        <button class="btn" id="btnReset" disabled>⟳ 重置</button>
        <button class="btn btn-danger" id="btnEStop">⛔ 緊急停止</button>
    </div>

    <!-- 審計日誌 -->
    <div class="log-area" id="logArea">
        <div class="log-entry"><span class="time">[系統]</span> 控制台已就緒，等待指令。</div>
        <div class="log-entry"><span class="time">[系統]</span> 核心原則：AI 建議 → 人類確認 → 授權 BOT 執行</div>
    </div>

    <div class="footnote">
        DEMO · SIMULATION ONLY · NOT CONNECTED · NO UNAUTHORIZED CONTROL
    </div>
</div>

<script>
    (function() {
        "use strict";

        // DOM 元素
        const phaseDisplay = document.getElementById('phaseDisplay');
        const confirmDisplay = document.getElementById('confirmDisplay');
        const statusDisplay = document.getElementById('statusDisplay');
        const authDisplay = document.getElementById('authDisplay');
        const logArea = document.getElementById('logArea');

        const stepAI = document.getElementById('stepAI');
        const stepOPER = document.getElementById('stepOPER');
        const stepHuman = document.getElementById('stepHuman');
        const stepBOT = document.getElementById('stepBOT');
        const stepResult = document.getElementById('stepResult');

        const btnStart = document.getElementById('btnStart');
        const btnReset = document.getElementById('btnReset');
        const btnEStop = document.getElementById('btnEStop');

        // 狀態變數
        let isRunning = false;
        let isEStop = false;
        let currentStep = 0; // 0=idle, 1=AI, 2=OPER, 3=Human, 4=BOT, 5=Result
        let timer = null;
        let logCount = 0;

        // === 輔助函式 ===
        function resetAllSteps() {
            [stepAI, stepOPER, stepHuman, stepBOT, stepResult].forEach(el => {
                el.classList.remove('active', 'done');
            });
        }

        function setStepActive(index) {
            resetAllSteps();
            const steps = [stepAI, stepOPER, stepHuman, stepBOT, stepResult];
            for (let i = 0; i < steps.length; i++) {
                if (i < index) steps[i].classList.add('done');
                else if (i === index) steps[i].classList.add('active');
            }
        }

        function setPhase(text, type = 'idle') {
            phaseDisplay.textContent = text;
            phaseDisplay.className = 'value ' + type;
        }

        function setStatus(text, type = 'idle') {
            statusDisplay.textContent = text;
            statusDisplay.className = 'value ' + type;
        }

        function setConfirm(text) {
            confirmDisplay.textContent = text;
        }

        function addLog(message, type = 'info') {
            const time = new Date().toLocaleTimeString('zh-TW', { hour12: false });
            const entry = document.createElement('div');
            entry.className = 'log-entry';
            let cls = '';
            if (type === 'ok') cls = 'ok';
            else if (type === 'warn') cls = 'warn';
            else if (type === 'err') cls = 'err';
            entry.innerHTML = `<span class="time">[${time}]</span> <span class="${cls}">${message}</span>`;
            logArea.appendChild(entry);
            logArea.scrollTop = logArea.scrollHeight;
            logCount++;
            // 限制日誌數量，避免過長
            if (logCount > 80) {
                const first = logArea.querySelector('.log-entry');
                if (first) first.remove();
                logCount--;
            }
        }

        // === 重置控制台 ===
        function resetPanel() {
            if (timer) {
                clearTimeout(timer);
                timer = null;
            }
            isRunning = false;
            currentStep = 0;
            setPhase('待命', 'idle');
            setStatus('就緒', 'idle');
            setConfirm('—');
            authDisplay.textContent = '👤 人類核准';
            authDisplay.className = 'value idle';
            resetAllSteps();
            btnStart.disabled = false;
            btnReset.disabled = true;
            addLog('系統已重置，回到待命狀態。', 'warn');
        }

        // === 模擬「人類確認」對話 ===
        function askHumanConfirmation() {
            return new Promise((resolve) => {
                setPhase('等待人類確認', 'running');
                setStatus('請按下「確認」按鈕', 'running');
                authDisplay.textContent = '⏳ 等待確認';
                authDisplay.className = 'value running';
                addLog('👤 請求人類確認：是否授權 BOT 執行此任務？', 'warn');

                // 建立一個臨時確認按鈕（UI 上直接修改按鈕功能）
                const originalText = btnStart.textContent;
                btnStart.textContent = '✅ 確認執行 (人類)';
                btnStart.disabled = false;
                btnStart.className = 'btn btn-primary';
                btnStart.style.background = '#4caf50';
                btnStart.style.borderColor = '#4caf50';

                const handler = () => {
                    btnStart.textContent = originalText;
                    btnStart.className = 'btn btn-primary';
                    btnStart.style.background = '';
                    btnStart.style.borderColor = '';
                    btnStart.removeEventListener('click', handler);
                    setConfirm('✅ 已確認 (Wshao777)');
                    authDisplay.textContent = '✅ 已授權';
                    authDisplay.className = 'value done';
                    addLog('✅ 人類確認完成，授權 BOT 執行。', 'ok');
                    resolve(true);
                };
                btnStart.addEventListener('click', handler);

                // 同時也監聽 EStop 中斷
                const estopHandler = () => {
                    btnStart.removeEventListener('click', handler);
                    btnStart.textContent = originalText;
                    btnStart.className = 'btn btn-primary';
                    btnStart.style.background = '';
                    btnStart.style.borderColor = '';
                    btnStart.removeEventListener('click', estopHandler);
                    addLog('⛔ 人類確認被緊急停止中斷。', 'err');
                    resolve(false);
                };
                btnEStop.addEventListener('click', estopHandler, { once: true });
            });
        }

        // === 主要流程 ===
        async function runAutomation() {
            if (isRunning) return;
            if (isEStop) {
                addLog('⛔ 系統處於緊急停止狀態，無法啟動。', 'err');
                return;
            }

            // 重置到初始狀態
            resetPanel();
            isRunning = true;
            btnStart.disabled = true;
            btnReset.disabled = true;
            addLog('🚀 啟動自動化流程...', 'ok');

            // Step 1: AI 建議
            setPhase('AI 分析中', 'running');
            setStatus('正在生成建議...', 'running');
            setStepActive(0);
            addLog('🧠 AI 建議：基於風力數據與風險模型，建議執行「降載保護」程序。', 'info');
            await sleep(1200);

            // Step 2: OPER AI 協作
            setPhase('OPER 協作中', 'running');
            setStatus('多 Agent 協同驗證...', 'running');
            setStepActive(1);
            addLog('⚙️ OPER AI 協作完成：驗證通過，風險係數 0.23，建議人類核准。', 'ok');
            await sleep(1000);

            // Step 3: 人類確認
            setStepActive(2);
            const confirmed = await askHumanConfirmation();
            if (!confirmed) {
                // 被 EStop 或取消
                isRunning = false;
                btnStart.disabled = false;
                btnReset.disabled = false;
                setPhase('已中斷', 'error');
                setStatus('流程中斷', 'error');
                return;
            }

            // Step 4: 授權 BOT 執行
            setStepActive(3);
            setPhase('BOT 執行中', 'running');
            setStatus('正在派發指令...', 'running');
            addLog('🤖 BOT 已接收指令，執行模擬降載動作 (DEMO MODE)。', 'ok');
            await sleep(1500);

            // Step 5: Demo 結果
            setStepActive(4);
            setPhase('✅ 完成', 'done');
            setStatus('展示成功', 'done');
            addLog('✅ Demo 結果：風機模擬降載至 75%，系統狀態正常。', 'ok');
            addLog('📋 審計紀錄：已寫入 audit.log (時間戳記、操作者、結果)。', 'info');

            // 完成
            isRunning = false;
            btnStart.disabled = false;
            btnReset.disabled = false;
            authDisplay.textContent = '✅ 已授權 (已完成)';
            authDisplay.className = 'value done';
            setConfirm('✅ 已確認 (Wshao777)');
            addLog('🏁 自動化流程結束。', 'warn');
        }

        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        // === 緊急停止 ===
        function triggerEStop() {
            if (isEStop) {
                addLog('⛔ 系統已處於緊急停止狀態。', 'err');
                return;
            }
            isEStop = true;
            if (isRunning) {
                // 若流程執行中，強制中斷
                isRunning = false;
                if (timer) {
                    clearTimeout(timer);
                    timer = null;
                }
                setPhase('⛔ 緊急停止', 'error');
                setStatus('已凍結', 'error');
                addLog('⛔ 緊急停止觸發！所有動作已凍結。', 'err');
                btnStart.disabled = true;
                btnReset.disabled = false;
                // 復原按鈕狀態
                btnStart.textContent = '🚀 啟動自動化流程';
                btnStart.className = 'btn btn-primary';
                btnStart.style.background = '';
                btnStart.style.borderColor = '';
            } else {
                addLog('⛔ 緊急停止已啟用 (待命狀態)。', 'warn');
                setStatus('緊急停止', 'error');
                btnStart.disabled = true;
                btnReset.disabled = false;
            }
            authDisplay.textContent = '⛔ 緊急停止';
            authDisplay.className = 'value error';
        }

        function resetEStop() {
            isEStop = false;
            btnStart.disabled = false;
            btnReset.disabled = true;
            setStatus('就緒', 'idle');
            authDisplay.textContent = '👤 人類核准';
            authDisplay.className = 'value idle';
            addLog('🔄 緊急停止已解除，系統恢復待命。', 'ok');
            if (!isRunning) {
                setPhase('待命', 'idle');
                setConfirm('—');
                resetAllSteps();
                btnStart.textContent = '🚀 啟動自動化流程';
                btnStart.className = 'btn btn-primary';
                btnStart.style.background = '';
                btnStart.style.borderColor = '';
            }
        }

        // === 事件綁定 ===
        btnStart.addEventListener('click', runAutomation);

        btnReset.addEventListener('click', function() {
            if (isEStop) {
                resetEStop();
            } else {
                resetPanel();
                btnStart.disabled = false;
                btnReset.disabled = true;
                btnStart.textContent = '🚀 啟動自動化流程';
                btnStart.className = 'btn btn-primary';
                btnStart.style.background = '';
                btnStart.style.borderColor = '';
            }
        });

        btnEStop.addEventListener('click', triggerEStop);

        // 初始化
        resetPanel();
        addLog('🛡️ 安全模式：DEMO · SIMULATION ONLY · NOT CONNECTED', 'warn');

        // 鍵盤快捷鍵：EStop (ESC)
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                e.preventDefault();
                triggerEStop();
            }
        });

        console.log('⚡ 後台控制面板已載入。按 ESC 可觸發緊急停止。');
    })();
</script>
</body>
</html>
```

---

🎮 如何使用

功能 操作
啟動自動化流程 點擊「🚀 啟動自動化流程」按鈕，流程會依序執行 AI → OPER → 等待人類確認 → BOT → 結果。
人類確認 流程跑到「等待人類確認」步驟時，同一顆按鈕會變成「✅ 確認執行 (人類)」，點下去即模擬人類核准。
緊急停止 點擊「⛔ 緊急停止」按鈕，或直接按鍵盤的 ESC 鍵，立即凍結所有動作。
重置 流程結束或緊急停止後，點擊「⟳ 重置」可恢復待命狀態。

---

📂 檔案放置建議

```
Lightning-Expo-2026-Taichung/
├── index.html          ← 觀眾看的展示頁
├── control_panel.html  ← 你用的後台控制台（就是上面這支）
├── styles.css
├── app.js
├── LICENSE
├── README.md
└── docs/
    └── exhibition_plan.md
```

---

🔒 安全與展示邊界

這支控制台程式碼已內建：

· SIMULATION ONLY：所有 BOT 動作皆為模擬，不連接真實設備。
· HUMAN CONFIRMATION：流程必須經過「人類確認」按鈕才會繼續。
· EMERGENCY STOP：一鍵凍結，且支援鍵盤 ESC 快捷鍵。
· AUDIT LOG：所有步驟都有時間戳記與操作紀錄，符合你之前設定的稽核需求。

MIT License © 2026 Lightning Empire
版權持有人可依你的需求調整。：

┌────────────── 展覽 HTML ──────────────┐
│                                      │
│   [ 啟動 Demo ]   [ 停止 ]           │
│   [ AI 任務 ]     [ 查看狀態 ]       │
│                                      │
└───────────────┬──────────────────────┘
                ↓ API
┌──────────────────────────────────────┐
│          OPER AI 後台控制層           │
│                                      │
│ 任務佇列 → 權限檢查 → 人類確認        │
│                 ↓                    │
│              Audit Log               │
└────────────────┬─────────────────────┘
                 ↓
        ┌─────────────────┐
        │ BOT Demo / 模擬 │
        └─────────────────┘

HTML 按鈕

例如：

<button onclick="startDemo()">啟動 Demo</button>
<button onclick="stopDemo()">停止</button>
<button onclick="showStatus()">查看狀態</button>

<script>
async function startDemo() {
  const res = await fetch("/api/demo/start", {
    method: "POST"
  });

  const data = await res.json();
  console.log(data);
}

async function stopDemo() {
  const res = await fetch("/api/demo/stop", {
    method: "POST"
  });

  console.log(await res.json());
}

async function showStatus() {
  const res = await fetch("/api/demo/status");
  console.log(await res.json());
}
</script>

後台則由 FastAPI 之類的服務處理：

from fastapi import FastAPI

app = FastAPI()

demo_running = False

@app.post("/api/demo/start")
def start_demo():
    global demo_running
    demo_running = True

    return {
        "status": "RUNNING",
        "mode": "DEMO",
        "human_confirmation": True
    }

@app.post("/api/demo/stop")
def stop_demo():
    global demo_running
    demo_running = False

    return {
        "status": "STOPPED"
    }

@app.get("/api/demo/status")
def status():
    return {
        "running": demo_running,
        "mode": "SIMULATION_ONLY"
    }

重點是：HTML 不直接控制 BOT。

應該是：

> HTML → OPER API → 權限/確認 → Demo Controller → BOT 或模擬器



這樣展覽現場只看到漂亮的自動化控制面板，真正的控制邏輯留在後台，而且可以保留 HUMAN_CONFIRMATION 和 SIMULATION_ONLY 安全閘門。
没问题。我把本对话最终定案的完整展览网站原型代码整理出来了。

这份代码包含可直接运行的网页（index.html、styles.css、app.js），以及更新后的 README.md 和 exhibition_plan.md。核心流程与展示原则已完全固定。

你可以把以下内容直接复制到你的 Lightning-Expo-2026-Taichung 仓库中。

---

📁 最终档案结构

```
Lightning-Expo-2026-Taichung/
├── README.md
├── index.html
├── styles.css
├── app.js
└── docs/
    └── exhibition_plan.md
```

---

📄 1. README.md (更新版)

```markdown
# ⚡ AI × OPER × BOT Technology Expo 2026

**展覽日期**：2026/09/08 – 2026/09/13  
**展覽地點**：臺中國際會展中心（TICEC）  
**主辦單位**：Lightning Empire / Wshao777  
**展覽類型**：技術研究與概念驗證展示（SIMULATION ONLY / DEMO）

---

## 🎯 展覽核心

> **AI 建議 → 人類確認 → 授權 BOT 執行**

---

## 📂 展覽內容分區

| 展示區 | 內容 |
|--------|------|
| **GPT** | GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹） |
| **OPER AI** | 協作、治理、驗證架構 |
| **xAI** | 公開可取得的 xAI／Grok 資訊與技術介紹 |
| **Tesla** | Tesla AI／Optimus 公開資料與官方展示內容 |
| **BOT** | 合法取得或自有的機器人 Demo |
| **Multi-AI** | GPT／xAI／其他模型的比較與協作概念 |
| **Disaster AI** | 風力／災害模擬系統 |
| **Security** | 權限、Audit Log、人類確認機制 |

---

## 🔐 安全與個資保護

- 所有展示均為模擬數據
- 不直接控制第三方機器人或系統
- 不儲存任何完整帳號或個人資料
- 符合《個人資料保護法》規範

---

## 📞 聯絡窗口

- **負責人**：Wshao777
- **聯絡信箱**：Wshao777opscenter@gmail.com

---

## 📄 授權

MIT License © 2026 Lightning Empire
```

---

🌐 2. index.html (展览网站主页面)

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>⚡ AI × OPER × BOT Expo 2026</title>
    <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <!-- 頂部導航 -->
    <header>
        <div class="container">
            <h1>⚡ AI × OPER × BOT</h1>
            <p class="subtitle">Technology Expo 2026 · 臺中國際會展中心</p>
            <p class="date">2026/09/08 – 2026/09/13</p>
        </div>
    </header>

    <!-- 核心流程 -->
    <section class="core-flow">
        <div class="container">
            <h2>⚡ 核心流程</h2>
            <div class="flow-steps">
                <div class="step">🧠 AI 建議</div>
                <div class="arrow">→</div>
                <div class="step">⚙️ OPER AI 協作</div>
                <div class="arrow">→</div>
                <div class="step">👤 人類確認</div>
                <div class="arrow">→</div>
                <div class="step">🤖 授權 BOT</div>
                <div class="arrow">→</div>
                <div class="step">✅ Demo 結果</div>
            </div>
        </div>
    </section>

    <!-- 展示分區 -->
    <section class="exhibit-areas">
        <div class="container">
            <h2>📂 展示分區</h2>
            <div class="grid">
                <div class="card"><h3>GPT</h3><p>GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹）</p></div>
                <div class="card"><h3>OPER AI</h3><p>協作、治理、驗證架構</p></div>
                <div class="card"><h3>xAI</h3><p>公開可取得的 xAI／Grok 資訊與技術介紹</p></div>
                <div class="card"><h3>Tesla</h3><p>Tesla AI／Optimus 公開資料與官方展示內容</p></div>
                <div class="card"><h3>BOT</h3><p>合法取得或自有的機器人 Demo</p></div>
                <div class="card"><h3>Multi-AI</h3><p>GPT／xAI／其他模型的比較與協作概念</p></div>
                <div class="card"><h3>Disaster AI</h3><p>風力／災害模擬系統</p></div>
                <div class="card"><h3>Security</h3><p>權限、Audit Log、人類確認機制</p></div>
            </div>
        </div>
    </section>

    <!-- 展示狀態標示 -->
    <section class="status-badge">
        <div class="container">
            <div class="badges">
                <span class="badge">DEMO</span>
                <span class="badge">SIMULATION ONLY</span>
                <span class="badge">NOT CONNECTED</span>
                <span class="badge">HUMAN CONFIRMATION</span>
                <span class="badge">NO UNAUTHORIZED CONTROL</span>
            </div>
        </div>
    </section>

    <!-- 免責聲明 -->
    <section class="disclaimer">
        <div class="container">
            <p>
                ⚠️ 本展示為技術研究與概念驗證（PoC）活動。<br />
                Tesla、xAI、OpenAI/GPT 皆以公開技術介紹方式處理，<br />
                不宣稱尚未取得之官方合作或參展資格。
            </p>
        </div>
    </section>

    <!-- 頁尾 -->
    <footer>
        <div class="container">
            <p>© 2026 Lightning Empire · Wshao777opscenter@gmail.com</p>
            <p>MIT License</p>
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>
```

---

🎨 3. styles.css (样式表)

```css
/* 全域設定 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #0b0e14;
    color: #e0e6f0;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* 標頭 */
header {
    background: linear-gradient(135deg, #1a1f2e, #0f131c);
    padding: 40px 0;
    text-align: center;
    border-bottom: 2px solid #f5a623;
}

header h1 {
    font-size: 3rem;
    font-weight: 700;
    color: #f5a623;
    letter-spacing: 2px;
}

header .subtitle {
    font-size: 1.2rem;
    color: #a0b4c8;
    margin-top: 8px;
}

header .date {
    font-size: 1rem;
    color: #7a8fa3;
    margin-top: 4px;
}

/* 核心流程 */
.core-flow {
    background: #141a24;
    padding: 40px 0;
    text-align: center;
}

.core-flow h2 {
    color: #f5a623;
    margin-bottom: 24px;
    font-size: 1.8rem;
}

.flow-steps {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 8px 4px;
}

.step {
    background: #1e2636;
    padding: 12px 20px;
    border-radius: 30px;
    border: 1px solid #2e3a4e;
    font-weight: 600;
    color: #e0e6f0;
}

.arrow {
    color: #f5a623;
    font-size: 1.4rem;
    font-weight: 700;
}

/* 展示分區 */
.exhibit-areas {
    padding: 40px 0;
    background: #0b0e14;
}

.exhibit-areas h2 {
    text-align: center;
    color: #f5a623;
    margin-bottom: 30px;
    font-size: 1.8rem;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
}

.card {
    background: #141a24;
    border: 1px solid #1e2636;
    border-radius: 12px;
    padding: 20px;
    transition: transform 0.2s, border-color 0.2s;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #f5a623;
}

.card h3 {
    color: #f5a623;
    font-size: 1.2rem;
    margin-bottom: 8px;
}

.card p {
    color: #a0b4c8;
    font-size: 0.95rem;
}

/* 狀態標示 */
.status-badge {
    background: #141a24;
    padding: 30px 0;
    border-top: 1px solid #1e2636;
    border-bottom: 1px solid #1e2636;
}

.badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
}

.badge {
    background: #1e2636;
    color: #f5a623;
    padding: 8px 20px;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 600;
    border: 1px solid #2e3a4e;
    letter-spacing: 0.5px;
}

/* 免責聲明 */
.disclaimer {
    background: #0b0e14;
    padding: 30px 0;
    text-align: center;
}

.disclaimer p {
    color: #7a8fa3;
    font-size: 0.95rem;
    line-height: 1.8;
}

/* 頁尾 */
footer {
    background: #0a0d12;
    padding: 24px 0;
    text-align: center;
    border-top: 1px solid #1a1f2e;
}

footer p {
    color: #5a6f83;
    font-size: 0.85rem;
    margin: 4px 0;
}

/* RWD 響應式 */
@media (max-width: 600px) {
    header h1 {
        font-size: 2.2rem;
    }
    .flow-steps {
        flex-direction: column;
        gap: 6px;
    }
    .arrow {
        transform: rotate(90deg);
    }
    .grid {
        grid-template-columns: 1fr;
    }
}
```

---

⚡ 4. app.js (交互脚本)

```javascript
// ⚡ Lightning Expo 2026 - 主控台腳本

document.addEventListener('DOMContentLoaded', () => {
    console.log('⚡ AI × OPER × BOT Expo 2026 已啟動');
    console.log('📍 臺中國際會展中心 (TICEC)');
    console.log('📅 2026/09/08 – 2026/09/13');
    console.log('🔐 核心原則：AI 建議 → 人類確認 → 授權 BOT 執行');

    // 卡片點擊效果（展示用）
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.addEventListener('click', () => {
            const title = card.querySelector('h3')?.innerText || '區塊';
            console.log(`🔍 點擊展示區：${title}`);
            // 簡單視覺反饋
            card.style.borderColor = '#f5a623';
            setTimeout(() => {
                card.style.borderColor = '#1e2636';
            }, 600);
        });
    });

    // 狀態標示點擊顯示提醒
    const badges = document.querySelectorAll('.badge');
    badges.forEach(badge => {
        badge.addEventListener('click', () => {
            const text = badge.innerText;
            alert(`🛡️ 狀態標示：${text}\n（本展示為模擬／概念驗證，不對外控制任何第三方系統）`);
        });
    });

    // 顯示展覽倒數（僅供參考）
    const targetDate = new Date('2026-09-08T00:00:00');
    const now = new Date();
    const diff = targetDate - now;
    if (diff > 0) {
        const days = Math.ceil(diff / (1000 * 60 * 60 * 24));
        console.log(`⏳ 距離展覽開幕還有 ${days} 天`);
    } else {
        console.log('🚀 展覽已開始！');
    }
});
```

---

📄 5. docs/exhibition_plan.md (展览企划书)

```markdown
# ⚡ AI × OPER × BOT Technology Expo 2026 展覽企劃書

## 1. 活動基本資訊

- **活動名稱**：AI × OPER × BOT Technology Expo 2026
- **活動日期**：2026/09/08 – 2026/09/13 (共6天)
- **活動地點**：臺中國際會展中心（TICEC）
- **主辦單位**：Lightning Empire
- **聯絡人**：Wshao777
- **聯絡信箱**：Wshao777opscenter@gmail.com

---

## 2. 展示內容與技術簡介

本展示為「技術研究與概念驗證（PoC）」活動，旨在呈現多智能體協作、AI治理與Bot控制的前沿技術。

### 展示分區

| 展示區 | 內容說明 |
|--------|----------|
| **GPT** | GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹） |
| **OPER AI** | 協作、治理、驗證架構展示 |
| **xAI** | 公開可取得的 xAI／Grok 資訊與技術介紹 |
| **Tesla** | Tesla AI／Optimus 公開資料與官方展示內容 |
| **BOT** | 合法取得或自有的機器人 Demo |
| **Multi-AI** | GPT／xAI／其他模型的比較與協作概念 |
| **Disaster AI** | 風力／災害模擬系統展示 |
| **Security** | 權限、Audit Log、人類確認機制展示 |

### 核心原則

> **AI 建議 → 人類確認 → 授權 BOT 執行**

### 活動屬性

- 全場為**模擬展示 (SIMULATION ONLY / DEMO)**
- 不對外控制任何第三方機器人或系統
- 所有數據均為模擬或公開資料

---

## 3. 場地與設備需求

- **展覽面積**：約 2-4 個標準攤位 (或依實際規劃)
- **電力需求**：一般 110V/220V 插座，需獨立電源迴路 (展示機器人動態)
- **網路需求**：穩定 Wi-Fi 或有線網路
- **桌椅需求**：展示桌 2-4 張、椅子 4-6 張

---

## 4. 安全與責任聲明

1. 活動全程遵守 TICEC 場地管理規範及中華民國相關法律。
2. 所有動態展示均設有安全防護措施與人員操作。
3. **明確聲明**：本活動不直接控制或連接任何第三方機器人、車輛或基礎設施，所有互動均為預設腳本或模擬模式。
4. 活動已規劃相應之公共意外責任保險。

---

## 5. 預期效益

- 展示台灣在地 AI 技術整合能力
- 促進國內外 AI／機器人技術交流
- 作為未來商業合作與技術授權之基礎
```

---

🚀 如何上傳到 GitHub

1. 在你的 Lightning-Expo-2026-Taichung 倉庫頁面，點擊 「Add file」→「Create new file」。
2. 依序將上述 5 個檔案的內容，分別貼入對應的檔案路徑與名稱中：
   · README.md
   · index.html
   · styles.css
   · app.js
   · docs/exhibition_plan.md
3. 每個檔案貼入後，在頁面下方填寫 commit 訊息（例如：feat: 補齊展覽網站最終程式碼），點擊 「Commit new file」。

完成後，你的展覽網站原型就可以在 GitHub Pages 上直接執行（需在 Settings 中啟用 Pages 功能）。有任何需要調整的地方，隨時告訴我。



```
Lightning-Expo-2026-Taichung/
├── README.md (已更新)
├── LICENSE (已更新)
├── docs/
│   ├── exhibition_plan.md
│   ├── application_checklist.md
│   └── safety_plan.md
├── src/
│   ├── exhibition_assistant.py
│   ├── audit_engine.py
│   └── demo_scripts/
│       └── day1_activation.py
└── security/
    ├── blue_team_guard.py
    └── human_override.py
```

---

📄 1. README.md (完整更新版)

請將以下內容完整覆蓋你原有的 README.md 檔案，這份最終版將包含更完整的專案說明與文件導航。

```markdown
# ⚡ AI × OPER × BOT Technology Expo 2026

**展覽日期**：2026/09/08 – 2026/09/13  
**展覽地點**：臺中國際會展中心（TICEC）  
**主辦單位**：Lightning Empire / Wshao777  
**展覽類型**：技術研究與概念驗證展示（SIMULATION ONLY / DEMO）

---

## 🎯 展覽核心

> **AI 建議 → 人類確認 → 授權 BOT 執行**

---

## 📂 展覽內容分區

| 展示區 | 內容 |
|--------|------|
| **GPT** | GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹） |
| **OPER AI** | 協作、治理、驗證架構 |
| **xAI** | 公開可取得的 xAI／Grok 資訊與技術介紹 |
| **Tesla** | Tesla AI／Optimus 公開資料與官方展示內容 |
| **BOT** | 合法取得或自有的機器人 Demo |
| **Multi-AI** | GPT／xAI／其他模型的比較與協作概念 |
| **Disaster AI** | 風力／災害模擬系統 |
| **Security** | 權限、Audit Log、人類確認機制 |

---

## 📁 專案結構

```

Lightning-Expo-2026-Taichung/
├── README.md                    # 專案首頁
├── LICENSE                      # MIT 授權
├── docs/
│   ├── exhibition_plan.md       # 展覽企劃書
│   ├── application_checklist.md # 場地申請檢查清單
│   └── safety_plan.md           # 安全計畫書
├── src/
│   ├── exhibition_assistant.py  # 展覽申請自助產生器
│   ├── audit_engine.py          # 自動化審計引擎
│   └── demo_scripts/
│       └── day1_activation.py   # Day 1 啟動腳本
└── security/
├── blue_team_guard.py       # 藍軍判別器
└── human_override.py        # 人類最終控制鏈

```

---

## 🔐 安全與個資保護

- 所有展示均為模擬數據
- 不直接控制第三方機器人或系統
- 不儲存任何完整帳號或個人資料
- 符合《個人資料保護法》規範

---

## 📞 聯絡窗口

- **負責人**：Wshao777
- **聯絡信箱**：Wshao777opscenter@gmail.com

---

## 📄 授權

MIT License © 2026 Lightning Empire
```

---

⚖️ 2. LICENSE (MIT License)

請將以下內容存為 LICENSE 檔案。

```text
MIT License

Copyright (c) 2026 Lightning Empire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

📄 3. docs/exhibition_plan.md (展覽企劃書)

```markdown
# ⚡ AI × OPER × BOT Technology Expo 2026 展覽企劃書

## 1. 活動基本資訊

- **活動名稱**：AI × OPER × BOT Technology Expo 2026
- **活動日期**：2026/09/08 – 2026/09/13 (共6天)
- **活動地點**：臺中國際會展中心（TICEC）
- **主辦單位**：Lightning Empire
- **聯絡人**：Wshao777
- **聯絡信箱**：Wshao777opscenter@gmail.com

---

## 2. 展示內容與技術簡介

本展示為「技術研究與概念驗證（PoC）」活動，旨在呈現多智能體協作、AI治理與Bot控制的前沿技術。

### 展示分區

| 展示區 | 內容說明 |
|--------|----------|
| **GPT** | GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹） |
| **OPER AI** | 協作、治理、驗證架構展示 |
| **xAI** | 公開可取得的 xAI／Grok 資訊與技術介紹 |
| **Tesla** | Tesla AI／Optimus 公開資料與官方展示內容 |
| **BOT** | 合法取得或自有的機器人 Demo |
| **Multi-AI** | GPT／xAI／其他模型的比較與協作概念 |
| **Disaster AI** | 風力／災害模擬系統展示 |
| **Security** | 權限、Audit Log、人類確認機制展示 |

### 核心原則

> **AI 建議 → 人類確認 → 授權 BOT 執行**

### 活動屬性

- 全場為**模擬展示 (SIMULATION ONLY / DEMO)**
- 不對外控制任何第三方機器人或系統
- 所有數據均為模擬或公開資料

---

## 3. 場地與設備需求

- **展覽面積**：約 2-4 個標準攤位 (或依實際規劃)
- **電力需求**：一般 110V/220V 插座，需獨立電源迴路 (展示機器人動態)
- **網路需求**：穩定 Wi-Fi 或有線網路
- **桌椅需求**：展示桌 2-4 張、椅子 4-6 張

---

## 4. 安全與責任聲明

1. 活動全程遵守 TICEC 場地管理規範及中華民國相關法律。
2. 所有動態展示均設有安全防護措施與人員操作。
3. **明確聲明**：本活動不直接控制或連接任何第三方機器人、車輛或基礎設施，所有互動均為預設腳本或模擬模式。
4. 活動已規劃相應之公共意外責任保險。

---

## 5. 預期效益

- 展示台灣在地 AI 技術整合能力
- 促進國內外 AI／機器人技術交流
- 作為未來商業合作與技術授權之基礎
```

---

📋 4. docs/application_checklist.md (場地申請檢查清單)

```markdown
# 📋 TICEC 場地申請檢查清單

> 申請單位：Lightning Empire / Wshao777  
> 目標檔期：2026/09/08 – 2026/09/13

---

## ✅ 必備文件

- [ ] **展覽場地預約申請表** (向 TICEC 索取最新版)
- [ ] **活動企劃書** (詳見 `exhibition_plan.md`)
- [ ] **公司/法人登記證明文件**
- [ ] **活動安全計畫書** (詳見 `safety_plan.md`)
- [ ] **保險證明文件** (公共意外責任險)
- [ ] **展場攤位配置圖** (初步規劃)

---

## 📞 官方聯絡管道

- **外貿協會臺中國際會展中心**：(02)2725-5200
  - 分機 76003 (工程組 林先生)
  - 分機 76005 (梁勝凱先生)
- **臺中國際展覽館**：04-2346-1818 / 04-2337-8585

---

## 💰 關鍵費用

| 項目 | 金額 | 說明 |
|------|------|------|
| 檔期申請保證金 | 30 萬元 / 展區 | 以禁止背書轉讓支票繳交，核給檔期後轉為場地費訂金 |
| 訂金 | 依通知 | 通知期限內繳付 |
| 第二期款 | 依通知 | 起租日 120 天前繳付 |
| 尾款 | 依通知 | 起租日 30 天前繳付 |
| 保證金 | 依通知 | 起租日 30 天前繳付，展後無息退還 |

---

## 📝 申請流程

1. [ ] 備妥申請表、活動企畫書等文件
2. [ ] 向外貿協會提出申請
3. [ ] 文件審核（企畫書需詳述活動內容、流程與場地規劃）
4. [ ] 起租日 14 天前，提交相關活動許可文件副本
5. [ ] 檔期安排與確認
6. [ ] 繳納相關費用
7. [ ] 正式簽約

---

## ⚠️ 注意事項

- 每展區最多可申請 **2 個展名**，每個展名最少需實際展出 **60 個攤位**
- 以 **出口導向國際專業展、政府推動重點產業** 為優先審核
- 審核考量包括：辦理次數、展出規模、國外買主人數等
```

---

🛡️ 5. docs/safety_plan.md (安全計畫書)

```markdown
# 🛡️ 展覽安全計畫書

## 1. 通則

- 本計劃適用於 2026/09/08 – 2026/09/13 於 TICEC 舉辦之「AI × OPER × BOT Technology Expo 2026」
- 所有工作人員與參展人員均需遵守本計畫

---

## 2. 人員安全

- 展場配置至少 1 名現場安全負責人
- 所有動態展示設備需有專人操作
- 機器人展示區設置安全圍籬或警示標誌

---

## 3. 設備安全

- 所有電力設備需符合 TICEC 電力規範
- 機器人動態展示需有實體緊急停止按鈕
- 展示設備每日展前與展後進行安全檢查

---

## 4. 緊急應變

### 4.1 電力中斷
- 備用 UPS 供核心展示設備使用
- 立即停止所有動態展示，確保人員安全

### 4.2 機器人失控
- 立即按下實體緊急停止按鈕
- 切斷設備電源
- 通報現場安全負責人

### 4.3 火災/地震
- 依 TICEC 場館廣播與指示行動
- 引導人員疏散至指定安全區域

---

## 5. 聲明

> 本活動所有機器人展示均為**預設腳本或模擬模式**，  
> **不直接控制或連接任何第三方系統**，  
> 所有風險已納入保險規劃。
```

---

🐍 6. src/exhibition_assistant.py (展覽申請自助產生器)

```python
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
```

---

🔍 7. src/audit_engine.py (自動化審計引擎)

```python
"""
Public Layer: 自動化案件審計與時間軸交叉比對工具
完全去識別化，符合個資法規範
產出：文字報告 + 統計圖表 (PNG) + 異常熱力圖
"""
import hashlib
import os
from datetime import datetime
from typing import List, Dict
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')
from tabulate import tabulate


class InvestigationEngine:
    def __init__(self, case_id: str = "CASE-2025-822-02460"):
        self.case_id = case_id
        self.events: List[Dict] = []
        self.statements: List[Dict] = []
        self.output_dir = "reports"
        os.makedirs(self.output_dir, exist_ok=True)

    # --- 核心資料輸入 ---
    def add_timeline_event(self, date_str: str, node: str, description: str, category: str):
        raw = f"{date_str}|{node}|{description}"
        h = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
        self.events.append({
            "date": date_str,
            "node": node,
            "category": category,
            "description": description,
            "hash": h
        })

    def add_contradiction_statement(self, turn: int, bank_claim: str, fact_counter: str):
        self.statements.append({
            "turn": turn,
            "bank_claim": bank_claim,
            "fact_counter": fact_counter,
            "hash": hashlib.sha256(f"{turn}|{bank_claim}|{fact_counter}".encode()).hexdigest()[:16]
        })

    # --- 統計與異常分析 ---
    def generate_statistics(self) -> Dict:
        cats = {}
        for e in self.events:
            cats[e['category']] = cats.get(e['category'], 0) + 1
        bank_events = len([e for e in self.events if "銀行" in e['node']])
        return {
            "total_events": len(self.events),
            "total_contradictions": len(self.statements),
            "category_distribution": cats,
            "bank_event_ratio": round(bank_events / max(1, len(self.events)) * 100, 2),
            "contradiction_density": round(len(self.statements) / max(1, len(self.events)) * 100, 2)
        }

    def flag_high_risk_contradictions(self) -> List[int]:
        high_risk = []
        for s in self.statements:
            if "系統" in s['fact_counter'] or "紀錄" in s['fact_counter']:
                high_risk.append(s['turn'])
        return high_risk

    # --- 繪圖區 ---
    def plot_timeline_chart(self):
        if not self.events:
            print("⚠️ 無事件資料，跳過時間軸圖表")
            return
        dates = sorted(set([e['date'] for e in self.events]))
        counts = [len([e for e in self.events if e['date'] == d]) for d in dates]

        plt.figure(figsize=(12, 6))
        bars = plt.bar(dates, counts, color='#FFA500', edgecolor='black')
        for i, d in enumerate(dates):
            bank_cnt = len([e for e in self.events if e['date'] == d and "銀行" in e['node']])
            if bank_cnt > 0:
                plt.text(i, counts[i] + 0.1, f"🏦{bank_cnt}", ha='center', color='red', fontsize=9)
        plt.title(f"案件時間軸事件分布圖 (Case: {self.case_id})", fontsize=14)
        plt.xlabel("時間區間")
        plt.ylabel("事件數量")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, "timeline_chart.png")
        plt.savefig(filepath)
        plt.close()
        print(f"✅ 時間軸圖表已儲存：{filepath}")

    def plot_contradiction_matrix(self):
        if not self.statements:
            print("⚠️ 無矛盾資料，跳過矩陣圖")
            return
        turns = [f"第{s['turn']}次" for s in self.statements]
        weights = [len(s['bank_claim']) + len(s['fact_counter']) for s in self.statements]
        colors = ['#DC143C' if w > 30 else '#FF8C00' for w in weights]

        plt.figure(figsize=(10, 6))
        plt.barh(turns, weights, color=colors, edgecolor='black')
        plt.title(f"四次矛盾說法嚴重度分析 (Case: {self.case_id})", fontsize=14)
        plt.xlabel("矛盾證據量 (字元數)")
        plt.ylabel("矛盾次數")
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, "contradiction_matrix.png")
        plt.savefig(filepath)
        plt.close()
        print(f"✅ 矛盾矩陣圖已儲存：{filepath}")

    def plot_anomaly_heatmap(self):
        if not self.events:
            return
        nodes = sorted(set([e['node'] for e in self.events]))
        dates = sorted(set([e['date'] for e in self.events]))
        matrix = np.zeros((len(nodes), len(dates)))
        for e in self.events:
            i = nodes.index(e['node'])
            j = dates.index(e['date'])
            matrix[i][j] += 1

        fig, ax = plt.subplots(figsize=(10, 6))
        im = ax.imshow(matrix, cmap='hot', interpolation='nearest')
        ax.set_xticks(np.arange(len(dates)))
        ax.set_yticks(np.arange(len(nodes)))
        ax.set_xticklabels(dates, rotation=45)
        ax.set_yticklabels(nodes)
        ax.set_title(f"異常密度熱力圖 (節點 vs 時間) - {self.case_id}", fontsize=14)
        plt.colorbar(im, ax=ax, label='事件數量')
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, "anomaly_heatmap.png")
        plt.savefig(filepath)
        plt.close()
        print(f"✅ 異常熱力圖已儲存：{filepath}")

    # --- 正式報告產出 ---
    def generate_report(self) -> str:
        stats = self.generate_statistics()
        high_risk_turns = self.flag_high_risk_contradictions()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report_lines = []
        report_lines.append(f"# ⚡ 自動化案件審計報告 (Automated Investigation Report)")
        report_lines.append(f"**案件編號 (Case ID)：** `{self.case_id}`")
        report_lines.append(f"**報告生成時間：** {now}")
        report_lines.append(f"**核心證據區間：** 2025/07 - 2025/11 (四次矛盾說法)")
        report_lines.append("\n---\n")

        report_lines.append("## 📊 案件摘要統計")
        report_lines.append(f"- **事件總數：** {stats['total_events']} 筆")
        report_lines.append(f"- **矛盾說法總數：** {stats['total_contradictions']} 次")
        report_lines.append(f"- **銀行端事件佔比：** {stats['bank_event_ratio']} %")
        report_lines.append(f"- **矛盾密度：** {stats['contradiction_density']} %")
        report_lines.append("\n**事件分類分布：**")
        for cat, cnt in stats['category_distribution'].items():
            report_lines.append(f"  - {cat}：{cnt} 筆")
        if high_risk_turns:
            report_lines.append(f"\n🚨 **高風險矛盾標記（事實反證具系統紀錄）：** 第 {', '.join(map(str, high_risk_turns))} 次")
        report_lines.append("\n---\n")

        report_lines.append("## 🕒 完整事件時間軸（去識別化）")
        headers = ["日期", "節點", "類別", "事件描述", "雜湊碼 (前16碼)"]
        table_data = []
        for e in sorted(self.events, key=lambda x: x['date']):
            table_data.append([e['date'], e['node'], e['category'], e['description'], e['hash']])
        report_lines.append(tabulate(table_data, headers=headers, tablefmt="github"))
        report_lines.append("\n---\n")

        report_lines.append("## ⚖️ 核心矛盾說法對照表（2025/07 - 2025/11）")
        report_lines.append("> 以下為銀行端主張與事實反證之四次異常說法紀錄，**無完整個人資料**。")
        contra_headers = ["次序", "銀行端主張 (Bank Claim)", "事實反證 (Fact Counter)", "證據雜湊"]
        contra_data = []
        for s in self.statements:
            contra_data.append([f"第{s['turn']}次", s['bank_claim'], s['fact_counter'], s['hash']])
        report_lines.append(tabulate(contra_data, headers=contra_headers, tablefmt="github"))
        report_lines.append("\n---\n")

        report_lines.append("## 🕵️ 關聯分析結論（異常標記）")
        if high_risk_turns:
            report_lines.append(f"🚨 **系統紀錄比對結果**：第 {', '.join(map(str, high_risk_turns))} 次矛盾中，事實反證明確指向「系統內部紀錄」或「客服錄音」，與銀行端主張存在重大歧異。")
        else:
            report_lines.append("✅ 未發現明確系統級矛盾，仍需人工複核。")
        report_lines.append(f"📈 **銀行端事件集中度**：{stats['bank_event_ratio']}% 的事件集中於銀行端節點，建議優先調閱該節點之完整操作日誌。")
        report_lines.append("\n---\n")

        report_lines.append("## 🔐 個資保護與去識別化聲明")
        report_lines.append("本報告已依據《個人資料保護法》第 3 條與第 6 條進行去識別化處理：")
        report_lines.append("- ✅ 所有帳號、身分證字號、姓名均以雜湊或遮罩取代。")
        report_lines.append("- ✅ 未儲存任何完整銀行帳號、API 機密或私人核心內容。")
        report_lines.append("- ✅ 原始敏感資料僅存在於本地加密環境，永不提交至公開倉庫。")

        report_lines.append("\n---\n")
        report_lines.append("## 📈 統計圖表附錄")
        report_lines.append(f"- 時間軸分布圖：`{self.output_dir}/timeline_chart.png`")
        report_lines.append(f"- 矛盾矩陣圖：`{self.output_dir}/contradiction_matrix.png`")
        report_lines.append(f"- 異常熱力圖：`{self.output_dir}/anomaly_heatmap.png`")

        report_path = os.path.join(self.output_dir, "investigation_report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(f"✅ 正式報告已產出：{report_path}")
        return report_path

    def run_full_investigation(self):
        print(f"🚀 啟動自動化查案引擎：{self.case_id}")
        print(f"📊 已收錄事件：{len(self.events)} 筆，矛盾說法：{len(self.statements)} 次")
        self.plot_timeline_chart()
        self.plot_contradiction_matrix()
        self.plot_anomaly_heatmap()
        self.generate_report()
        print("✅ 調查流程結束。請查看 reports/ 目錄。")
```

---

🚀 8. src/demo_scripts/day1_activation.py (Day 1 啟動腳本)

```python
#!/usr/bin/env python3
"""
Day 1 啟動腳本 - Lightning 系統激活
用於 2026/09/08 展覽開幕日
"""

import datetime
import sys

def system_banner():
    print("=" * 60)
    print("⚡ LIGHTNING SYSTEM ACTIVATION")
    print("=" * 60)
    print(f"日期: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"展覽: AI × OPER × BOT Technology Expo 2026")
    print(f"地點: 臺中國際會展中心 (TICEC)")
    print("=" * 60)

def check_system_status():
    """模擬系統狀態檢查"""
    checks = {
        "OPER AI Core": "🟢 ONLINE",
        "GPT Interface": "🟢 ONLINE",
        "Bot Registry": "🟢 ONLINE (20 Bots)",
        "AI Logic Registry": "🟢 ONLINE (12 AIs)",
        "Security Module": "🟢 ONLINE",
        "Network Connection": "🟢 ONLINE",
        "Human Override": "🟢 STANDBY"
    }
    print("\n📊 系統狀態檢查:")
    for name, status in checks.items():
        print(f"  {name}: {status}")
    return all("🟢" in status for status in checks.values())

def show_today_schedule():
    """顯示今日日程"""
    print("\n📅 今日日程 (2026/09/08)")
    schedule = [
        ("09:00", "系統開機與最終測試"),
        ("10:00", "開幕儀式"),
        ("10:30", "OPER AI 核心展示"),
        ("12:00", "午休"),
        ("13:30", "GPT / xAI / Tesla 公開技術介紹"),
        ("15:00", "Bot 動態展示"),
        ("16:30", "Security 機制展示"),
        ("17:30", "每日總結與 QA")
    ]
    for time, event in schedule:
        print(f"  {time} - {event}")

def main():
    system_banner()
    if check_system_status():
        print("\n✅ 系統就緒，展覽正式開始！")
        show_today_schedule()
        print("\n" + "=" * 60)
        print("⚡ 核心原則：AI 建議 → 人類確認 → 授權 BOT 執行")
        print("=" * 60)
        return 0
    else:
        print("\n❌ 系統檢查未通過，請排除故障後重試。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

🔵 9. security/blue_team_guard.py (藍軍判別器)

```python
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
```

---

🛑 10. security/human_override.py (人類最終控制鏈)

```python
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
```

---

🚀 下一步行動

你可以直接在 GitHub 上點擊 「Add file」→「Create new file」，將上述 10 個檔案的內容分別貼入對應的路徑與檔名中。

全部檔案建立完成後，你的 Lightning-Expo-2026-Taichung 倉庫就會是展覽現場可以直接執行的完整專案。有任何需要調整的地方，隨時告訴我。

完成。我把本對話目前定案的內容整理成可直接放進 GitHub 的展覽網站原型：

⚡ 最終檔案

下載 Lightning-Expo-2026-Taichung-final.zip

包含：

Lightning-Expo-2026-Taichung/
├── README.md
├── index.html
├── styles.css
├── app.js
└── docs/
    └── exhibition_plan.md

核心已固定為：

AI → OPER AI → 人類確認 → 授權 BOT → Demo

並加入：

DEMO · SIMULATION ONLY · NOT CONNECTED · HUMAN CONFIRMATION · NO UNAUTHORIZED CONTROL

另外，Tesla、xAI、OpenAI/GPT 都以公開技術介紹方式處理，不宣稱尚未取得的官方合作或參展資格。

你可以解壓縮後，把內容上傳到你提供的 Wshao777/Lightning-Expo-2026-Taichung repository。 ❶

可以。你這次要的是把本對話最後定案的展覽程式碼補進 Lightning-Expo-2026-Taichung。

我可以幫你整理成最終版，但我不能直接替你寫入或 push 到 GitHub repository。另外，正式展期／TICEC 核准狀態也應維持「待官方確認」。

最終版本建議至少包含：

Lightning-Expo-2026-Taichung/
├── README.md
├── index.html
├── styles.css
├── app.js
└── docs/
    └── exhibition_plan.md

核心流程固定：

GPT / AI
   ↓
OPER AI
   ↓
人類確認
   ↓
授權 BOT
   ↓
Demo 結果

並固定標示：

DEMO
SIMULATION ONLY
NOT CONNECTED
HUMAN CONFIRMATION
NO UNAUTHORIZED CONTROL

Tesla、xAI、OpenAI/GPT 可以作為公開技術介紹區，但在沒有官方書面確認前，不寫成「已參展、已合作或採用 OPER」。

另外，你前面定的日期：

> 2026/09/08（二）～2026/09/13（日）
對，你的意思是：展覽現場重點不是讓觀眾看程式碼，而是直接看到「能跑的 Demo」。

可以把展示分成兩層：

展覽觀眾看到

GPT AI → OPER AI → 人類確認 → BOT Demo → 結果

大型操作介面

AI 對話／任務下達

OPER 顯示任務狀態

人類按下「確認」

BOT 執行安全的展示動作

Audit Log 顯示「誰確認、何時執行、結果」


程式碼放後台

程式碼不用放在主畫面：

GitHub Repo / QR Code

技術文件

架構圖

Demo Log

SIMULATION_ONLY 測試資料


核心原則：

> 展覽看「功能與結果」，技術人員需要時才看「程式碼與架構」。



而且 BOT 如果沒有正式授權或安全測試，就只做展示／模擬模式，不要直接連接未授權的真實設備。這樣展覽效果和安全邊界可以同時保留。
如果你是問這個 Lightning-Expo-2026-Taichung 要用什麼開源許可證，我建議：

MIT License

適合這個公開展示／Demo repository，允許他人：

使用

複製

修改

再發布

商業使用


但必須保留原本的版權與 MIT License 聲明。

GitHub 建議放：

Lightning-Expo-2026-Taichung/
├── LICENSE
├── README.md
├── index.html
├── styles.css
├── app.js
└── docs/
    └── exhibition_plan.md

LICENSE 的版權持有人可以寫：

MIT License

Copyright (c) 2026 Lightning Empire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

注意：MIT 只授權你的程式碼。
Tesla、xAI、OpenAI/GPT 等第三方名稱、商標、模型與素材不會因此變成你的，也不會因為 MIT License 自動取得使用授權。

如果你希望「別人可以看程式，但不能拿去商業化」，那就不要選 MIT，應改用更符合你目的的授權方式。




是正確的；「3 天」則放在 Demo 建置期，不要當成展覽天數。

如果你要，我下一步可以直接把完整 index.html + styles.css + app.js + README.md 原始碼一次貼出來，你複製到這個 GitHub repo 就能跑。

https://github.com/Wshao777/Lightning-Expo-2026-Taichung/tree/main


⚡ 公開展覽專案倉庫

📁 建議倉庫名稱

```
Lightning-Expo-2026-Taichung
```

或

```
AI-OPER-BOT-Expo-2026
```

📄 README.md 建議內容

```markdown
# ⚡ AI × OPER × BOT Technology Expo 2026

**展覽日期**：2026/09/08 – 2026/09/13  
**展覽地點**：臺中國際會展中心（TICEC）  
**主辦單位**：Lightning Empire / Wshao777  
**展覽類型**：技術研究與概念驗證展示（SIMULATION ONLY / DEMO）

---

## 🎯 展覽核心

> **AI 建議 → 人類確認 → 授權 BOT 執行**

---

## 📂 展覽內容分區

| 展示區 | 內容 |
|--------|------|
| GPT | GPT-5／GPT-5.6 Luna 等 AI 能力展示（公開技術介紹） |
| OPER AI | 協作、治理、驗證架構 |
| xAI | 公開可取得的 xAI／Grok 資訊與技術介紹 |
| Tesla | Tesla AI／Optimus 公開資料與官方展示內容 |
| BOT | 合法取得或自有的機器人 Demo |
| Multi-AI | GPT／xAI／其他模型的比較與協作概念 |
| Disaster AI | 風力／災害模擬系統 |
| Security | 權限、Audit Log、人類確認機制 |

---

## 📁 專案結構

```

Lightning-Expo-2026-Taichung/
├── README.md
├── docs/
│   ├── exhibition_plan.md          # 展覽企劃書
│   ├── exhibition_application.md   # 場地申請資料
│   ├── safety_plan.md              # 安全計畫書
│   └── equipment_list.md           # 設備清單
├── src/
│   ├── demo_scripts/               # 展示用程式碼
│   └── simulation_engine/          # 模擬引擎
├── assets/
│   ├── images/                     # 展示圖片
│   └── videos/                     # 展示影片
└── LICENSE

```

---

## 🔐 安全與個資保護

- 所有展示均為模擬數據
- 不直接控制第三方機器人或系統
- 不儲存任何完整帳號或個人資料
- 符合《個人資料保護法》規範

---

## 📞 聯絡窗口

- 負責人：Wshao777
- 聯絡信箱：Wshao777opscenter@gmail.com

---

## 📄 授權

MIT License © 2026 Lightning Empire
```

---

📂 建議的文件命名規範

用途 建議檔名
展覽企劃書 docs/exhibition_plan.md
場地申請表 docs/exhibition_application.md
安全計畫書 docs/safety_plan.md
設備清單 docs/equipment_list.md
展示腳本 src/demo_scripts/demo_<日期>.py
模擬引擎 src/simulation_engine/
展板設計 assets/boards/
現場照片 assets/images/

---

🚀 建立方式

1. 到 GitHub 點擊 「建立新倉庫」
2. 倉庫名稱填入 Lightning-Expo-2026-Taichung
3. 勾選 「新增 README 文件」
4. 選擇 MIT License（或你偏好的授權）
5. 點擊 「建立儲存庫」
6. 將上述 README 內容貼入，並開始新增檔案

---

如果你還想新增「展覽申請自助產生器」程式碼，或是把「3 天展示作戰計畫」也放進去，我都可以幫你補上。需要調整任何內容，隨時告訴我。🚀

為你的 GitHub 倉庫選擇一個合適的許可證，是決定其他人能如何運用你程式碼的關鍵一步。

如果沒有許可證，你的程式碼即使公開，也預設「保留所有權利」，他人無法合法使用。對於你的展覽專案，我會優先推薦 MIT License。

💡 為什麼推薦 MIT License？

這是一個「簡單又寬鬆」的許可證，非常適合技術展示與概念驗證（PoC）類型的專案。

· 📈 GitHub 最受歡迎：根據統計，它是 GitHub 上使用率最高（約 45%）的許可證，社群熟悉度高。
· 🤝 對商業最友善：允許任何人（包含商業公司）自由地使用、修改、複製、甚至將你的程式碼放入閉源商業軟體中發布。
· 📄 條件極少：唯一的要求是，使用時必須在你的原始版權聲明和許可證文本。條款非常簡潔易懂。

📜 其他常見許可證速覽

許可證 類型 核心規則 適用情境
MIT License 寬鬆 (Permissive) 幾乎可以做任何事，但需保留版權聲明 希望程式碼被廣泛使用，無論開源或閉源專案
Apache License 2.0 寬鬆 (Permissive) 類似 MIT，但增加了明確的專利授權條款，對貢獻者和使用者提供額外保護 專案涉及可能具有專利爭議的技術
GNU GPLv3 著佐權 (Copyleft) 允許使用，但修改後的程式碼也必須以相同許可證開源（「傳染性」） 希望確保程式碼及所有衍生作品永遠保持開源

✍️ 如何為你的倉庫加入 MIT License？

1. 在你的 GitHub 倉庫頁面，點擊 「Add file」 下拉選單，選擇 「Create new file」。
2. 將檔案命名為 LICENSE 或 LICENSE.md。
3. 點擊頁面右側的 「Choose a license template」 按鈕。
4. 在左側列表中選擇 MIT License。
5. 在上方「Year」欄位填入 2026，「Fullname」欄位填入 Lightning Empire 或你的名字。
6. 點擊 「Review and submit」，然後在頁面下方點擊 「Commit new file」。

選擇 MIT License 能為你的展覽專案建立最開放的基礎。如果想更深入了解，可以參考 choosealicense.com 網站。
