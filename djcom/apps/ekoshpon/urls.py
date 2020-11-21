
from django.urls import path, include

from . import views

app_name = 'ekoshpon'
urlpatterns = [path('ekoshpon/', include('porta_z.urls')),
    path('', views.index, name = 'index'),
	path('porta-x/', views.porta_x, name = 'porta_x'),
]
