
---
## TW_Stock-Benchmark_return
description:TW_Stock-回測基準

**table:benchmark_return**
| name | type |
| :--- | :----: |
|發行量加權股價報酬指數|float|


## TW_Stock-Capital_reduction_otc
description:TW_Stock-上櫃減資

**table:capital_reduction_otc**
| name | type |
| :--- | :----: |
|恢復買賣日期|str|
|減資原因|str|
|開始交易基準價|float|
|最後交易之收盤價格|float|
|減資恢復買賣開始日參考價格|float|
|漲停價格|float|
|跌停價格|float|
|除權參考價|float|
|otc_cap_divide_ratio|float|


## TW_Stock-Capital_reduction_tse
description:TW_Stock-上市減資

**table:capital_reduction_tse**
| name | type |
| :--- | :----: |
|恢復買賣日期|datetime|
|減資原因|str|
|恢復買賣參考價|float|
|停止買賣前收盤價格|float|
|漲停價格|float|
|跌停價格|float|
|開盤競價基準|float|
|除權參考價|float|
|twse_cap_divide_ratio|float|


## TW_Stock-Company_basic_info
description:TW_Stock-企業基本資訊

**table:company_basic_info**
| name | type |
| :--- | :----: |
|公司名稱|str|
|產業類別|str|
|外國企業註冊地國|str|
|住址|str|
|營利事業統一編號|str|
|董事長|str|
|總經理|str|
|發言人|str|
|發言人職稱|str|
|代理發言人|str|
|總機電話|str|
|成立日期|str|
|上市日期|str|
|普通股每股面額|str|
|實收資本額(元)|int|
|已發行普通股數或TDR原發行股數|int|
|私募普通股(股)|int|
|特別股(股)|int|
|編製財務報告類型|str|
|普通股盈餘分派或虧損撥補頻率|str|
|普通股年度(含第4季或後半年度)現金股息及紅利決議層級|str|
|股票過戶機構|str|
|過戶電話|str|
|過戶地址|str|
|簽證會計師事務所|str|
|簽證會計師1|str|
|簽證會計師2|str|
|英文簡稱|str|
|英文通訊地址|str|
|傳真機號碼|str|
|電子郵件信箱|str|
|公司網址|str|
|投資人關係聯絡人|str|
|投資人關係聯絡人職稱|str|
|投資人關係聯絡電話|str|
|投資人關係聯絡電子郵件|str|
|公司網站內利害關係人專區網址|str|
|市場別|str|
|上櫃日期|str|
|興櫃日期|str|


## TW_Stock-Company_main_business
description:TW_Stock-企業主要經營業務

**table:company_main_business**
| name | type |
| :--- | :----: |
|主要經營業務|str|


## TW_Stock-Disposal_information
description:TW_Stock-處置股

**table:disposal_information**
| name | type |
| :--- | :----: |
|處置條件|str|
|處置措施|str|
|處置內容|str|
|處置開始時間|datetime|
|處置結束時間|datetime|


## TW_Stock-Dividend_otc
description:TW_Stock-上櫃除權息

**table:dividend_otc**
| name | type |
| :--- | :----: |
|除權息前收盤價|float|
|除權息參考價|float|
|權值|float|
|息值|float|
|權+息值|float|
|權/息|float|
|漲停價格|float|
|跌停價格|float|
|開盤競價基準|float|
|減除股利參考價|float|
|現金股利|float|
|每千股無償配股|float|
|現金增資股數|float|
|現金增資認購價|float|
|公開承銷股數|float|
|員工認購股數|float|
|原股東認購數|float|
|按持股比例千股認購|float|
|otc_divide_ratio|float|


## TW_Stock-Dividend_tse
description:TW_Stock-上市除權息

