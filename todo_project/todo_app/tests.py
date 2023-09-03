from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TodoItem

class TodoItemTests(APITestCase):

    def setUp(self):
        TodoItem.objects.create(description='Task 1')
        TodoItem.objects.create(description='Task 2', completed=True)

    def test_list_todo_items(self):
        url = reverse('todo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_todo_item(self):
        url = reverse('todo-list')
        data = {'description': 'New Task'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.count(), 3)

    def test_retrieve_todo_item(self):
        item = TodoItem.objects.get(description='Task 1')
        url = reverse('todo-detail', args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Task 1')

    def test_update_todo_item(self):
        item = TodoItem.objects.get(description='Task 2')
        url = reverse('todo-detail', args=[item.id])
        data = {'completed': False}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['completed'], False)

    def test_invalid_update(self):
        item = TodoItem.objects.get(description='Task 1')
        url = reverse('todo-detail', args=[item.id])
        data = {'completed': 'invalid_value'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

