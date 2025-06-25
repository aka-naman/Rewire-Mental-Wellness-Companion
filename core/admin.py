from django.contrib import admin
from .models import UserProfile, JournalEntry, MoodEntry

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_joined')
    search_fields = ('user__username', 'user__email')

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_created', 'date_modified')
    list_filter = ('date_created', 'user')
    search_fields = ('title', 'content', 'user__username')

@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood_type', 'mood_level', 'date_created')
    list_filter = ('mood_type', 'mood_level', 'date_created')
    search_fields = ('user__username', 'notes')
