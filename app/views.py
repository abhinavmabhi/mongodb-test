from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel

def index(request):
    items = MyModel.objects.all()
    return render(request, 'index.html', {'items': items})

def create_item(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    return render(request, 'create_item.html', {'form': form})