from rest_framework import viewsets, generics
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = []

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Rohit')
        serializer.save(created_by=user)

    def perform_update(self, serializer):
        serializer.save()

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Ganesh')
        return Project.objects.filter(users=user)

class ClientProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = []

    def perform_create(self, serializer):
        client_id = self.kwargs['client_id']
        client = Client.objects.get(id=client_id)
        user = self.request.user if self.request.user.is_authenticated else User.objects.get(username='Ganesh')
        serializer.save(client=client, created_by=user)
