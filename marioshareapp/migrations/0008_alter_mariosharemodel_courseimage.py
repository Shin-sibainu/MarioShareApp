# Generated by Django 3.2 on 2021-05-01 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0007_alter_mariosharemodel_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mariosharemodel',
            name='courseimage',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
