from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemDetail(generics.RetrieveUpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

# Create your views here.
