from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import TaskForm

# List tasks + add new task
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'mini/helo.html', {'tasks': tasks, 'form': form})

# Edit task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'mini/edit.html', {'form': form})

# Delete task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
