from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveBigIntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "song_master"


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "podcast_master"


class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "audiobook_master"
