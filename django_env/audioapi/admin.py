from django.contrib import admin
from .models import Song, Podcast, AudioBook

admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(AudioBook)
