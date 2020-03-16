from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Music(models.Model):
    # 歌曲
    id = models.BigAutoField(primary_key=True)
    ntes_id = models.CharField(max_length=255, blank=True, null=True)  # 网易云音乐ID
    music_name = models.CharField(max_length=255, blank=False, null=False)  # 歌曲名字
    music_auth = models.CharField(max_length=255)  # 歌曲作者
    music_url = models.URLField()  # 歌曲的URL路径，网易云的不能存这个URL(这个URL有失效时间)，自己上传的才存URL
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('music_name', 'music_auth')


class MyLoveMusic(models.Model):
    # 我喜欢的歌
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # 用户的ID
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE)  # 歌曲的ID
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user_id", "music_id")


class SongSheet(models.Model):
    # 自建歌单目录
    id = models.BigAutoField(primary_key=True)
    sheet_name = models.CharField(max_length=255, blank=False, null=False)  # 自建歌单名字
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # 用户的ID
    img_url = models.URLField(blank=True, null=True)  # 歌单封面
    song_sheet_desc = models.TextField(default='')  # 歌单描述
    is_public = models.BooleanField(default=False)  # 歌单是否公开
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("sheet_name", "user_id")


class SongSheetMusic(models.Model):
    # 自建歌单中的歌曲
    id = models.BigAutoField(primary_key=True)
    song_sheet_id = models.ForeignKey(SongSheet, on_delete=models.CASCADE)  # 自建歌单 ID
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE)  # 歌曲的ID
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("song_sheet_id", "music_id")


class RadioStation(models.Model):
    # 电台
    class RadioType(models.TextChoices):
        Casual = 'Casual', _('随心听')
        Classic = 'Classic', _('经典')
        Popular = 'Popular', _('流行')
        Blue = 'Blue', _('忧伤')
        Cantonese = 'Cantonese', _('粤语')
        Calm = 'Calm', _('平静')
        GetUP = 'GetUP', _('起床')
        LoveSong = 'LoveSong', _('情歌')

    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # 用户的ID，就是这个电台是谁创建的
    radio_name = models.CharField(max_length=255, blank=False, null=False)  # 自建歌单名字
    img_url = models.URLField(blank=True, null=True)  # 封面URL
    radio_desc = models.TextField(default='')  # 电台描述
    label = models.CharField(max_length=255, blank=True, null=True)  # 电台的标签
    radio_classification = models.CharField(max_length=20, choices=RadioType.choices,
                                            default=RadioType.Casual)  # 电台类型
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("radio_name", "radio_classification")


class RadioStationMusic(models.Model):
    # 电台中的歌曲
    id = models.BigAutoField(primary_key=True)
    radio_station_id = models.ForeignKey(RadioStation, on_delete=models.CASCADE)  # 电台ID
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE)  # 歌曲的ID
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("radio_station_id", "music_id")