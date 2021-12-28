from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskslist, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'), 
    path('changestatus/<int:id>', views.ChangeStatus, name='change-task'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('sobre/', views.sobre, name='sobre')
]
