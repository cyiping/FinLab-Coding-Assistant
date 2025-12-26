# SETUP.md
## Gemini Gem 設定說明（FinLab Coding Assistant）

本文件說明如何在 Gemini 中，
建立一個名為「FinLab Coding Assistant」的 Gem，
並正確掛載其 Knowledge Source。

---

## 1. 上傳檔案（Knowledge Source）

請在此 Gem 中，上傳以下三個權威文件（Authoritative Knowledge Sources）：

### 1.1 document.md
👉 官方技術規格與 API 定義（唯一真實來源）

包含內容：
- 函式庫用法
- 回測語法
- 指標計算
- 官方範例

---

### 1.2 database.md
👉 財經數據字典（Data Dictionary）

包含內容：
- 所有可用數據欄位
- 欄位代碼與語意說明

---

### 1.3 STYLE_GUIDE.md
👉 程式與策略風格標準

包含內容：
- 變數命名慣例
- 策略結構範本
- 回測參數預設與限制

---

## 2. 知識來源角色定義（重要）

- `document.md`  
  → **官方 API 與技術行為的唯一依據**

- `database.md`  
  → **所有可用財經數據欄位的完整清單**

- `STYLE_GUIDE.md`  
  → **策略程式碼的結構與撰寫風格標準**

Gem 在回應使用者問題時，
**必須以這三份文件作為主要推理與回答依據**。
