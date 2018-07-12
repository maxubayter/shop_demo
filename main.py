# -*- coding: utf-8 -*-

import requests
import json
import time

#апдейт бота
def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot603929717:AAHL0GmBrQko5rXSiddZAvrudsmSflJyEhg/getUpdates"
    par = {'limit' : limit, 'offset' : offset}
    result = requests.get(url, params = par)
    decoded = result.json()
    return decoded["result"]
#############################################

result = get_bot_updates(100, 0)
print(result)
message_id = 1


#прием данных от криптонатора
def currancy(coin):
    if coin == "/btc":
        url_coin = "https://api.cryptonator.com/api/ticker/btc-usd"
        result_coin = requests.get(url_coin)
        decoded_coin = result_coin.json()
        decoded_coin = decoded_coin['ticker']['price'] + " $"
    elif coin == "/eth":
        url_coin = "https://api.cryptonator.com/api/ticker/eth-usd"
        result_coin = requests.get(url_coin)
        decoded_coin = result_coin.json()
        decoded_coin = decoded_coin['ticker']['price'] + " $"
    elif coin == "/start":
        decoded_coin = "Бот выводит курс криптовалют bitcoin и ethereum с ресурса https://ru.cryptonator.com/. Для получения актуального курса на данный момент времени, введите в чате /btc (для биткоина), /eth (для эфириума)"
    else:
        decoded_coin = "wrong coin"
       
    return decoded_coin
###############################################


while True:         #обновление входящих сообщений

    for item in result:
        message_id = item["update_id"]
        message_text = item['message']['text']
        print(message_text)

        answer = currancy(message_text)
        print(currancy(message_text))

        chat_id = item['message']['chat']['id']
        print(chat_id)
        requests.post("https://api.telegram.org/bot603929717:AAHL0GmBrQko5rXSiddZAvrudsmSflJyEhg/sendMessage", params = {"chat_id" : chat_id, "text" : answer})

    new_offset = message_id + 1
    result = get_bot_updates(100, new_offset)

    #time.sleep(2)