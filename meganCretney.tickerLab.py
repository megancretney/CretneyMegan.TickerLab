# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:54:15 2022

@author: cretn
"""

#### Ticker Lab ######
myKey = "<<Enter your personal key here>>"
import json
import requests

## Get tickers
ticker = input("Enter your value: ")

commas = ticker.count(",")+1

## Get the info from API stuff
try:
    url = "https://yfapi.net/v6/finance/quote"

    querystring = {"symbols":ticker}

    headers = {
    'x-api-key': myKey
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    ## print(response.text)

## Print out answer
    stock_json = response.json()
    for i in range(commas):
        print(stock_json['quoteResponse']['result'][i]['longName'], stock_json['quoteResponse']['result'][i]['regularMarketPrice'])


except:
    print("PLease enter valid Ticker")