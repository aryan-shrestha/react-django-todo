from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list_create': '/task',
        'retrieve_update_delete': 'task-detail/<str:pk>',
    }
    return Response(api_urls)

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
