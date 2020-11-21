from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'porta_z/list.html')
	
def porta_x(request):
    return HttpResponse("Страница подкатегории экошпон порта-х")
	
def ekoshpon(request):
    return HttpResponse("Страница подкатегории экошпон ekoshpon порта-х")
	
def porta_z(request):
    return HttpResponse("Страница подкатегории экошпон порта-z1")
	
def test(request):
    return render('base.html')	
	
