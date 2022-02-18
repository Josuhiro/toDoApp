from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import *


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def assignUser(model, request):
    obj = model.objects.latest('pk')
    obj.user = request.user
    obj.save()

@login_required(login_url='login')
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
    if not get_referer(request):
        raise Http404
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/edit.html', context)


def delete(request, pk):
    if not get_referer(request):
        raise Http404
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
