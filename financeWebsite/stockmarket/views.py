from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader
import yfinance as yf


# import yfinance as yf
from yahoo_fin.stock_info import *
# from yahoofinance import BalanceSheet

def index(request):
    stockdata = get_income_statement("AAPL")
    indexNamesArr = list(stockdata.index.values)
    r = [0,1,2,3]
    context = {
        'stockdata' : stockdata,
        'indexNamesArr' : indexNamesArr,
        'testString' : 'aabhaas gupta',
        'val' : 'testAabhaas ',
        'a' : 'A',
        'b' : 'B',
        'f' : {'haha' : [2,3,4]}

    }
    return render(request, 'stockmarket/index.html', context)

# Create your views here.
