# Generated by Django 5.0.4 on 2024-06-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0002_alter_post_rating_pos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rating_pos',
        ),
        migrations.AddField(
            model_name='post',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
