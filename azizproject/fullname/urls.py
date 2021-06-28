from django.contrib import admin
from django.urls import path
from .views import index,create,delete, update,detail


urlpatterns = [
    path('',index, name = 'index'),
    path('create/', create, name='create'),
    path('detete/<int:id>/', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
    path('detail/','<int:id>/',detail, name='detail'),
    
]