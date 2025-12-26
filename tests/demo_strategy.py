from finlab import data
from finlab import backtest

# -----------------------------------
# 1. 數據獲取
# -----------------------------------
# 獲取收盤價與本益比數據
close = data.get('price:收盤價')
pe = data.get('price_earning_ratio:本益比')
rev_growth = data.get('monthly_revenue:去年同月增減(%)')

# -----------------------------------
# 2. 邏輯運算
# -----------------------------------
# 條件1：股價在 60 日均線之上 (趨勢多頭)
sma60 = close.average(60)
cond_trend = close > sma60

# 條件2：本益比小於 15 (價值低估)
cond_value = pe < 15

# 條件3：營收成長大於 20% (基本面動能)
cond_growth = rev_growth > 20

# 綜合選股條件
selection = cond_trend & cond_value & cond_growth

# 選股濾網：選出本益比最小的前 20 檔
position = selection.is_smallest(20)

# -----------------------------------
# 3. 回測執行
# -----------------------------------
report = backtest.sim(
    position=position,
    resample='M',           # 每月換股
    name='低本益比成長策略_v1',
    stop_loss=0.1,          # 10% 停損
    take_profit=0.2,        # 20% 停利
    fee_ratio=1.425/1000,
    tax_ratio=3/1000
)

# 顯示回測結果
# report.display()
