from django.urls import path

from .views import index_view, create_record, delete_record, update_record

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create/', create_record, name='create_record'),
    path('record/<pk>/update', update_record, name='update_record'),
    path('record/<pk>/delete', delete_record, name='delete_record'),


]