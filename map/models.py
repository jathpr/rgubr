from django.db import models
from django.utils import timezone


class Mark(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    begin_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title
