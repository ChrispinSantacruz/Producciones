# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Content, Rating
from .serializers import ContentSerializer, RatingSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Content
from django.views.decorators.csrf import csrf_exempt
import json

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'list': [IsAuthenticated],
                                    'retrieve': [IsAuthenticated]}

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action.get(self.action, [IsAuthenticated])]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

class ContentCreateView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
def create_content(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Procesa los datos recibidos y crea el contenido
        title = data.get('title')
        type = data.get('type')
        poster_url = data.get('poster_url')
        trailer_url = data.get('trailer_url')
        duration_minutes = data.get('duration_minutes')
        num_episodes = data.get('num_episodes')

        # Crea el objeto Content en la base de datos
        content = Content.objects.create(
            title=title,
            type=type,
            poster_url=poster_url,
            trailer_url=trailer_url,
            duration_minutes=duration_minutes,
            num_episodes=num_episodes
        )

        return JsonResponse({'message': 'Content created successfully', 'id': content.id})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})