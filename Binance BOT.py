import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager


client = Client('kNVxvm7mkxeKWIjD516jKJDSWiR1gh87Tv2zJMjWH9tKXZybki9orhz6ENkakKiN','r99UZGBOm473d108lTxSJ4B6OmrS41SHwmroKZ2hBnT2VxEe8rZguCFAuE7XQjgw')
bsm = BinanceSocketManager(client)
socket = bsm.trade_socket('BTCBUSD')

async def main():
    await socket.__aenter__()
    msg = await socket.recv()
    print(msg) 

#while True:
    #async def main():
        
        #await socket.__aenter__()
        #msg = await socket.recv()
        #frame = createframe(msg)
        #frame.to_sql('BTCBUSD', engine, if_exists='append', index=False)
        #print(frame)

    #def createframe(msg):
       # df = pd.DataFrame([msg])
       # df = df.loc[:,['s','E','p']]
      #  df.columns = ['symbol','Time','Price']
      #  df.Price = df.Price.astype(float)
      #  df.Time = pd.to_datetime(df.time, unit = 'ms')
       # return df
       # createframe(msg)    

  #  engine = sqlalchemy.create_engine('sqlite:///BTCBUSDstream.db')
