# Generated by Django 3.0.4 on 2020-03-24 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiostation',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radiostation',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='radiostation',
            name='radio_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='songsheet',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='songsheet',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='songsheet',
            name='song_sheet_desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mylovemusic',
            name='music_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music', unique=True),
        ),
    ]
