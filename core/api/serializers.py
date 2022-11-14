from .models import Category, Event, Task
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email = self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords must match.'})

        account.set_password(password)
        account.save()
        return account

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'username': instance.user.username,
            'name': instance.name,
            'deadline': instance.deadline,
            'category': instance.category.values(),
            'completed': instance.completed,
            "id": instance.id
        }

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'name': instance.name,
            'date': instance.date,
            'category': instance.category.values(),
            'id': instance.id
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude=['user']