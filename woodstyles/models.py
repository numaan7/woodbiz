from django.utils import timezone
from django.db import models

# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Newsletter(models.Model):
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.email
    
class Wood(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='static/images')
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.title
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-date',)
    def __str__(self):
        return self.name
