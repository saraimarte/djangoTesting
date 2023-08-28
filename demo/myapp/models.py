from django.db import models

# Create your models here.
#TodoItem(s) represents a database table
#CRUD Create Retrieve Update Delete 
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length = 20)

    def __str__(self):
        return self.name