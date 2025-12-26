# SETUP.md
## ChatGPT Project / Custom GPT 設定說明

本文件說明如何在 ChatGPT Project / Custom GPT 中，
建立一個「FinLab Coding Assistant」所需的知識檔案結構。

---

## 1. 上傳檔案（Project Knowledge / Files）

請在此 ChatGPT 專案中，上傳以下三個權威文件（Authoritative Sources）：

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

## 2. 文件角色定義（非常重要）

- `document.md`  
  → **API 與技術規範的唯一真實來源（Single Source of Truth）**

- `database.md`  
  → **所有資料欄位的唯一允許清單**

- `STYLE_GUIDE.md`  
  → **所有策略程式碼的結構與風格標準**

任何不在上述文件中定義的內容，  
**一律視為不存在、不可使用**。
