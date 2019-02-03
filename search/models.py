from django.conf import settings
from django.db import models
from django.utils import timezone

class SearchResult(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    where = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
