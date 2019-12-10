from django.urls import path

from .views import topics, topic

urlpatterns = [
    path('topics/', topics),
    path('topic/<int:topic>', topic)
]