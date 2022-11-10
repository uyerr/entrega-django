from django.contrib import admin
from chats.models import ThreadModel, MessageModel

# Register your models here.

admin.site.register(ThreadModel)

admin.site.register(MessageModel)