**table:dividend_tse**
| name | type |
| :--- | :----: |
|除權息前收盤價|float|
|除權息參考價|float|
|權值+息值|float|
|權/息|float|
|漲停價格|float|
|跌停價格|float|
|開盤競價基準|float|
|減除股利參考價|float|
|詳細資料|str|
|最近一次申報資料 季別/日期|str|
|最近一次申報每股 (單位)淨值|float|
|最近一次申報每股 (單位)盈餘|float|
|twse_divide_ratio|float|


## TW_Stock-Financial_statement
description:TW_Stock-企業財報

**table:financial_statement**
| name | type |
| :--- | :----: |
|現金及約當現金|float|
|透過損益按公允價值衡量之金融資產_流動|float|
|透過其他綜合損益按公允價值衡量之金融資產_流動|float|
|按攤銷後成本衡量之金融資產_流動|float|
|避險之金融資產_流動|float|
|合約資產_流動|float|
|應收帳款及票據|float|
|其他應收款|float|
|存貨|float|
|待出售非流動資產|float|
|當期所得稅資產_流動|float|
|其他流動資產|float|
|流動資產|float|
|透過損益按公允價值衡量之金融資產_非流動|float|
|透過其他綜合損益按公允價值衡量之金融資產_非流動|float|
|按攤銷後成本衡量之金融資產_非流動|float|
|避險之金融資產_非流動|float|
|合約資產_非流動|float|
|採權益法之長期股權投資|float|
|預付投資款|float|
|不動產廠房及設備|float|
|商譽及無形資產合計|float|
|遞延所得稅資產|float|
|遞延資產合計|float|
|使用權資產|float|
|投資性不動產淨額|float|
|其他非流動資產|float|
|非流動資產|float|
|資產總額|float|
|短期借款|float|
|應付商業本票∕承兌匯票|float|
|透過損益按公允價值衡量之金融負債_流動|float|
|避險之金融負債_流動|float|
|按攤銷後成本衡量之金融負債_流動|float|
|合約負債_流動|float|
|應付帳款及票據|float|
|其他應付款|float|
|當期所得稅負債|float|
|負債準備_流動|float|
|與待出售非流動資產直接相關之負債|float|
|租賃負債─流動|float|
|一年內到期長期負債|float|
|特別股負債_流動|float|
|流動負債|float|
|透過損益按公允價值衡量之金融負債_非流動|float|
|避險之金融負債_非流動|float|
|按攤銷後成本衡量之金融負債_非流動|float|
|合約負債_非流動|float|
|特別股負債_非流動|float|
|應付公司債_非流動|float|
|銀行借款_非流動|float|
|租賃負債_非流動|float|
|負債準備_非流動|float|
|遞延貸項|float|
|應計退休金負債|float|
|遞延所得稅|float|
|非流動負債|float|
|負債總額|float|
|普通股股本|float|
|特別股股本|float|
|預收股款|float|
|待分配股票股利|float|
|換股權利證書|float|
|股本|float|
|資本公積合計|float|
|法定盈餘公積|float|
|未分配盈餘|float|
|保留盈餘|float|
|其他權益|float|
|庫藏股票帳面值|float|
|母公司股東權益合計|float|
|共同控制下前手權益|float|
|合併前非屬共同控制股權|float|
|非控制權益|float|
|股東權益總額|float|
|負債及股東權益總額|float|
|營業收入淨額|float|
|營業成本|float|
|營業毛利|float|
|營業費用|float|
|研究發展費|float|
|推銷費用|float|
|管理費用|float|
|預期信用減損_損失_利益_營業費用|float|
|其他收益及費損淨額|float|
|營業利益|float|
|財務成本|float|
|採權益法之關聯企業及合資損益之份額|float|
|營業外收入及支出|float|
|稅前淨利|float|
|所得稅費用|float|
|繼續營業單位損益|float|
|停業單位損益|float|
|合併前非屬共同控制股權損益|float|
|合併總損益|float|
|本期綜合損益總額|float|
|歸屬母公司淨利_損|float|
|歸屬非控制權益淨利_損|float|
|歸屬共同控制下前手權益淨利_損|float|
|綜合損益歸屬母公司|float|
|綜合損益歸屬非控制權益|float|
|綜合損益歸屬共同控制下前手權益|float|
|每股盈餘|float|
|繼續營業單位稅前淨利_淨損|float|
|本期稅前淨利_淨損|float|
|折舊費用|float|
|攤銷費用|float|
|呆帳費用提列_轉列收入_數|float|
|透過損益按公允價值衡量金融資產及負債之淨損失_利益|float|
|利息費用|float|
|利息收入|float|
|股利收入|float|
|採用權益法認列之關聯企業及合資損失_利益_之份額|float|
|處分及報廢不動產_廠房及設備損失_利益|float|
|處分無形資產損失_利益|float|
|處分投資損失_利益|float|
|非金融資產減損迴轉利益|float|
|未實現銷貨利益_損失|float|
|已實現銷貨損失_利益|float|
|未實現外幣兌換損失_利益|float|
|收益費損項目合計|float|
|應收帳款_增加_減少|float|
|應收帳款_關係人_增加_減少|float|
|存貨_增加_減少|float|
|與營業活動相關之資產之淨變動合計|float|
|應付帳款增加_減少|float|
|應付帳款_關係人增加_減少|float|
|與營業活動相關之負債之淨變動合計|float|
|營運產生之現金流入_流出|float|
|退還_支付_之所得稅|float|
|營業活動之淨現金流入_流出|float|
|取得透過其他綜合損益按公允價值衡量之金融資產|float|
|處分透過其他綜合損益按公允價值衡量之金融資產|float|
|取得不動產_廠房及設備|float|
|處分不動產_廠房及設備|float|
|取得無形資產|float|
|處分無形資產|float|
|收取之利息|float|
|收取之股利|float|
|其他投資活動|float|
|投資活動之淨現金流入_流出|float|
|短期借款增加|float|
|短期借款減少|float|
|應付短期票券增加|float|
|應付短期票券減少|float|
|發行公司債|float|
|償還公司債|float|
|舉借長期借款|float|
|償還長期借款|float|
|存入保證金增加|float|
|存入保證金減少|float|
|發放現金股利|float|
|支付之利息|float|
|籌資活動之淨現金流入_流出|float|
|本期現金及約當現金增加_減少_數|float|
|期初現金及約當現金餘額|float|
|期末現金及約當現金餘額|float|
|資產負債表帳列之現金及約當現金|float|


