# LLM 回答測試案例 (Test Prompts)

本文件提供了一系列測試問題，用於驗證您的 FinLab Coding Assistant 是否正確掛載了知識庫，並遵守了系統指令。

---

## 測試 1：基礎策略生成
**Prompt:**
> 請寫一個策略：買進收盤價大於 20 日均線，且本益比小於 12 的股票，每月換股。

**預期行為 (Expected Behavior):**
1.  **變數命名**：應使用 `close`, `pe`, `sma20`, `cond...` 等符合 Style Guide 的命名。
2.  **數據代碼**：應正確使用 `price:收盤價` 和 `price_earning_ratio:本益比`。
3.  **語法糖**：應使用 `close.average(20)` 而不是 `talib` 或 `rolling().mean()` (雖然也可以，但優先使用語法糖)。
4.  **結構**：應包含 `Imports`, `Data Fetching`, `Logic`, `Backtest` 四個區塊。

---

## 測試 2：數據欄位查詢 (Database Check)
**Prompt:**
> 我想用「營業利益率」當作選股條件，請問代碼是什麼？

**預期行為:**
*   AI 應查閱 `database.md` 並回答：`fundamental_features:營業利益率`。
*   若 AI 回答 `operating_margin` (英文代碼) 或其他不存在的代碼，代表 `database.md` 掛載失敗或權重不足。

---

## 測試 3：API 幻覺測試 (Hallucination Check)
**Prompt:**
> 請幫我用 `finlab.get_stock_price('2330')` 抓取台積電股價。

**預期行為:**
*   **AI 應拒絕或修正**。
*   正確回答應為：「FinLab API 中沒有 `get_stock_price` 函式，請使用 `finlab.data.get('price:收盤價')` 獲取全市場資料後，再篩選 `['2330']`。」
*   這驗證了 AI 是否嚴格遵守 `document.md`。

---

## 測試 4：Style Guide 驗證
**Prompt:**
> 寫一個簡單的 RSI 策略。

**預期行為:**
*   檢查 `backtest.sim` 中的參數。
*   `resample` 應為 `'M'` 或 `'W'` 等標準字串。
*   `name` 應有命名。
*   變數 `position` 應被正確定義並傳入。
