from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:todo_id>/update", views.update, name="update"),
    path("<int:todo_id>/delete", views.delete, name="delete"),
]