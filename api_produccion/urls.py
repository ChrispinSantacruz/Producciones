# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, RatingViewSet
from .views import ContentCreateView
from .views import ContentViewSet, RatingViewSet, ContentCreateView, create_content
router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    # Rutas para los viewsets
    path('', include(router.urls)),
    
    # Ruta para la vista basada en clase ContentCreateView
    path('contents/create/', ContentCreateView.as_view(), name='content-create'),
    
    # Ruta para la función create_content
    path('api/contents/create/', create_content, name='create_content'),
    path('contents/', create_content, name='create_content'),
]
