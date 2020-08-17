from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
import yfinance as yf
import json

# import yfinance as yf
from yahoo_fin.stock_info import *
# from yahoofinance import BalanceSheet

def index(request):
    stockdata = get_income_statement("AAPL")
    indexNamesArr = list(stockdata.index.values)
    jsonTestObj = stockdata.to_json()
    t = '{\"Product\":{\"0\":\"Desktop Computer\",\"1\":\"Tablet\",\"2\":\"iPhone\",\"3\":\"Laptop\"},\"Price\":{\"0\":700,\"1\":250,\"2\":800,\"3\":1200}}'
    a = {}
    a['test'] = t
    r = [0,1,2,3]
    x = 'testAabhaas '
    # print(stockdata.to_json())
    # print(type(stockdata.to_json()))
    context = {
        'stockdata' : stockdata,
        'indexNamesArr' : indexNamesArr,
        'testString' : 'aabhaas gupta',
        'val' : 'ho',
        'a' : 'A',
        'b' : 'B',
        'jsonTestObj' : jsonTestObj,

    }
    return render(request, 'stockmarket/index.html', context)

# Create your views here.
