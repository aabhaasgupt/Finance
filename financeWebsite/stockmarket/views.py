from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render
from django.template import loader

def index(request):
    print("ii")
    # t = loader.get_template('stockmarket/index.html')
    # template = loader.get_template('/templates/stockmarket/index.html')
    #return HttpResponse(template.render(request))
    # return HttpResponse("<h1>hii</h1>")
    stockdata = "yoyo"
    r = [0,1,2,3]
    context = {
        'stockdata' : stockdata,
        'r' : r
    }
    return render(request, 'stockmarket/index.html', context)

# Create your views here.
