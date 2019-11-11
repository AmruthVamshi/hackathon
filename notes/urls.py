from django.contrib import admin
from django.urls import path
from . import views
app_name='notes'
urlpatterns = [
    path('',views.home,name='home'),
    path('save',views.formsave,name='save'),
    path('delete/<int:post_pk>',views.delete,name='delete'),
]
