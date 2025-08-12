from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from . import models
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):  # renamed to avoid clash
    if request.method == "POST":
        username = request.POST.get("username")  # matches HTML
        password = request.POST.get("password")  # matches HTML
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # using Django's login
            return redirect('todolist')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            obj = models.TODOO(title=title, user=request.user)
            obj.save()
        return redirect('todolist')

    res = models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todolist.html', {'res': res})



@login_required
def edit_todo(request, srno):
    todo = get_object_or_404(models.TODOO, srno=srno, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
        return redirect('todolist')
    return render(request, 'edit.html', {'todo': todo})

@login_required
def delete_todo(request, srno):
    todo = get_object_or_404(models.TODOO, srno=srno, user=request.user)
    todo.delete()
    return redirect('todolist')


def signout(request):
    logout(request)
    return redirect('/login')