from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Todo

def index (request):
    todos = Todo.objects.order_by('-id') 
    return render(request, 'index.html', {'todos': todos, 'length': len(todos)})

def add (request):

    name = request.POST.get('todo-add')
    if (name == ''):
        return HttpResponseRedirect(reverse('todo:index'))

    todo = Todo(name=name)
    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))

def update (request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    
    if (todo.done):
        todo.done = False
    else:
        todo.done = True
    
    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))

def delete (request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))

