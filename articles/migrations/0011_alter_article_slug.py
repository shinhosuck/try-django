# Generated by Django 3.2 on 2023-03-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
