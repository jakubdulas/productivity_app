from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task, Category, Event
from .serializers import TaskSerializer, CategorySerializer, EventSerializer
# Create your views here.

# Authentication

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    print(request.user)
    return Response({'text': 'Hello world!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(user=request.user).all()
    serialied_tasks = TaskSerializer(tasks, many=True)

    data  = {
        "tasks": serialied_tasks.data
    }

    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.filter(user=request.user).all()
    serializer = CategorySerializer(categories, many=True)
    data  = serializer.data
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_events(request):
    events = Event.objects.filter(user=request.user).all()
    serialized_events = EventSerializer(events, many=True)
    data = {
        "events": serialized_events.data
    }
    return Response(data)
