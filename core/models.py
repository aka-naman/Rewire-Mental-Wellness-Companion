from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Journal Entries'
    
    def __str__(self):
        return f"{self.title} - {self.date_created.strftime('%Y-%m-%d')}"

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', '😄 Happy'),
        ('neutral', '😐 Neutral'),
        ('sad', '😟 Sad'),
        ('angry', '😠 Angry'),
        ('crying', '😭 Crying'),
    ]
    
    MOOD_LEVELS = [
        (1, 'Very Low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Very High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_entries')
    mood_type = models.CharField(max_length=20, choices=MOOD_CHOICES)
    mood_level = models.IntegerField(choices=MOOD_LEVELS)
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Mood Entries'
    
    def __str__(self):
        return f"{self.user.username}'s Mood: {self.get_mood_type_display()} ({self.date_created.strftime('%Y-%m-%d')})"
