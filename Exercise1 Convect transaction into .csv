#referring https://hackmd.io/@s02260441/HJcMcnds8

from twstock import Stock
import pandas as pd
target_stock='6488'#目標股票代號 
target_year=2022#目標年份
target_month=7#目標月份
stock=Stock(target_stock)
target_price=stock.fetch_from(target_year,target_month)
name_attribute=['Date','Capacity','Turnover','Open','High','Low','Close','Change','Transaction']
df=pd.DataFrame(columns=name_attribute,data=target_price)
filename=f'./stock_data/{target_stock}.csv'

df.to_csv(filename)
