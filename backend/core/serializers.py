# your_app/serializers.py

from rest_framework import serializers
from .models import Project, Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True, read_only=True)  # if using ManyToMany or ForeignKey

    class Meta:
        model = Project
        fields = '__all__'
