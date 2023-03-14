from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoListItem

def view_todo(request):
    all_todo_items = ToDoListItem.objects.all()
    return(render(request, 'todolist.html', {'all_items': all_todo_items}))

def addToDoView(request):
    content = request.POST['content']
    new_item = ToDoListItem(content=content)
    new_item.save()
    return HttpResponseRedirect('/')

def deleteToDoView(request, item):
    delete_item = ToDoListItem.objects.get(id=item)
    delete_item.delete()
    return HttpResponseRedirect('/')
