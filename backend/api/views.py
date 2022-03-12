from asyncio import Task
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
@api_view(['GET'])
def api_over_view(request):
    return Response("hello world")

@api_view(['GET'])
def task_list(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk: int):
    tasks=Task.objects.get(id=(pk))
    serializer=TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk: int):
    task=Task.objects.get(id=(pk))
    serializer=TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])

def task_delete(request, pk: int):
    task=Task.objects.get(id=(pk))
    task.delete()
    return Response("Item deleted successfully")

        
        
