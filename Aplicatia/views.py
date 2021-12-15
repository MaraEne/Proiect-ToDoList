from django.shortcuts import render, redirect
from .forms import *

def index (request):
    Aplicatia = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'Aplicatia':Aplicatia, 'form':form}
    return render(request, 'Aplicatia/lista.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'Aplicatia/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context={'item': item}
    return render(request, 'Aplicatia/delete.html', context)
