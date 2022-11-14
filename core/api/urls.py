from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-tasks', views.get_tasks, name='all_tasks'),
    path('get-categories', views.get_categories, name='get_categories'),
    path('get-events', views.get_events, name='get_events'),
]
