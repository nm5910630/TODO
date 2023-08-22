
from django.contrib import admin
from django.urls import path
from app.views import *

from .api import *

urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
   
   
   ################### API ######################################
   
   path('todos/', get_todos, name='get_todos'),
   path('todos/create/', create_todo, name='create_todo'),
   path('todos/toggle/<int:todo_id>/', toggle_todo_status, name='toggle_todo_status'),
   path('todos/delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]
