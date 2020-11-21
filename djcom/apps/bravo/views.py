from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'bravo/list - page.html')

	
def bravo_21(request):
    return render(request,'bravo/list - page.html')

def bravo_22(request):
    return HttpResponse("Страница товара Браво-22")	
