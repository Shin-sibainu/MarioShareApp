# Generated by Django 3.2 on 2021-05-12 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0025_remove_mariosharemodel_like_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='mariosharemodel',
            name='like_set',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
