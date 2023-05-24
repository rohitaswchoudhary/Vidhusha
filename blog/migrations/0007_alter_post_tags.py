# Generated by Django 4.2.1 on 2023-05-23 08:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='Enter your post tags...', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
