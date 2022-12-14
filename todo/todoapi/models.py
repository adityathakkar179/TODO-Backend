from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title