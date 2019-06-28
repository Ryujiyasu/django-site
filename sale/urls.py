from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list/',views.sale,name='sale_list'),
    path('<int:year>/',views.year_sale),
    path('<int:year>/<int:month>/',views.month_sale)
    ]