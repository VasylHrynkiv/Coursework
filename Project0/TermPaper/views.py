from django.shortcuts import render, redirect
from .models import Gen_info, Developer, Package
from .forms import DForm, PForm, GForm

def index(request):
    obj = Gen_info.objects.all()
    return render(request, 'TermPaper/home.html', {'obj': obj})

def dev(request):
    obj = Developer.objects.all()
    return render(request, 'TermPaper/dev.html', {'obj': obj})

def pack(request):
    obj = Package.objects.all()
    return render(request, 'TermPaper/pack.html', {'obj': obj})

def adddata(request):
    if request.method == "POST":
        form = GForm(request.POST)
        if form.is_valid:
            form.save() 
            return redirect('home')
    form = GForm
    return render(request, 'TermPaper/adddata.html', {'form': form})

def adddev(request):
    if request.method == "POST":
        form = DForm(request.POST)
        if form.is_valid:
            form.save() 
            return redirect('dev')
    form = DForm
    return render(request, 'TermPaper/adddev.html', {'form': form})

def addpack(request):
    if request.method == "POST":
        form = PForm(request.POST)
        if form.is_valid:
            form.save() 
            return redirect('pack')
    form = PForm
    return render(request, 'TermPaper/addpack.html', {'form': form})

def update(request, pk):
    obj = Gen_info.objects.get(pk=pk)
    form = GForm(instance=obj)
    if request.method == "POST":
        form = GForm(request.POST or None, instance=obj)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'TermPaper/update.html', {'obj': obj, 'form': form})

def delete(request, pk):
    obj = Gen_info.objects.get(pk=pk)
    obj.delete()
    return redirect('home')
    
def deldev(request, pk):
    obj = Developer.objects.get(pk=pk)
    obj.delete()
    return redirect('dev')

def delpack(request, pk):
    obj = Package.objects.get(pk=pk)
    obj.delete()
    return redirect('pack')

def search(request):
    if request.method == "POST":
        Search = request.POST['Search']
    obj = Gen_info.objects.filter(name__contains=Search)
    return render(request, 'TermPaper/home.html', {'obj':obj})