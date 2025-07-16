from django.shortcuts import render, redirect, get_object_or_404
from .models import Bb
from .forms import BbForm

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

def create(request):
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BbForm()
    return render(request, 'bboard/create.html', {'form': form})

def detail(request, slug):
    bb = get_object_or_404(Bb, slug=slug)
    return render(request, 'bboard/detail.html', {'bb': bb})