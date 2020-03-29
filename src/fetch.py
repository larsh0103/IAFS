import pandas as pd
import yfinance as yf

def get_stock_history(symbol,period='10y',name=None):
    
    if name: 
        df = (
            yf.Ticker(symbol).history(period=period)
            .assign(Ticker=symbol)
            .assign(Name=name)
        )
    else:
        df = (
            yf.Ticker(symbol).history(period=period)
            .assign(Ticker=symbol)
        )
    
    return df




def get_multiple_stock_history(ticker_dict):
    df = pd.DataFrame(columns = get_stock_history(list(ticker_dict.keys())[0]).columns)
    for key,name in ticker_dict.items():
        df= pd.concat((df, get_stock_history(key,period='3mo',name=name)))
    df['Date'] = df.index
    df =df.reset_index(drop=True)
    return df