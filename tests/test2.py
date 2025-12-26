from finlab import data
from finlab import backtest

# -----------------------------------
# 1. 數據獲取
# -----------------------------------
# 使用正確的數據欄位代碼
close = data.get('price:收盤價')
pe = data.get('price_earning_ratio:本益比')
# 獲取基準指數
benchmark = data.get('benchmark_return:發行量加權股價報酬指數')

# -----------------------------------
# 2. 邏輯運算 (使用官方語法糖)
# -----------------------------------
# 計算 20 日均線
sma20 = close.average(20)

# 定義條件：收盤價 > 20MA 且 本益比 < 15
cond = (close > sma20) & (pe < 15)

# 選出符合條件中本益比最低的前 10 檔
position = cond.is_smallest(10)

# -----------------------------------
# 3. 回測執行
# -----------------------------------
# 修正名稱：必須以中文開頭
report = backtest.sim(
    position=position,
    resample='M',
    name='我的實戰策略_v1',  # 這裡已修正為中文開頭
    upload=True            # 上傳至官網
)

# 設定對標基準
report.benchmark = benchmark.squeeze()

# -----------------------------------
# 4. 輸出結果
# -----------------------------------
# 在 VS Code 中執行會嘗試開啟瀏覽器顯示報表
report.display()

# 額外在終端機印出前五筆統計數據，確保程式運作正常
print("\n--- 策略統計數據 ---")
print(report.get_stats())

# 印出當前最新的持股股票
print("\n--- 最新選股部位 ---")
last_pos = report.position.iloc[-1]
print(last_pos[last_pos > 0])