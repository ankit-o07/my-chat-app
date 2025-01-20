from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Message
from django.db import models

@login_required
def home(request):
    users = User.objects.exclude(username=request.user.username)
    context={
        "users":users
    }
    return render(request,'chat/home.html',context)


def login(request):
    context={
        "name":"login"
    }
    return render(request,'chat/login.html',context)

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'chat/signup.html', {'form': form})



@login_required
def chat_room(request, username):
    other_user = get_object_or_404(User, username=username)
    room_name = '_'.join(sorted([request.user.username, other_user.username]))
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=other_user)) |
        (models.Q(sender=other_user) & models.Q(receiver=request.user))
    ).order_by('timestamp')

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'messages': messages,
        'other_user': other_user,
    })
    

def logout(request):
    context={
        "name":"logout"
    }

    return render(request,'chat/signup.html',context)





