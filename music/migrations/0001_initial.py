# Generated by Django 3.0.4 on 2020-03-14 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ntes_id', models.CharField(blank=True, max_length=255, null=True)),
                ('music_name', models.CharField(max_length=255)),
                ('music_auth', models.CharField(max_length=255)),
                ('music_url', models.URLField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('music_name', 'music_auth')},
            },
        ),
        migrations.CreateModel(
            name='RadioStation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('radio_name', models.CharField(max_length=255)),
                ('radio_classification', models.CharField(choices=[('Casual', '随心听'), ('Classic', '经典'), ('Popular', '流行'), ('Blue', '忧伤'), ('Cantonese', '粤语'), ('Calm', '平静'), ('GetUP', '起床'), ('LoveSong', '情歌')], default='Casual', max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('radio_name', 'radio_classification')},
            },
        ),
        migrations.CreateModel(
            name='SongSheet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sheet_name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('sheet_name', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='SongSheetMusic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music')),
                ('song_sheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.SongSheet')),
            ],
            options={
                'unique_together': {('song_sheet_id', 'music_id')},
            },
        ),
        migrations.CreateModel(
            name='RadioStationMusic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music')),
                ('radio_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.RadioStation')),
            ],
            options={
                'unique_together': {('radio_station_id', 'music_id')},
            },
        ),
        migrations.CreateModel(
            name='MyLoveMusic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'music_id')},
            },
        ),
    ]
