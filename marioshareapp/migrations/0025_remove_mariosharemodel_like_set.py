# Generated by Django 3.2 on 2021-05-12 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0024_mariosharemodel_like_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mariosharemodel',
            name='like_set',
        ),
    ]
