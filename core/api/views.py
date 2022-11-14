from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, Category, Event
from .serializers import TaskSerializer, CategorySerializer, EventSerializer
# Create your views here.

# Authentication

@api_view(['POST'])
def home(request):
    print(request.user)
    return Response({'text': 'Hello world!'})

@api_view()
def get_tasks(request):
    tasks = Task.objects.all()
    serialied_tasks = TaskSerializer(tasks, many=True)

    data  = {
        "tasks": serialied_tasks.data
    }

    return Response(data)

@api_view()
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    data  = serializer.data
    return Response(data)

@api_view()
def get_events(request):
    events = Event.objects.all()
    serialized_events = EventSerializer(events, many=True)
    data = {
        "events": serialized_events.data
    }
    return Response(data)

# {
#  "events": 
#  [
#   {
#     "id": 1,
#     "name": "urodziny przemka",
#     "category": "school",
#     "date": "01.01.2001",
#   },
#   {
#     "id": 2,
#     "name": "imieniny zbyszka",
#     "category": "home",
#     "date": "05.01.2001",
#   },
#  ]
# }