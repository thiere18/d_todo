from asyncio import Task
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,mixins
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
# @api_view(['GET'])
# def api_over_view(request):
#     return Response("hello world")

# @api_view(['GET'])
# def task_list(request):
#     tasks=Task.objects.all()
#     serializer=TaskSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def task_detail(request, pk: int):
#     tasks=Task.objects.get(id=(pk))
#     serializer=TaskSerializer(tasks, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def task_create(request):
#     serializer=TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['POST'])
# def task_update(request, pk: int):
#     task=Task.objects.get(id=(pk))
#     serializer=TaskSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['DELETE'])

# def task_delete(request, pk: int):
#     task=Task.objects.get(id=(pk))
#     task.delete()
#     return Response("Item deleted successfully")

        
# class  TodoCreate(generics.CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
class  TodoDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
todo_detail_view=TodoDetail.as_view()

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TodoDelete(generics.DeleteAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    

class TodoUpdateView(generics.UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field='pk'
    
class TodoDeleteView(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field='pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
class TodoMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
    ,):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field='pk'
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    pass