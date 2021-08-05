import pandas as pd
import numpy as np
from datetime import datetime #becz we want only one function datetime
import matplotlib.pyplot as plt #use to make charts

plt.style.use('fivethirtyeight')
#Load the data
reliance = pd.read_csv('RELIANCE.NS.csv')


#create the simple moving average with a 30 days window
SMA30=pd.DataFrame()
SMA30['Close']=reliance['Close'].rolling(window=30).mean()
SMA100=pd.DataFrame()
SMA100['Close']=reliance['Close'].rolling(window=100).mean()




#create a new data frame to store all the data
data=pd.DataFrame()
data['RELIANCE']=reliance['Close']
data['SMA30']=SMA30['Close']
data['SMA100']=SMA100['Close']
#print(data)
#create  a func to signal when to buy and sell
def buy_sell(data):
    sigPriceBuy=[]
    sigPriceSell=[]
    flag=-1

    for i in range(len(data)):
        if data['SMA30'][i]>data['SMA100'][i]:
            if flag!=1:
                sigPriceBuy.append(data['RELIANCE'][i])
                sigPriceSell.append(np.nan)
                flag=1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i]<data['SMA100'][i]:
            if flag!=0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['RELIANCE'][i])
                flag=0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
    return (sigPriceBuy,sigPriceSell)


#Store the buy and sell data into a variable 
buy_sell_data= buy_sell(data)
data['Buy_Signal_Price']=buy_sell_data[0]
data['Sell_Signal_Price']=buy_sell_data[1]
#print(data)

#visualize the data and market trend of buy and sell
plt.figure(figsize=(12.5,5.5))
plt.plot(data['RELIANCE'],label='RELIANCE Close Price',alpha=0.5)
plt.plot(data['SMA30'],label='SMA30',alpha=0.5)
plt.plot(data['SMA100'],label='SMA100',alpha=0.5)
plt.scatter(data.index, data['Buy_Signal_Price'],label='Buy',marker='^',color='green')
plt.scatter(data.index, data['Sell_Signal_Price'],label='Buy',marker='v',color='red')
plt.title('RELIANCE Close price history of buy and sell')
plt.xlabel('12-Aug,2002- 5 May,2021')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
