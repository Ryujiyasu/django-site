from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import User_requestForm
from .models import User_request
from artist.models import Artist_group

@login_required
def index(request):
    if request.POST:
        form = User_requestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.artist_name=request.user
            post.save()
        return render(request,'user_request/thanks.html')
    else :
        form = User_requestForm()
    return render(request,'user_request/index.html',{'form': form})



@login_required
def check(request):
    role = Artist_group.objects.filter(user=request.user)[0]
    if str(role) == "admin":
        datas=User_request.objects.all()
        return render(request, 'user_request/check.html',{'datas':datas})
    return redirect('/')

