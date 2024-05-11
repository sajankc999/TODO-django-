from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title