
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
	path('bravo-21.html', views.bravo_21, name = 'bravo-21'),
	path('bravo-22.html', views.bravo_22, name = 'bravo-22'),
]
