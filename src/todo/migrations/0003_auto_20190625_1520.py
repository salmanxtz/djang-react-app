# Generated by Django 2.2.2 on 2019-06-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190625_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
