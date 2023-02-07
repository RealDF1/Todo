import datetime
from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)