## TW_Stock-Important_subsidiary
description:TW_Stock-企業重要子公司資訊

**table:important_subsidiary**
| name | type |
| :--- | :----: |
|主要經營業務|str|
|地區|str|
|符合重要子公司認定之標準(註)|str|
|市場別|str|


## TW_Stock-Insider_shareholding_transfer_declaration
description:TW_Stock-內部人持股轉讓宣告

**table:insider_shareholding_transfer_declaration**
| name | type |
| :--- | :----: |
|申報人身分|str|
|預定轉讓方式及股數_轉讓股數|float|
|每日於盤中交易最大得轉讓股數|float|
|目前持有股數_自有持股|float|
|目前持有股數_保留運用決定權信託股數|float|
|預定轉讓總股數_自有持股|float|
|預定轉讓總股數_保留運用決定權信託股數|float|
|預定轉讓後持股_自有持股|float|
|預定轉讓後持股_保留運用決定權信託股數|float|
|是否申報持股未完成轉讓|str|
|有效轉讓開始日|datetime|
|有效轉讓截止日|datetime|
|市場別|str|


## TW_Stock-Institutional_investors_trading_all_market_summary
description:TW_Stock-整體市場三大法人買賣金額統計

**table:institutional_investors_trading_all_market_summary**
| name | type |
| :--- | :----: |
|買進金額|int|
|賣出金額|int|
|買賣超|int|


## TW_Stock-Institutional_investors_trading_summary
description:TW_Stock-三大法人買賣超

