from django.urls import path

# local imports
from todos.views import TodoListCreateAPIView, TodoDetailsAPIView

urlpatterns = [
    path("", TodoListCreateAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailsAPIView.as_view(), name="todo-details")
    
]
