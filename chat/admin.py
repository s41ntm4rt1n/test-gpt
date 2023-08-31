from django.contrib import admin
from .models import Chat, Message



class MessageInLine(admin.StackedInline):
    model = Message
    extra = 1

class ChatAdmin(admin.ModelAdmin):
    list_display=['user','created_at']
    list_filter = ['user', 'created_at']
    inlines = (MessageInLine,)

admin.site.register(Chat, ChatAdmin)    

