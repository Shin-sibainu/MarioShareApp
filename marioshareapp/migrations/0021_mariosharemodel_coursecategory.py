# Generated by Django 3.2 on 2021-05-08 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marioshareapp', '0020_auto_20210508_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='mariosharemodel',
            name='coursecategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='marioshareapp.coursecategory'),
            preserve_default=False,
        ),
    ]
