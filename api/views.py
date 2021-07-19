from django.shortcuts import render
from api import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskSerializer
from api.models import Task

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def create_task(request):
    serializers = TaskSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['PUT'])
def update_task(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializer(instance=task,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")

