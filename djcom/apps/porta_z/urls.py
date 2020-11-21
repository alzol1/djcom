
from django.urls import path

from . import views

urlpatterns = [path('porta_z/', views.porta_z, name = 'porta_z'),
    path('', views.index, name = 'index'), 
	path('test', views.test, name = 'base'),
]
