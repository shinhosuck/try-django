from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return '{}'.format(self.title)