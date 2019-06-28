from django.urls import path
from . import views

urlpatterns = [
    path('music/',views.music,name='music'),
    path('goods/',views.goods,name='goods'),
    path('app/',views.app,name='app'),
    path('cd/',views.cd,name='cd'),
]
