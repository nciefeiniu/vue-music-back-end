# Generated by Django 3.0.4 on 2020-03-24 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200324_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylovemusic',
            name='music_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music'),
        ),
    ]