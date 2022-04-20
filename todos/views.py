from django.shortcuts import render

#third-party imports
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# local imports
from todos.serializers import TodoSerializer
from todos.models import Todo
from todos.pagination import CustomPageNumberPagination

class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete']
    search_fields = ['title']
    ordering_fields = ['id', 'title']


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)


class TodoDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)