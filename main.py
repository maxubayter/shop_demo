# -*- coding: utf-8 -*-
import requests
import json
import time

token = "603929717:AAHL0GmBrQko5rXSiddZAvrudsmSflJyEhg"
coins_list = ['/btc' , '/eth' , '/ltc' , '/bch' , '/xmr' , '/xrp' , '/zec']
message_id = 1
chat_id = 1

#апдейт бота
def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot" + token + "/getUpdates"
    par = {'limit' : limit, 'offset' : offset}
    result = requests.get(url, params = par)
    decoded = result.json()
    return decoded["result"]
result = get_bot_updates(100, 0)

#прием данных от криптонатора
def get_cryptonator(coin):
    url_coin = "https://api.cryptonator.com/api/ticker" + coin + "-usd"
    get_price = requests.get(url_coin)
    decoded_price = get_price.json()
    decoded_price = decoded_price['ticker']['price'] + " $"
    return decoded_price

#обновление входящих сообщений
while True:         
    for item in result:
        message_id = item["update_id"]
        message_text = item['message']['text']
        print(message_text)
        if message_text in coins_list:
            answer = get_cryptonator(message_text)
            print(get_cryptonator(message_text))
            chat_id = item['message']['chat']['id']
            print(chat_id)
        elif message_text == "/start":
            answer = "Бот выводит курс криптовалют bitcoin и ethereum с ресурса https://ru.cryptonator.com/. Для получения актуального курса на данный момент времени, введите в чате /btc (для Bitcoin), /eth (для Ethereum), /ltc (для Litecoin), /bch (для Bitcoin Cash), /xmr (для Monero), /xrp (для Ripple), /zec (для Zcash)"
        else:
            answer = "Wrong coin"
        requests.post("https://api.telegram.org/bot" + token + "/sendMessage", params = {"chat_id" : chat_id, "text" : answer})
    new_offset = message_id + 1
    result = get_bot_updates(100, new_offset)
