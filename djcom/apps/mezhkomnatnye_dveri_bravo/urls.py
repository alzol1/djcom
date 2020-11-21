from django.urls import path, include

from . import views

app_name = 'mezhkomnatnye_dveri_bravo'

urlpatterns = [path('', views.index, name = 'mezhkomnatnye'),
    path('ekoshpon/', include('ekoshpon.urls'), name = 'ekoshpon'),
    path('hard-fleks/', include('hard_fleks.urls')),
    
    
	path('ekoshpon/', views.index, name = 'index/ekoshpon/'),
]
