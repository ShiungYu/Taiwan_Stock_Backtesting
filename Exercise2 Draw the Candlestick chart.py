#Referring https://hackmd.io/v7m8LMfzQHu1y_dQNuXwbQ
#要先用Exercise創建出csv.檔
import pandas as pd #讀取.csv file...
import matplotlib #繪圖主要工具
import mplfinance as mpf 
target_stock='6488'
df=pd.read_csv(f'./stock_data/{target_stock}.csv',parse_dates=True,index_col=1)#讀取csv檔
df.rename(columns={'Turnover':'Volume'},inplace=True)#由於mplfinance模組中對於交易量的辨認是Volume這個字，所以我們使用pandas的df.rename()功能調整表頭
mc=mpf.make_marketcolors(up='r',down='g',inherit=True)
s=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc)
kwargs=dict(type='candle',mav=(5,20,60),volume=True,figratio=(10,8),figscale=0.75,title=target_stock,style=s)
mpf.plot(df,**kwargs)
