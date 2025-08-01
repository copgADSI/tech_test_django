from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import User, Entry
from .serializers import UserSerializer, EntrySerializer

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({'error': 'Email already registered'}, status=400)
            user = serializer.save()
            return Response(UserSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'message': 'User deleted'}, status=204)

class EntryViewSet(viewsets.ViewSet):
    def create(self, request):
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        serializer = EntrySerializer(data={'user': user.id})
        if serializer.is_valid():
            entry = serializer.save()
            return Response(EntrySerializer(entry).data, status=201)
        return Response(serializer.errors, status=400)
