from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Entry
from .serializers import ProjectSerializer, EntrySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        entry = serializer.save()
        project_id = self.request.data.get('project')
        if project_id:
            try:
                project = Project.objects.get(id=project_id)
                project.entries.add(entry)
            except Project.DoesNotExist:
                pass  # handle error if needed


# Create your views here.
