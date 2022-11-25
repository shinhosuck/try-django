from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    # def save(self, *args, **kwargs):

    #     return super().save(*args, **kwargs)
    
    

    class Meta:
        ordering = ['-date_created']

    def str_func(self):
        return 'hello world'

    def __str__(self):
        return '{}'.format(self.title)