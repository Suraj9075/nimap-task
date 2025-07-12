from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    users = UserSimpleSerializer(many=True, read_only=True)
    user_ids = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, many=True)
    client = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'created_by', 'created_at', 'users', 'user_ids']

    def create(self, validated_data):
        users = validated_data.pop('user_ids')
        project = Project.objects.create(**validated_data)
        project.users.set(users)
        return project
