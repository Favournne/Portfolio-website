from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length = 50)
    email=models.CharField(max_length = 50)
    contact=models.CharField(max_length = 100)

    def __str__(self):
        return self.name  
    


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name  

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




