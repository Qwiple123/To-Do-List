from django.contrib import admin
from django.urls import path
from todoapp.views import view_todo, addToDoView, deleteToDoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_todo, name='todolist'),
    path('addToDoItem/', addToDoView, name='add_item'),
    path('deleteTodoItem/<int:item>/', deleteToDoView, name='delete_item')
]
