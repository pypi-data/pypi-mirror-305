import yfinance as yf
import pandas as pd
import plotly.express as px
import sys

""" period ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', 'ytd', 'max']")"""
def tickerReturn(scrip,period,**kwargs):
    chartShow = kwargs.get('chart', None)
    returns = []
    scrips = scrip.split(" ") 
    itr  = len(scrip.split(" "))
    df = yf.download(scrip, period=period)
    if df.empty:
        print("Provide valid data to continue")
        sys.exit()
    df2=df.reset_index()
    df.index = df.index.set_names(['new_index1'])
    df2 = df.reset_index(level=[0])
    df.index = df.index.set_names(['new_index1'])
    df2 = df.reset_index(level=[0])
    df2 = df.reset_index(level=[0], drop=True)
    df.columns = df.columns.get_level_values(1)
    df.reset_index(drop=True, inplace=True)
    for its in range(itr):
        val = df.iloc[:, its]
        first_val = round(val[0])
        last_val = round(val.tail(1).item())
        change = round((last_val-first_val)/first_val*100)
        returns.append(change)

    if(chartShow=="yes"):
        df3 = pd.DataFrame(list(zip(scrips, returns)),columns =['Stock', 'Return'])
        fig = px.bar(df3, x='Stock',y='Return',color="Stock",labels={'Return':'Return in %'},title="Stock return in given period",width=800,height=600).update_traces(width=0.2)
        fig.update_layout(bargap=0.0,bargroupgap=0)
        fig.update_yaxes(automargin=True, ticksuffix="%")
        fig.show()
        return scrips,returns
    else:
        return scrips,returns

# scrip = "ITC.NS TCS.NS LTFOODS.NS"
# scrips,returns = tickerReturn("ITC.NS TCS.NS LTFOODS.NS",period="1mo",chart="yes")
# #scrips,returns = tickerReturn("ITC.NS TCS.NS LTFOODS.NS",period="1mo")
# print(returns)
# print("*************************End of Process****************************")