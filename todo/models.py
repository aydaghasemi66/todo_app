from django.db import models
from accounts.models import CustomeUser

class Task(models.Model):
    user = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
