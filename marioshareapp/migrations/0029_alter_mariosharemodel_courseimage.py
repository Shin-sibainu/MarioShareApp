# Generated by Django 3.2 on 2021-05-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0028_auto_20210512_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mariosharemodel',
            name='courseimage',
            field=models.ImageField(blank=True, default='../media/public_thumbnail.png', null=True, upload_to=''),
        ),
    ]