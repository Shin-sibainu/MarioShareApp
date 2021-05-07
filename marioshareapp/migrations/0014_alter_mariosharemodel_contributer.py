# Generated by Django 3.2 on 2021-05-05 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marioshareapp', '0013_alter_mariosharemodel_contributer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mariosharemodel',
            name='contributer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
