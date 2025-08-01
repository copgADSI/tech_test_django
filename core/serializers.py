from rest_framework import serializers
from .models import User, Entry
from django.utils import timezone
from datetime import timedelta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'created_at', 'updated_at']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'user', 'entry_time', 'exit_time', 'created_at', 'updated_at']
        read_only_fields = ['entry_time', 'exit_time']

    def create(self, validated_data):
        now = timezone.now()
        validated_data['entry_time'] = now
        validated_data['exit_time'] = now + timedelta(hours=5)
        return super().create(validated_data)
