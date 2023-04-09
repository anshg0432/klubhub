from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Club,Event,Highlight,Club_follow

def start(request):
    return render(request, 'clubs/start.html')


def home(request):
    x = Club_follow.objects.filter(user = request.user).all()
    arr = []
    for each in x:
        arr.append(Club.objects.filter(id = each.follow_id).first())
    context = {
        'clubs': arr
    
    }
    
        
    return render(request, 'clubs/home.html',context)


def clubs(request):
    
    if request.method == "POST":
        it = Club_follow()
        it.user = request.user
        it.follow_id = int(request.POST['title'])
        it.save()
        return redirect('../../home')
    context_2 = {
        'events': Event.objects.all(),
        'highlights': Highlight.objects.all(),
        'club_follow': Club_follow.objects.all()
    }
    return render(request, 'clubs/my_clubs.html',context_2)


def explore(request):
    context_3 = {
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs/explore.html',context_3)

def clubs_d(request):
    
    if request.method == "POST":
        it = Club_follow()
        it.user = request.user
        it.follow_id = int(request.POST['title'])
        it.save()
        return redirect('../../home')
    context_2 = {
        'events': Event.objects.all(),
        'highlights': Highlight.objects.all(),
        'club_follow': Club_follow.objects.all()
    }
    return render(request, 'clubs/dsc_club.html',context_2)