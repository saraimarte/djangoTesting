from django.db import models

# Create your models here.

class TodoItem(models.ModeL):
    title = models.CharField(max_Length = 200)
    completed = models.BooleanField(defualt = False)