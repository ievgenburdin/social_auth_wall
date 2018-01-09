from django.contrib import admin
from django.contrib import admin
# MPTT using for nesting categories, read on https://django-mptt.readthedocs.io/
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin

from wall.models import Message, Comment


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created')

class CommentAdmin(MPTTModelAdmin):
    list_display = ('text', 'message_id', 'created')


admin.site.register(Message, MessageAdmin)

admin.site.register(Comment, CommentAdmin)