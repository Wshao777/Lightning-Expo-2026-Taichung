OPER-PY3 AI Development Policy

1. Public Repository Principle

OPER-PY3 的公開 Repository 以技術文件與開發規範為主要公開內容。

公開區域原則上只允許 Markdown 文件。

AI 不得自行將私人核心程式、憑證、個人資料或本機執行環境提交至公開 Repository。

2. AI Allowed File Types

在 OPER-PY3 開發環境中，AI 只有在使用者明確授權時，才可以建立或修改以下檔案：

.py
.md
.json

其中：

- ".py"：Python 原始碼
- ".md"：文件、規格、架構與開發說明
- ".json"：經使用者授權的結構化資料

3. AI Forbidden File Types

AI 不得自行建立、下載、編譯、產生或加入以下類型：

.exe
.msi
.bat
.cmd
.com
.sh
.bash
.zsh
.dll
.so
.dylib
.bin

也不得自行建立：

未知格式的可執行檔
未知來源的二進位檔
未授權的動態函式庫
未授權的安裝程式

除非使用者明確提出需求並確認用途，AI 不得自行產生上述檔案。

4. No Silent Installation

AI 不得：

- 自行安裝未知軟體
- 自行下載未知執行檔
- 自行執行外部二進位檔
- 自行建立 Windows 啟動腳本
- 自行修改系統啟動項目
- 自行建立常駐背景程式
- 自行建立資料採集器
- 自行加入未授權的遠端控制功能

任何系統級操作都必須由使用者明確授權。

5. No Credential Collection

AI 不得要求或儲存：

- Facebook 密碼
- GitHub 密碼
- API Secret
- Access Token
- Cookie
- Session
- SSH Private Key
- 個人身分資料

憑證不得寫入公開 Repository。

6. Public Repository Rule

公開 Repository 的內容應以：

README.md
docs/*.md
LICENSE

等公開文件為主。

私人 Python 原始碼、OPER Core、AI 實作、Bot 實作與本機資料不得因 AI 自動化而意外公開。

7. AI File Creation Rule

AI 建立新檔案前必須確認：

1. 檔案名稱
2. 副檔名
3. 所屬目錄
4. 是否屬於公開 Repository
5. 是否包含私人資料
6. 是否包含憑證
7. 是否具有執行或系統修改能力

若無法確認，AI 應停止建立檔案，而不是自行猜測。

8. No Automatic Repository Expansion

AI 不得自行：

- 建立大量新目錄
- 建立大量空白檔案
- 複製不存在的模組
- 假設不存在的 API
- 假設不存在的核心功能
- 自動增加未經要求的 Bot
- 自動加入追蹤器
- 自動加入資料採集器

專案架構必須以現有 Repository 與使用者明確指示為準。

9. OPER Core

OPER Core 屬於開發者控制範圍。

公開文件可以描述架構與介面，但不得因 AI 自動化而將私人核心原始碼、秘密設定或未授權資料公開。

10. Principle

OPER-PY3 的 AI 開發原則：

«AI 可以協助建構。

AI 不得自行擴張權限。

AI 可以產生程式碼。

AI 不得自行產生未授權的執行檔。

AI 可以整理文件。

AI 不得自行公開私人核心。

AI 是開發工具，不是 Repository 所有者。»
