from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Bb
from .forms import BbForm, CustomUserCreationForm

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

def create(request):
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES)
        if form.is_valid():
            bb = form.save(commit=False)
            bb.user = request.user  # Привязываем объявление к пользователю
            bb.save()
            return redirect('index')
    else:
        form = BbForm()
    return render(request, 'bboard/create.html', {'form': form})

def detail(request, slug):
    bb = get_object_or_404(Bb, slug=slug)
    return render(request, 'bboard/detail.html', {'bb': bb})

def delete(request, slug):
    bb = get_object_or_404(Bb, slug=slug)
    if request.method == 'POST':
        bb.delete()
        return redirect('index')
    return render(request, 'bboard/delete.html', {'bb': bb})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'bboard/register.html', {'form': form})