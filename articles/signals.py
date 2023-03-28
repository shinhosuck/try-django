from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from articles.models import Article
import random


def create_unique_slug(instance, article=None, new_title=None):
    instance.slug = slugify(instance.title)
    articles = Article.objects.filter(slug = instance.slug)
    print("SLUG ADDED")
    if articles:
        for article in articles:
            article.slug = f"{instance.slug}{random.randint(10000, 50000)}"
            article.save()
    return 


def update_title_and_slug(article, new_title, instance):
    print("UPDATE TITLE AND SLUG")
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


# THIS GETS TRIGERED WHEN AN ARTICLE WITHOUT A SLUG IS BEING UPDATED AND WHEN A NEW ARTICLE IS CREATED.
@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, *args, **kwargs):
    print("PRE_POST")
    article = sender.objects.filter(id=instance.id).first()
    print("article:", article)
    new_title = instance.title

    if article and new_title:
         print("ARTICLE AND TITLE")
         update_title_and_slug(article, new_title, instance)

    if instance.slug == None:
        print("NEW ARTICLE")
        create_unique_slug(instance)

# THIS GETS TRIGERED ONLY WHEN A NEW ARTICLE IS CREATED.
# @receiver(post_save, sender=Article)

# def article_post_save(sender, instance, created, *args, **kwargs):
#     print("POST_SAVE1")
#     if created:
#         print("CREATED")
#         create_unique_slug(instance)
# post_save.connect(article_post_save, sender=Article)