# fetquest
 
FETQUEST library is based on yfinance lib, Package to help on Stock Market Visualization and Data Handaling.

To find out the period return i.e for 1 year or 1 month use the below function. for Indian stock market use "{ScripName}.NS"
```
To Get Chart on the data use. {chart="yes"}

from fetquest import tickerReturn
scrips,returns = tickerReturn("SBIN.NS HDFCBANK.NS",period="3mo",chart="yes")


from fetquest import tickerReturn
scrips,returns = tickerReturn("SBIN.NS HDFCBANK.NS",period="3mo")
```
Periods accepted are '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', 'ytd', 'max'

By using space as delimiter Scrips can be added.

This will return the Scrips provided in list -{scrips} and percentage return in {retruns} variables.

New Functions will be added as developed.