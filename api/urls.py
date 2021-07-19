from django.urls import path
from api import views
urlpatterns =[
    path('task-list/',views.task_list,name="task-list"),
    path('create-task/',views.create_task,name="create-task"),
    path('update-task/<int:pk>',views.update_task,name="update-task"),
    path('delete-task/<int:pk>',views.taskDelete,name="delete-task"),
]