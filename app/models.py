from django.db import models

# Create your models here.
class Profile(models.Model):
    slackUsername = models.CharField(max_length=250, null=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(null=True)
    backend = models.BooleanField(null=True, default=True)