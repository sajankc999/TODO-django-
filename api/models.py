from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
