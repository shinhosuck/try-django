from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
import random



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    # instance url for article detail
    def get_absolute_url(self):
        # url = reverse("article-detail", kwargs={"slug": self.slug})
        url = f"/article/{self.slug}"
        return url
    
    # def save(self, *args, **kwargs):
    #     # if not self.slug:
    #     #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

def create_unique_slug(instance, article=None, new_title=None):
    instance.slug = slugify(instance.title)
    articles = Article.objects.filter(slug = instance.slug)
    if articles:
        for article in articles:
            article.slug = f"{instance.slug}{random.randint(10000, 50000)}"
            article.save()
    return 


# WHEN AN AUTHOR  UPDATES THE ARTICLE TITLE
def update_title_and_slug(article, new_title, instance):
    if article.title != new_title:
        instance.slug = slugify(new_title)
        pre_save.disconnect(article_pre_save, sender=Article)
        instance.save()
        return update_slug(instance)
    return


def update_slug(instance):
    articles = Article.objects.filter(slug = instance.slug).exclude(id=instance.id)
    if articles:
        for article in articles:
            article.slug = f"{instance.slug}{random.randint(10000, 50000)}"
            article.save()
        return


@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, *args, **kwargs):
    article = Article.objects.filter(id=instance.id).first()
    new_title = instance.title

    if article and new_title:
        update_title_and_slug(article, new_title, instance)

    if not instance.slug:
        create_unique_slug(instance)


@receiver(post_save, sender=Article)
def article_post_save(sender, instance, created, *args, **kwargs):
    pass

