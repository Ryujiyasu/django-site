
from django.shortcuts import render
import csv
from io import TextIOWrapper
from sale.models import Sale,Mt_Service,Mt_aritstname
import datetime
from django.contrib.auth.decorators import login_required
from artist.models import Artist_group
from django.shortcuts import redirect

@login_required
def music(request):
    role= Artist_group.objects.filter(user=request.user)[0]
    if str(role)=="admin":
        if 'csv' in request.FILES:
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            csv_file = csv.reader(form_data)
            i=0
            for line in csv_file:
                if i==0:
                    i=i+1
                    continue
                sale = Sale()
                sale.artist_name = line[6]
                mt_artistname=Mt_aritstname()
                sale.user=mt_artistname.objets.filter(artist_name=line[6])
                sale.item = line[5]
                sale.count = int(line[18])
                tax=line[32]
                pre_price = float(line[25])
                if tax=='非課税':
                    post_price = pre_price
                else:
                    post_price = pre_price * 1.08
                sale.pricesum=post_price
                sale.price=artistsell.pricesum/artistsell.count
                service=Mt_Service()
                sale.service_type=service.objects.objects.get_or_create(service_type='music')
                date=line[2][0:4]+"-"+line[2][5:7]+"-"+line[2][8:]
                sale.date=date
                sale.importdate=datetime.date.today()
                sale.save()
            return render(request, 'importcsv/upload_music.html')
        else:
            return render(request, 'importcsv/upload_music.html')
    return redirect('/')



@login_required
def goods(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        i=0
        for line in csv_file:
            if i==0:
                i=i+1
                continue
            sale = Sale()
            item_and_artist=line[18]
            item_and_artist_split=item_and_artist.split("/")
            sale.artist_name = item_and_artist_split[1]
            mt_artistname=Mt_aritstname()
            sale.user=mt_artistname.objets.filter(artist_name=item_and_artist_split[1])
            sale.item = item_and_artist_split[0]
            sale.count = int(line[21])
            sale.pricesum=float(line[22])
            sale.price=float(line[20])
            service=Mt_Service()
            sale.service_type=service.objects.objects.get_or_create(service_type='goods')
            date_time=line[1]
            date=date_time.split(' ')
            year_month_day=date[0].split('/')
            year=year_month_day[0]
            month=year_month_day[1]
            day=year_month_day[2]
            YearMonthDay=year+"-"+month+"-"+day
            sale.date=YearMonthDay
            sale.importdate=datetime.date.today()
            sale.save()
        return render(request, 'importcsv/upload_goods.html')
    else:
        return render(request, 'importcsv/upload_goods.html')
@login_required
def app(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        i=0
        for line in csv_file:
            if i==0:
                i=i+1
                continue
            sale = Sale()
            sale.artist_name = line[0]
            mt_artistname=Mt_aritstname()
            sale.user=mt_artistname.objets.filter(artist_name=line[0])
            sale.item = line[1]
            sale.count = 1
            sale.pricesum=float(line[6])
            sale.price=float(line[6])
            service=Mt_Service()
            sale.service_type=service.objects.get_or_create(service_type='app')
            date=line[12]
            year_month_day=date.split('/')
            year=year_month_day[0]
            month=year_month_day[1]
            day=year_month_day[2]
            YearMonthDay=year+"-"+month+"-"+day
            sale.date=YearMonthDay
            sale.importdate=datetime.date.today()
            sale.save()
        return render(request, 'importcsv/upload_app.html')
    else:
        return render(request, 'importcsv/upload_app.html')
@login_required
def cd(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        i=0
        for line in csv_file:
            if i==0:
                i=i+1
                continue
            sale = Sale()
            sale.artist_name = line[10]
            mt_artistname=Mt_aritstname()
            sale.user=mt_artistname.objets.filter(artist_name=line[10])
            sale.item = line[9]
            sale.count = int(line[6])
            sale.pricesum=float(line[7])
            sale.price=artistsell.pricesum/artistsell.count
            service=Mt_Service()
            sale.service_type=service.objects.get_or_create(service_type='cd')
            date=line[0]
            year=date[0:4]
            month=date[4:]
            day='01'
            YearMonthDay=year+"-"+month+"-"+day
            sale.date=YearMonthDay
            sale.importdate=datetime.date.today()
            sale.save()
        return render(request, 'importcsv/upload_cd.html')
    else:
        return render(request, 'importcsv/upload_cd.html')
