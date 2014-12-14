from django.contrib import admin
from basic.media.models import *

from imagekit.admin import AdminThumbnail


class AudioSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(AudioSet, AudioSetAdmin)


class AudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Audio, AudioAdmin)


class PhotoSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(PhotoSet, PhotoSetAdmin)


class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='photo_admin_thumbnail')
admin.site.register(Photo, PhotoAdmin)


class VideoSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(VideoSet, VideoSetAdmin)


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Video, VideoAdmin)
