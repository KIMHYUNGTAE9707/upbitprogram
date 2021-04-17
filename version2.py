import pyupbit as pu
import time
from datetime import datetime, timedelta

access = "33a3a5IacumnipasRVQ8C5yqn0u9oKtWBk7yi42E"
secret = "jWKTxSNm1scFxsuy06DRMWPPRkj1uVQaNWpS2wgm"
my_id = pu.Upbit(access, secret)

my_money = my_id.get_balances()[0]

tickers = pu.get_tickers(fiat="KRW")
tickers.remove("KRW-BTC")
tickers.remove("KRW-ETH")
tickers.remove("KRW-BCH")
tickers.remove("KRW-BSV")
count_tickers = len(tickers)

def waiting_time():
    now = datetime.now()
    # go 5 minutes into the future
    later5min = now + timedelta(0, 0, 0, 0, 5)  # 분봉 교체시 교체
    # round to 5 minutes
    next5min = datetime(later5min.year, later5min.month, later5min.day, later5min.hour, 5 * int(later5min.minute / 5),
                        0, 0)  # 분봉 교체시 교체
    time.sleep((next5min - now).total_seconds())

i = 0
a = 0
print("5분 차트를 기다리는중")
waiting_time()
time.sleep(10)
while a < 1:

    coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
    coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
    coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
    coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
    candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

    candle2_start_price = coin_candle.iloc[1, 0]
    candle3_start_price = coin_candle.iloc[2, 0]
    candle2_finish_price = coin_candle.iloc[1, 3]
    candle3_finish_price = coin_candle.iloc[2, 3]
    coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

    def round_profit_sell():
        my_coin = my_id.get_balances()[1]
        profit_sell = float(my_coin.get('avg_buy_price')) * 1.0065 #수익률 교체시 교체
        if profit_sell < 10:
            profit_sell = round(profit_sell, 2)
        if 10 <= profit_sell < 100:
            profit_sell = round(profit_sell, 1)
        if 100 <= profit_sell < 1000:
            profit_sell = round(profit_sell, 0)
        if 1000 <= profit_sell < 10000:
            profit_sell = round(profit_sell / 5, 0) * 5
        if 10000 <= profit_sell < 100000:
            profit_sell = round(profit_sell, -1)
        if 100000 <= profit_sell < 1000000:
            profit_sell = round(profit_sell / 5, -1) * 5
        if 1000000 <= profit_sell < 2000000:
            profit_sell = round(profit_sell / 5, -2) * 5
        if 2000000 <= profit_sell:
            profit_sell = round(profit_sell, -3)
        print(my_id.sell_limit_order(tickers[i], profit_sell, float(my_coin.get('balance'))))

    def round_nothing_sell():
        my_coin = my_id.get_balances()[1]
        nothing_sell = float(my_coin.get('avg_buy_price')) * 1.001 #수익률 교체시 교체
        if nothing_sell < 10:
            nothing_sell = round(nothing_sell, 2)
        if 10 <= nothing_sell < 100:
            nothing_sell = round(nothing_sell, 1)
        if 100 <= nothing_sell < 1000:
            nothing_sell = round(nothing_sell, 0)
        if 1000 <= nothing_sell < 10000:
            nothing_sell = round(nothing_sell / 5, 0) * 5
        if 10000 <= nothing_sell < 100000:
            nothing_sell = round(nothing_sell, -1)
        if 100000 <= nothing_sell < 1000000:
            nothing_sell = round(nothing_sell / 5, -1) * 5
        if 1000000 <= nothing_sell < 2000000:
            nothing_sell = round(nothing_sell / 5, -2) * 5
        if 2000000 <= nothing_sell:
            nothing_sell = round(nothing_sell, -3)
        print(my_id.sell_limit_order(tickers[i], nothing_sell, float(my_coin.get('balance'))))

    def water_buying_process():

        coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
        coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
        coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
        coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
        candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

        candle2_start_price = coin_candle.iloc[1, 0]
        candle3_start_price = coin_candle.iloc[2, 0]
        candle2_finish_price = coin_candle.iloc[1, 3]
        candle3_finish_price = coin_candle.iloc[2, 3]
        coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

        water_buying_count = 0
        water_buying_button1 = 0
        while water_buying_button1 == 0:

            coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
            coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
            coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
            coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
            candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

            candle2_start_price = coin_candle.iloc[1, 0]
            candle3_start_price = coin_candle.iloc[2, 0]
            candle2_finish_price = coin_candle.iloc[1, 3]
            candle3_finish_price = coin_candle.iloc[2, 3]
            coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

            if len(my_id.get_order(tickers[i])) > 0:
                my_coin = my_id.get_balances()[1]
                if candle3_finish_price < float(my_coin.get('avg_buy_price')):
                    print(my_id.cancel_order(my_id.get_order(tickers[i])[0].get('uuid')))
                    time.sleep(2.5)
                    print(my_id.buy_limit_order(tickers[i], candle3_finish_price, coin_count))
                    water_buying_button2 = 0
                    wait_water_button_time = 0
                    while water_buying_button2 == 0:

                        coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
                        coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
                        coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
                        coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
                        candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

                        candle2_start_price = coin_candle.iloc[1, 0]
                        candle3_start_price = coin_candle.iloc[2, 0]
                        candle2_finish_price = coin_candle.iloc[1, 3]
                        candle3_finish_price = coin_candle.iloc[2, 3]
                        coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

                        time.sleep(2.5)
                        if len(my_id.get_order(tickers[i])) == 0:
                            print("추가매수")
                            water_buying_count += 1
                            if water_buying_count == 3:
                                time.sleep(2.5)
                                round_nothing_sell()
                                exit_button = 0
                                while exit_button == 0:

                                    my_coin = my_id.get_balances()[1]
                                    coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
                                    coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
                                    coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
                                    coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
                                    candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

                                    candle2_start_price = coin_candle.iloc[1, 0]
                                    candle3_start_price = coin_candle.iloc[2, 0]
                                    candle2_finish_price = coin_candle.iloc[1, 3]
                                    candle3_finish_price = coin_candle.iloc[2, 3]
                                    coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

                                    time.sleep(2.5)
                                    if len(my_id.get_order(tickers[i])) > 0:
                                        if float(my_coin.get('avg_buy_price')) * 0.99 >= pu.get_current_price(tickers[i]):
                                            print(my_id.cancel_order(my_id.get_order(tickers[i])[0].get('uuid')))
                                            time.sleep(3)
                                            if float(my_coin.get('balance')) > 0:
                                                print(my_id.sell_market_order(tickers[i], float(my_coin.get('balance'))))
                                                print("손해 매도")
                                                exit_button = 1
                                                water_buying_button2 = 1
                                                water_buying_button1 = 1
                                            else:
                                                round_nothing_sell()
                                        else:
                                            return
                                    else:
                                        print("환수 매도")
                                        exit_button = 1
                                        water_buying_button2 = 1
                                        water_buying_button1 = 1
                            else:
                                time.sleep(2.5)
                                round_profit_sell()
                                waiting_time()
                                time.sleep(10)
                                if len(my_id.get_order(tickers[i])) > 0:
                                    water_buying_button2 = 1
                                else:
                                    print("이익 매도")
                                    water_buying_button2 = 1
                                    water_buying_button1 = 1
                        else:
                            wait_water_button_time = wait_water_button_time + 1
                            if wait_water_button_time == 30:
                                print(my_id.cancel_order(my_id.get_order(tickers[i])[0].get('uuid')))
                                time.sleep(2.5)
                                round_profit_sell()
                                waiting_time()
                                time.sleep(10)
                                if len(my_id.get_order(tickers[i])) == 0:
                                    print("이익 매도")
                                    water_buying_button2 = 1
                                    water_buying_button1 = 1
                                else:
                                    water_buying_button2 = 1
            else:
                print("이익 매도")
                water_buying_button1 = 1

    if i + 1 == len(tickers):
        i = 0
        print("5분 차트를 기다리는중")
        waiting_time()
        time.sleep(10)

    if coin_candle_info2 < 0 and coin_candle_info3 < 0 and (candle3_finish_price / candle2_start_price) <= 0.99 and candle_volume >= 80000000 and candle2_finish_price >= candle3_start_price:
        print("조건 만족 코인 발견")
        print(tickers[i])
        print(my_id.buy_limit_order(tickers[i], candle3_finish_price, coin_count))

        buying_sell_button1 = 0
        wait_buying_time1 = 0
        while buying_sell_button1 == 0:

            coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
            coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
            coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
            coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
            candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

            candle2_start_price = coin_candle.iloc[1, 0]
            candle3_start_price = coin_candle.iloc[2, 0]
            candle2_finish_price = coin_candle.iloc[1, 3]
            candle3_finish_price = coin_candle.iloc[2, 3]
            coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

            time.sleep(2.5)
            if len(my_id.get_order(tickers[i])) == 0:
                print("매수")
                time.sleep(2.5)
                round_profit_sell()
                buying_sell_button2 = 0
                wait_selling_time1 = 0
                while buying_sell_button2 == 0:

                    coin_candle = pu.get_ohlcv(tickers[i], interval="minute5", count="4")  # 분봉 교체시 교체
                    coin_candle_info1 = coin_candle.iloc[0, 3] - coin_candle.iloc[0, 0]
                    coin_candle_info2 = coin_candle.iloc[1, 3] - coin_candle.iloc[1, 0]
                    coin_candle_info3 = coin_candle.iloc[2, 3] - coin_candle.iloc[2, 0]
                    candle_volume = ((coin_candle.iloc[0, 4] + coin_candle.iloc[1, 4] + coin_candle.iloc[2, 4]) * pu.get_current_price(tickers[i])) / 3

                    candle2_start_price = coin_candle.iloc[1, 0]
                    candle3_start_price = coin_candle.iloc[2, 0]
                    candle2_finish_price = coin_candle.iloc[1, 3]
                    candle3_finish_price = coin_candle.iloc[2, 3]
                    coin_count = 1000000 / candle3_finish_price  # 투자금 교체시 교체

                    time.sleep(2.5)
                    if len(my_id.get_order(tickers[i])) == 0:
                        print("이익 매도")
                        buying_sell_button2 = 1
                    else:
                        wait_selling_time1 = wait_selling_time1 + 1
                        if wait_selling_time1 == 45:
                            waiting_time()
                            time.sleep(10)
                            if len(my_id.get_order(tickers[i])) > 0:
                                water_buying_process()
                            else:
                                print("이익 매도")
                            buying_sell_button2 = 1

                buying_sell_button1 = 1


            else:
                wait_buying_time1 = wait_buying_time1 + 1
                if wait_buying_time1 == 20:
                    print(my_id.cancel_order(my_id.get_order(tickers[i])[0].get('uuid')))
                    buying_sell_button1 = 1

        waiting_time()
        time.sleep(10)
        print("다음 코인 확인")
        i = 0
        i = i + 1

    else:
        time.sleep(0.03)
        print("다음 코인 확인")
        i = i + 1
