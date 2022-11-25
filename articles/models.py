from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # class Meta:
    #     ordering = ['-date_created']

    def __str__(self):
        return '{}'.format(self.title)