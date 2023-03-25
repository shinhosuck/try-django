from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def instance_title_to_slug(instance, save=False):
    slug = slugify(instance.title)
    instance.slug = slug
    if save:
        instance.save()

def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance_title_to_slug(instance, save=False)
        
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance_title_to_slug(instance, save=True)

post_save.connect(article_post_save, sender=Article)