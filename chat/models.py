from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
import secrets
import math, datetime
from django.utils import timezone, timesince

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    

    def get_absolute_url(self):
        return reverse("chat:index", kwargs={
            
            'chat_slug':self.slug,
        })

    def get_messages(self):
        messages = Message.objects.filter(chat=self)
        return messages
    
    def get_most_recent_message(self):
        messages = Message.objects.filter(chat=self)
        return messages.order_by('-created_at').first()

    def __str__(self):
        return f"{self.user}" 
    
    def delete_with_messages(self):
        self.messages.all().delete()
        self.delete()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(secrets.token_hex(5))  # Generate a 10-character slug
        super().save(*args, **kwargs)
        
    def time_elapsed(self):
        now = timezone.now()
        elapsed_time = now - self.created_at
        days = elapsed_time.days
        hours = elapsed_time.seconds // 3600
        minutes = elapsed_time.seconds // 60

        if days > 7:
            return self.created_at  
        elif days >= 2:
            return f"{days} days ago"
        elif days == 1:
            return f"{days} day ago"
        elif hours >= 1:
            return f"{hours} hours ago"
        elif minutes >= 1:
            return f"{minutes} minutes ago"
        else:
            return "Less than a minute ago"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



