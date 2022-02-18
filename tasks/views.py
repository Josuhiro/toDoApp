from django.shortcuts import render, redirect
from .forms import *


def assignUser(model, request):
    obj = model.objects.latest('pk')
    obj.user = request.user
    obj.save()


def index(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            assignUser(Task, request)
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/tasks.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/edit.html', context)
