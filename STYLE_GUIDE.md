# FinLab 策略開發風格指南 (Style Guide)

* 本指南旨在統一 FinLab 策略程式碼的撰寫風格，確保程式碼的可讀性與一致性。
* 本文件為 FinLab 量化策略的統一撰寫規範，適用於所有人類工程師與 AI 助手（包含但不限於 ChatGPT、Gemini）。

## 1. 變數命名慣例 (Variable Naming Conventions)

為了讓程式碼語意清晰，請遵循以下命名規則：

*   **原始數據 (Raw Data)**：使用小寫英文，盡量與數據內容對應。
    *   收盤價：`close`
    *   開盤價：`open_` (避免與 python 內建 open 衝突)
    *   本益比：`pe`
    *   股價淨值比：`pb`
    *   月營收：`rev`
*   **技術指標 (Indicators)**：使用通用縮寫。
    *   移動平均：`sma` 或 `ma`
    *   相對強弱指標：`rsi`
    *   KD指標：`k`, `d`
*   **篩選條件 (Conditions)**：
    *   單一條件：使用 `cond` 前綴或具體描述，如 `cond1`, `cond_rsi`, `bullish_signal`。
    *   組合條件：通常命名為 `entries` (進場) 或 `exits` (出場)，若為單一訊號源則直接合併至 `position`。
*   **最終部位 (Final Position)**：
    *   傳入回測函式的變數統一命名為 **`position`**。
*   **回測報告 (Report)**：
    *   回測結果物件命名為 **`report`** 或 **`r`**。

**範例：**

```python
from finlab import data

# Data
close = data.get('price:收盤價')
pe = data.get('price_earning_ratio:本益比')

# Indicators
sma20 = close.average(20)

# Conditions
cond1 = close > sma20
cond2 = pe < 15

# Position
position = cond1 & cond2
```

## 2. 策略結構範本 (Strategy Structure Template)

標準的策略程式碼應包含以下四個區塊，並依序排列：

1.  **套件引入 (Imports)**：引入 `finlab.data` 與 `finlab.backtest`。
2.  **數據獲取 (Data Fetching)**：一次性獲取所有需要的數據。
3.  **邏輯運算 (Logic & Calculation)**：計算指標、定義條件、合成訊號。
4.  **回測執行 (Backtest Execution)**：設定參數並執行回測。

**標準範本：**

```python
from finlab import data
from finlab import backtest

# -----------------------------------
# 1. 數據獲取
# -----------------------------------
close = data.get('price:收盤價')
pe = data.get('price_earning_ratio:本益比')
# ... 其他數據

# -----------------------------------
# 2. 邏輯運算
# -----------------------------------
# 定義條件
cond_trend = close > close.average(60)  # 趨勢向上
cond_value = pe < 15                    # 價值低估

# 綜合選股條件
selection = cond_trend & cond_value

# 選股濾網 (例如：只選前 20 檔)
# 使用 FinlabDataFrame 的語法糖 is_largest / is_smallest
position = selection.is_largest(20)

# (選用) 設定多空部位或權重
# position = position * 0.5  # 設定權重

# -----------------------------------
# 3. 回測執行
# -----------------------------------
report = backtest.sim(
    position=position,
    resample='M',           # 換股頻率
    name='策略名稱_v1',      # 策略名稱
    stop_loss=0.1,          # 停損 (選填)
    take_profit=0.2         # 停利 (選填)
)

# 顯示結果
# report.display()
```

## 3. 回測參數標準寫法 (Backtesting Parameter Standards)

在使用 `finlab.backtest.sim` 時，請遵守以下參數設定建議：

*   **`position` (必填)**：
    *   必須是一個 `FinlabDataFrame` (Boolean 或 Float)。
    *   True 代表持有，False 代表空手；數值代表權重。
*   **`resample` (換股頻率)**：
    *   使用 pandas offset string 標準縮寫。
    *   `'D'`：每日 (Daily)
    *   `'W'`：每週 (Weekly) - 預設週日
    *   `'W-Fri'`：每週五 (Weekly on Friday)
    *   `'M'`：每月 (Monthly) - 月底
    *   `'Q'`：每季 (Quarterly)
*   **`name` (策略名稱)**：
    *   建議使用 **"中文名稱_版本號"** 或 **"英文名稱_版本號"**。
    *   範例：`"低本益比動能_v1"`, `"High_Dividend_Yield_v2"`。
    *   *注意：相同名稱的策略上傳會互相覆蓋。*
*   **`stop_loss` / `take_profit` (停損停利)**：
    *   使用浮點數表示百分比。
    *   `0.1` 代表 10%。
*   **`fee_ratio` / `tax_ratio` (交易成本)**：
    *   除非有特殊需求，否則使用預設值即可（預設為台股費率）。

**完整參數範例：**

```python
report = backtest.sim(
    position, 
    resample='M', 
    name="我的優質策略", 
    stop_loss=0.1, 
    take_profit=0.2, 
    fee_ratio=1.425/1000, 
    tax_ratio=3/1000,
    upload=True # 設為 False 可不傳至網站，僅本地跑測
)
```
