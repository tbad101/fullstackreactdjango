We would like you to create a basic Django application to host a Todo-list API. The requirements are:

1. Each todo item should store:
   1. A description
   2. A 'completed' flag
   3. A created timestamp
   4. An update timestamp

2. Implement the "List", "Read", "Create" and "Update" APIs using REST practices (preferably using Django-Rest-Framework)

3. Store the results in a SQLite Database



1.Create a new Django project and navigate to its root directory:

django-admin startproject todo_project
cd todo_project

2.Create a new Django app for the Todo-list API:

python manage.py startapp todo_app

3.In your todo_app directory, create a model for the Todo item in models.py:

from django.db import models

class TodoItem(models.Model):
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

4.Create serializers in serializers.py to convert the model instances to JSON and vice versa:

from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'







5.Create views in views.py to handle the API endpoints:

from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemDetail(generics.RetrieveUpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

6.Create URLs in urls.py for the API endpoints:

from django.urls import path
from .views import TodoItemList, TodoItemDetail

urlpatterns = [
    path('todos/', TodoItemList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoItemDetail.as_view(), name='todo-detail'),
]

7.Add your app's URLs to the project's urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
]

8.Run migrations and create the SQLite database:

python manage.py makemigrations
python manage.py migrate

9.Create a superuser to access the admin panel:

python manage.py createsuperuser

10.Run the development server:

python manage.py runserver
