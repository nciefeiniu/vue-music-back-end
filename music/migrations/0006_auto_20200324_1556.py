# Generated by Django 3.0.4 on 2020-03-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200324_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimages',
            name='file',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]