**table:institutional_investors_trading_summary**
| name | type |
| :--- | :----: |
|外陸資買進股數(不含外資自營商)|int|
|外陸資賣出股數(不含外資自營商)|int|
|外陸資買賣超股數(不含外資自營商)|int|
|外資自營商買進股數|int|
|外資自營商賣出股數|int|
|外資自營商買賣超股數|int|
|投信買進股數|int|
|投信賣出股數|int|
|投信買賣超股數|int|
|自營商買進股數(自行買賣)|int|
|自營商賣出股數(自行買賣)|int|
|自營商買賣超股數(自行買賣)|int|
|自營商買進股數(避險)|int|
|自營商賣出股數(避險)|int|
|自營商買賣超股數(避險)|int|


## TW_Stock-Internal_equity_changes
description:TW_Stock-內部人持股變化

**table:internal_equity_changes**
| name | type |
| :--- | :----: |
|發行股數|float|
|董監增加股數|float|
|董監減少股數|float|
|董監持有股數|float|
|董監持有股數占比|float|
|經理人持有股數|float|
|百分之十以上大股東持有股數|float|
|市場別|str|


## TW_Stock-Internal_equity_insufficient
description:TW_Stock-內部人持股不足數

**table:internal_equity_insufficient**
| name | type |
| :--- | :----: |
|發行股數|float|
|全體董事(不包含獨立董事)應持有股數|float|
|全體董事(不包含獨立董事)實際持有股數|float|
|全體董事(不包含獨立董事)法人代表人分戶集保股數|float|
|全體董事(不包含獨立董事)保留運用決定權信託股數|float|
|全體董事(不包含獨立董事)不足股數|float|
|監察人應持有股數|float|
|監察人應持有股數實際持有股數|float|
|監察人應持有股數法人代表人分戶集保股數|float|
|監察人應持有股數保留運用決定權信託股數|float|
|監察人應持有股數不足股數|float|
|持股不足已通知其董監|str|
|市場別|str|


## TW_Stock-Internal_equity_pledge
description:TW_Stock-內部人質押

**table:internal_equity_pledge**
| name | type |
| :--- | :----: |
|董監持股|float|
|董監設質|float|
|董監解質|float|
|董監累計設質|float|
|董監設質股數占比|float|
|經理人持股|float|
|百分之十以上大股東持有股數|float|
|經理人及百分之十以上大股東設質股數|float|
|經理人及百分之十以上大股東設質股數占比|float|
|市場別|str|


## TW_Stock-Intraday_trading
description:TW_Stock-當沖

**table:intraday_trading**
| name | type |
| :--- | :----: |
|當日沖銷交易成交股數|float|
|當日沖銷交易買進成交金額|float|
|當日沖銷交易賣出成交金額|float|


## TW_Stock-Intraday_trading_stat
description:TW_Stock-整體市場當沖統計

**table:intraday_trading_stat**
| name | type |
| :--- | :----: |
|當日沖銷交易總成交股數|float|
|當日沖銷交易總成交股數占市場比重|float|
|當日沖銷交易總買進成交金額|float|
|當日沖銷交易總買進成交金額占市場比重|float|
|當日沖銷交易總賣出成交金額|float|
|當日沖銷交易總賣出成交金額占市場比重|float|


## TW_Stock-Inventory
description:TW_Stock-集保餘額

**table:inventory**
| name | type |
| :--- | :----: |
|人數|int|
|持有股數|int|
|占集保庫存數比例|float|


## TW_Stock-Margin_balance
description:TW_Stock-整體市場融資券統計

**table:margin_balance**
| name | type |
| :--- | :----: |
|融資券總買進|float|
|融資券總賣出|float|
|現金(券)總償還|float|
|融資券總餘額|float|


## TW_Stock-Margin_transactions
description:TW_Stock-融資券

