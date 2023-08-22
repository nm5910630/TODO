from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TODO
from .serializers import TodoSerializer

@api_view(['GET'])
def get_todos(request):
    todos = TODO.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def toggle_todo_status(request, todo_id):
    try:
        todo = TODO.objects.get(pk=todo_id)
    except TODO.DoesNotExist:
        return Response(status=404)

    if todo.status == 'C':
        todo.status = 'P'
    else:
        todo.status = 'C'
    todo.save()
    serializer = TodoSerializer(todo)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo(request, todo_id):
    try:
        todo = TODO.objects.get(pk=todo_id)
    except TODO.DoesNotExist:
        return Response(status=404)

    todo.delete()
    return Response(status=204)
