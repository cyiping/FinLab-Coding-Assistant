# -----------------------------------
# 請寫一個策略：買進收盤價大於 20 日均線，且本益比小於 12 的股票，每月換股。
# -----------------------------------
#!/usr/bin/env python
import finlab
finlab.login('您的 API_TOKEN')
from finlab import data
from finlab import backtest


# -----------------------------------
# 1. 數據獲取 (使用您已下載的欄位)
# -----------------------------------
close = data.get('price:收盤價')
pe = data.get('price_earning_ratio:本益比')
benchmark = data.get('benchmark_return:發行量加權股價報酬指數')

# -----------------------------------
# 2. 邏輯運算 (範例：價值動能策略)
# -----------------------------------
# 條件一：收盤價站上 60 日均線 (季線) 
sma60 = close.average(60)
cond_trend = close > sma60 

# 條件二：本益比處於低檔 (例如小於 15 倍)
cond_value = pe < 15

# 綜合條件並選出符合條件中本益比最低的 10 檔股票
position = (cond_trend & cond_value).is_smallest(10)

# -----------------------------------
# 3. 回測執行
# -----------------------------------
report = backtest.sim(
    position=position,
    resample='M',              # 每月月底換股
    name='價值動能策略_v1',      # 策略名稱
    upload=True                # 同步上傳至 FinLab 網站管理
)

# 設定回測報告的對標基準為加權報酬指數
report.benchmark = benchmark.squeeze()
# report.display()
