
from django.urls import path

from . import views

app_name = 'porta_x'
urlpatterns = [
    path('porta-x/', views.index, name = 'porta-x'),
	
]
