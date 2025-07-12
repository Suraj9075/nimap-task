from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, ClientProjectCreateView

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_id>/projects/', ClientProjectCreateView.as_view(), name='client-projects'),
]



