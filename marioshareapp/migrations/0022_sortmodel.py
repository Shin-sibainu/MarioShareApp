# Generated by Django 3.2 on 2021-05-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0021_mariosharemodel_coursecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SortModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
