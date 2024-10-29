from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    subtitle = models.CharField(max_length = 100, blank= True)
    author = models.CharField(max_length= 100, blank=True)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)