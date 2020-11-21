
from django.urls import path, include

from . import views

urlpatterns = [path('mezhkomnatnye/', include('mezhkomnatnye_dveri_bravo.urls')),
    path('', views.index, name = 'dveri-bravo'),
]
