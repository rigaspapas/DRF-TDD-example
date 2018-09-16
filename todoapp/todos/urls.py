from django.conf.urls import url
from todos.views import TodoListCreateAPIView, TodoDetailAPIView

app_name = "todos"

urlpatterns = [
    url(r"^$", TodoListCreateAPIView.as_view(), name="list"),
    url(r"^(?P<pk>[0-9]+)/$", TodoDetailAPIView.as_view(), name="detail"),
]
