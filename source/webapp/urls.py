from django.urls import path

from .views import index_view, create_record, delete_record

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create/', create_record, name='create_record'),
    # path('tasks/', tasks_view, name='tasks_view'),
    # path('task/<pk>', task_view, name='task_view'),
    # path('task/<pk>/update', update_task, name='update_task'),
    path('record/<pk>/delete', delete_record, name='delete_record'),


]