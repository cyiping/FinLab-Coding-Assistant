# FinLab Code Assistant

本專案旨在提供一套標準化的知識庫與設定文件，協助使用者在 **ChatGPT** 或 **Gemini** 等大型語言模型 (LLM) 中，建立一個專業且準確的 **FinLab 量化交易程式碼助手**。

透過掛載本專案提供的文件，您的 AI 助手將能夠：
1.  **準確撰寫**符合 FinLab API 規範的策略程式碼。
2.  **正確查詢**可用的財經數據欄位代碼。
3.  **統一風格**，產出易讀、好維護的程式碼結構。

---

## 📂 目錄結構

```text
FinLab-Coding-Assistant/
├── document.md             # API 技術規格與語法說明
├── database.md             # 財經數據字典 (Data Dictionary)
├── STYLE_GUIDE.md          # 程式碼風格指南
├── ChatGPT/                # ChatGPT 專用設定
│   ├── SETUP.md            # 設定與上傳步驟
│   └── SYSTEM_INSTRUCTION.md # 系統提示詞 (System Prompt)
├── Gemini/                 # Gemini 專用設定
│   ├── SETUP.md            # 設定與上傳步驟
│   └── SYSTEM_INSTRUCTION.md # 系統提示詞 (System Prompt)
├── README.md               # 本說明文件
├── CHANGELOG.md            # AI 規則變更紀錄
├── GOVERNANCE.md           # 審核 / 責任 / 版本政策
└── tests/                  # AI 輸出驗證案例（進階）

```

---

## 🚀 快速開始

請根據您使用的 AI 平台，選擇對應的設定指南：

### 🤖 使用 ChatGPT (Custom GPT / Project)

1.  進入 `ChatGPT/` 資料夾。
2.  閱讀 **`SETUP.md`**，了解如何上傳知識庫檔案。
3.  複製 **`SYSTEM_INSTRUCTION.md`** 的內容，貼入 GPT 的 Instructions 欄位。
4.  上傳根目錄中的 `document.md`、`database.md` 以及 `STYLE_GUIDE.md` 至 Knowledge 區塊。

### 💎 使用 Gemini (Gems)

1.  進入 `Gemini/` 資料夾。
2.  閱讀 **`SETUP.md`**，了解如何建立 Gem 並掛載知識庫。
3.  複製 **`SYSTEM_INSTRUCTION.md`** 的內容，貼入 Gem 的 System Instructions 欄位。
4.  上傳根目錄中的 `document.md`、`database.md` 以及 `STYLE_GUIDE.md` 至 Knowledge Source。

---

## 📚 核心文件說明

| 檔案名稱 | 用途 | 重要性 |
| :--- | :--- | :--- |
| **`document.md`** | **API 規格書**。包含函式庫用法、回測語法、指標計算範例。 | ⭐⭐⭐⭐⭐ (核心大腦) |
| **`database.md`** | **數據字典**。包含所有可用的財經數據欄位名稱與代碼。 | ⭐⭐⭐⭐⭐ (核心字典) |
| **`STYLE_GUIDE.md`** | **風格指南**。定義變數命名、策略結構與參數標準。 | ⭐⭐⭐⭐ (品質保證) |

---

## 💡 使用技巧

建立好您的 FinLab Assistant 後，您可以這樣問它：

*   「幫我寫一個本益比小於 15 且股價在季線之上的策略。」
*   「如何計算近 5 日的平均成交量？」
*   「我要查詢『營業利益率』的數據代碼是什麼？」
*   「請幫我優化這段程式碼，使其符合 Style Guide。」

---

## ⚠️ 注意事項

*   **知識庫更新**：若 FinLab API 或數據欄位有更新，請務必同步更新根目錄中的文件，並重新上傳至您的 AI 助手。
*   **隱私安全**：本專案提供的文件均為公開技術規格，不包含任何個人 API Token 或私鑰，請安心使用。
