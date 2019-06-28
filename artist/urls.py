from django.urls import path

from . import views


app_name = 'artist'

urlpatterns = [
    path('home',views.index,name="index")

]