**table:margin_transactions**
| name | type |
| :--- | :----: |
|融資買進|int|
|融資賣出|int|
|融資現金償還|int|
|融資前日餘額|int|
|融資今日餘額|int|
|融資限額|int|
|融券買進|int|
|融券賣出|int|
|融券現券償還|int|
|融券前日餘額|int|
|融券今日餘額|int|
|融券限額|int|
|資券互抵|int|
|註記|str|
|融資使用率|float|
|融券使用率|float|


## TW_Stock-Monthly_revenue
description:TW_Stock-上市櫃月營收

**table:monthly_revenue**
| name | type |
| :--- | :----: |
|當月營收|int|
|上月營收|int|
|去年當月營收|int|
|上月比較增減(%)|float|
|去年同月增減(%)|float|
|當月累計營收|int|
|去年累計營收|int|
|前期比較增減(%)|float|


## TW_Stock-Oversea_investment
description:TW_Stock-企業海外轉轉資

**table:oversea_investment**
| name | type |
| :--- | :----: |
|公司名稱|str|
|投資公司名稱|str|
|地區別代號|str|
|本期期末持股比例|float|
|原始投資金額本期期末|float|
|原始投資金額去年年底|float|
|本期期末投資餘額|float|
|本期認列之投資損益|float|
|市場別|str|


## TW_Stock-Price
description:TW_Stock-上市櫃市場成交資訊

**table:price**
| name | type |
| :--- | :----: |
|成交股數|int|
|成交筆數|int|
|成交金額|int|
|收盤價|float|
|開盤價|float|
|最低價|float|
|最高價|float|
|最後揭示買價|float|
|最後揭示賣價|float|


## TW_Stock-Price_earning_ratio
description:TW_Stock-個股日本益比、殖利率及股價淨值比

**table:price_earning_ratio**
| name | type |
| :--- | :----: |
|殖利率(%)|float|
|本益比|float|
|股價淨值比|float|


## TW_Stock-Rotc_monthly_revnue
description:TW_Stock-興櫃月營收

**table:rotc_monthly_revnue**
| name | type |
| :--- | :----: |
|當月營收|float|
|上月營收|float|
|去年當月營收|float|
|上月比較增減(%)|float|
|去年同月增減(%)|float|
|當月累計營收|float|
|去年累計營收|float|
|前期比較增減(%)|float|
|備註|str|


## TW_Stock-Rotc_price
description:TW_Stock-興櫃月營收

**table:rotc_price**
| name | type |
| :--- | :----: |
|成交股數|float|
|成交金額|float|
|開盤價|float|
|收盤價|float|
|最高價|float|
|最低價|float|
|日均價|float|
|成交筆數|float|
|最後揭示買價|float|
|最後揭示賣價|float|


## TW_Stock-Security_lending
description:TW_Stock-借券

**table:security_lending**
| name | type |
| :--- | :----: |
|前日借券餘額|int|
|借券|int|
|借券還券|int|
|借券增減|int|
|借券餘額|int|


## TW_Stock-Security_lending_sell
description:TW_Stock-借券賣出

**table:security_lending_sell**
| name | type |
| :--- | :----: |
|借券賣出|int|
|借券賣出還券|int|
|借券賣出餘額|int|
|借券賣出限額|int|


## TW_Stock-Shareholders_meeting
description:TW_Stock-股東會期程

**table:shareholders_meeting**
| name | type |
| :--- | :----: |
|公司地址|str|
|股東會類別|str|
|開會地點|str|
|是否改選董監|str|
|聯絡電話|str|
|股務單位|str|
|股務單位電話|str|
|行使期間|str|
|電子投票平台|str|
|投票網址|str|
|公告日期|datetime|
|公告時間|str|
|市場別|str|


## TW_Stock-Stock_index_price
description:TW_Stock-指數資訊

**table:stock_index_price**
| name | type |
| :--- | :----: |
|收盤指數|float|
|漲跌百分比(%)|float|


