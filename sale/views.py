from django.shortcuts import render
from .models import Sale
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'sale/index.html')

@login_required
def sale(request):
    login_user = request.user
    object_list=Sale.objects.filter(user=login_user)
    price_sum=0

    for i in object_list:
        price_sum+=i.pricesum
    context={
        'object_list':object_list,
        'price_sum': price_sum
    }
    return render(request,'sale/list.html',context=context)

@login_required
def year_sale(request,year):
    login_user = request.user
    object_list=Sale.objects.filter(user=login_user,date__year=year)
    price_sum=0
    for i in object_list:
        price_sum+=i.pricesum
    context={
        'object_list':object_list,
        'price_sum': price_sum
    }
    return render(request,'sale/list.html',context=context)

@login_required
def month_sale(request,year,month):
    login_user = request.user
    object_list=Sale.objects.filter(user=login_user,date__year=year,date__month=month)
    price_sum=0
    for i in object_list:
        price_sum+=i.pricesum
    context={
        'object_list':object_list,
        'price_sum': price_sum
    }
    return render(request,'sale/list.html',context=context)