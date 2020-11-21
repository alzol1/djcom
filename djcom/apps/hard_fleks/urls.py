
from django.urls import path, include

from . import views

urlpatterns = [path('bravo/', include('bravo.urls')),
    path('', views.index, name = 'index'),
]