## TW_Stock-Stock_index_vol
description:TW_Stock-指數成交量資訊

**table:stock_index_vol**
| name | type |
| :--- | :----: |
|成交股數|int|
|成交金額|float|
|成交筆數|int|


## TW_Stock-Trading_attention
description:TW_Stock-注意股

**table:trading_attention**
| name | type |
| :--- | :----: |
|注意交易資訊|str|
|收盤價|float|
|本益比|float|


## TW_Stock-Treasury_stock
description:TW_Stock-庫藏股

**table:treasury_stock**
| name | type |
| :--- | :----: |
|買回目的|str|
|買回股份總金額上限|float|
|預定買回股數|float|
|買回價格區間-最低|float|
|買回價格區間-最高|float|
|預定買回期間-起|datetime|
|預定買回期間-迄|datetime|
|是否執行完畢|str|
|本次已買回股數|float|
|本次執行完畢已註銷或轉讓股數|float|
|本次已買回股數佔預定買回股數比例(%)|float|
|本次已買回總金額|float|
|本次平均每股買回價格|float|
|本次買回股數佔公司已發行股份總數比例(%)|float|
|本次未執行完畢之原因|str|


## US_Stock-Us_fundamental
description:US_Stock-財報

**table:us_fundamental**
| name | type |
| :--- | :----: |
|calendardate|datetime|
|reportperiod|datetime|
|lastupdated|datetime|
|accoci|float|
|assets|float|
|assetsavg|float|
|assetsc|float|
|assetsnc|float|
|assetturnover|float|
|bvps|float|
|capex|float|
|cashneq|float|
|cashnequsd|float|
|cor|float|
|consolinc|float|
|currentratio|float|
|de|float|
|debt|float|
|debtc|float|
|debtnc|float|
|debtusd|float|
|deferredrev|float|
|depamor|float|
|deposits|float|
|divyield|float|
|dps|float|
|ebit|float|
|ebitda|float|
|ebitdamargin|float|
|ebitdausd|float|
|ebitusd|float|
|ebt|float|
|eps|float|
|epsdil|float|
|epsusd|float|
|equity|float|
|equityavg|float|
|equityusd|float|
|ev|float|
|evebit|float|
|evebitda|float|
|fcf|float|
|fcfps|float|
|fxusd|float|
|gp|float|
|grossmargin|float|
|intangibles|float|
|intexp|float|
|invcap|float|
|invcapavg|float|
|inventory|float|
|investments|float|
|investmentsc|float|
|investmentsnc|float|
|liabilities|float|
|liabilitiesc|float|
|liabilitiesnc|float|
|marketcap|float|
|ncf|float|
|ncfbus|float|
|ncfcommon|float|
|ncfdebt|float|
|ncfdiv|float|
|ncff|float|
|ncfi|float|
|ncfinv|float|
|ncfo|float|
|ncfx|float|
|netinc|float|
|netinccmn|float|
|netinccmnusd|float|
|netincdis|float|
|netincnci|float|
|netmargin|float|
|opex|float|
|opinc|float|
|payables|float|
|payoutratio|float|
|pb|float|
|pe|float|
|pe1|float|
|ppnenet|float|
|prefdivis|float|
|price|float|
|ps|float|
|ps1|float|
|receivables|float|
|retearn|float|
|revenue|float|
|revenueusd|float|
|rnd|float|
|roa|float|
|roe|float|
|roic|float|
|ros|float|
|sbcomp|float|
|sgna|float|
|sharefactor|float|
|sharesbas|float|
|shareswa|float|
|shareswadil|float|
|sps|float|
|tangibles|float|
|taxassets|float|
|taxexp|float|
|taxliabilities|float|
|tbvps|float|
|workingcapital|float|


## Macro-World_index
description:Macro-世界指數

**table:world_index**
| name | type |
| :--- | :----: |
|open|float|
|high|float|
|low|float|
|close|float|
|adj_close|float|
|vol|float|
