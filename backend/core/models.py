from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Entry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='entries')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name} ({self.project.name})"


# # Create your models here.