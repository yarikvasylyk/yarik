from django.urls import path

from .views import topics, topic, create_topic

urlpatterns = [
    path('topics/', topics),
    path('create_topic/', create_topic),
    path('topic/<int:topic>', topic)
]