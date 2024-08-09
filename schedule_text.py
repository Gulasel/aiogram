import schedule
import time
import requests

def test():
    print("Hello Itpark")
    print(time.ctime())
    
def get_btc_price():
    print("=====BTCUSDT=====")
    url='https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response=requests.get(url=url).json()
    price=response.get("price")
    print(f'Стоимость биткоина на текущее время:{time.ctime()}, цена {price}')
      
# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at("10:30").do(test)
# schedule.every().thursday.at("10:34").do(test)
# schedule.every().hour.at(":35").do(test)



schedule.every(2).seconds.do(get_btc_price)
while True:
    schedule.run_pending()
    # time.sleep(2)