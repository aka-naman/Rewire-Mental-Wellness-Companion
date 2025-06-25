from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, JournalEntryForm, MoodEntryForm
from .models import JournalEntry, MoodEntry

def home(request):
    """Home page view"""
    # Show home page to all users, even if authenticated
    return render(request, 'home.html')

def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    """User profile view"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    # Get recent mood entries
    recent_moods = MoodEntry.objects.filter(user=request.user).order_by('-date_created')[:5]
    
    # Get journal stats
    journal_count = JournalEntry.objects.filter(user=request.user).count()
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'recent_moods': recent_moods,
        'journal_count': journal_count
    }
    return render(request, 'profile.html', context)

@login_required
def journal_view(request):
    """Journal entries view"""
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.user = request.user
            journal_entry.save()
            messages.success(request, 'Journal entry created successfully!')
            return redirect('journal')
    else:
        form = JournalEntryForm()
    
    # Get all journal entries for the user
    entries = JournalEntry.objects.filter(user=request.user).order_by('-date_created')
    
    # Handle search
    query = request.GET.get('q')
    if query:
        entries = entries.filter(content__icontains=query) | entries.filter(title__icontains=query)
    
    context = {
        'form': form,
        'entries': entries,
        'query': query
    }
    return render(request, 'journal.html', context)

@login_required
def journal_entry_detail(request, pk):
    """Journal entry detail view"""
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Journal entry updated successfully!')
            return redirect('journal')
    else:
        form = JournalEntryForm(instance=entry)
    
    context = {
        'form': form,
        'entry': entry
    }
    return render(request, 'journal_detail.html', context)

@login_required
def journal_entry_delete(request, pk):
    """Journal entry delete view"""
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Journal entry deleted successfully!')
        return redirect('journal')
    
    context = {
        'entry': entry
    }
    return render(request, 'journal_delete.html', context)

@login_required
def mood_tracker_view(request):
    """Mood tracker view"""
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            messages.success(request, 'Mood entry recorded successfully!')
            return redirect('mood')
    else:
        form = MoodEntryForm()
    
    # Get all mood entries for the user
    entries = MoodEntry.objects.filter(user=request.user).order_by('-date_created')
    
    # Get mood data for visualization
    mood_data = {
        'labels': [],
        'values': [],
        'colors': []
    }
    
    # Color mapping for moods
    color_map = {
        'happy': '#FFD700',  # Gold
        'neutral': '#A9A9A9',  # Dark Gray
        'sad': '#6495ED',  # Cornflower Blue
        'angry': '#FF4500',  # Orange Red
        'crying': '#9370DB',  # Medium Purple
    }
    
    # Get last 7 days of mood entries
    last_week = timezone.now() - timedelta(days=7)
    recent_moods = MoodEntry.objects.filter(
        user=request.user, 
        date_created__gte=last_week
    ).order_by('date_created')
    
    for mood in recent_moods:
        mood_data['labels'].append(mood.date_created.strftime('%Y-%m-%d'))
        mood_data['values'].append(mood.mood_level)
        mood_data['colors'].append(color_map.get(mood.mood_type, '#000000'))
    
    context = {
        'form': form,
        'entries': entries,
        'mood_data': mood_data
    }
    return render(request, 'mood_tracker.html', context)

@login_required
def dashboard_view(request):
    """Dashboard view"""
    # Get recent journal entries
    recent_journals = JournalEntry.objects.filter(user=request.user).order_by('-date_created')[:3]
    # Get recent mood entries
    recent_moods = MoodEntry.objects.filter(user=request.user).order_by('-date_created')[:5]
    # Get mood data for chart
    mood_data = {
        'labels': [],
        'values': [],
        'colors': []
    }
    color_map = {
        'happy': '#FFD700',
        'neutral': '#A9A9A9',
        'sad': '#6495ED',
        'angry': '#FF4500',
        'crying': '#9370DB',
    }
    last_week = timezone.now() - timedelta(days=7)
    weekly_moods = MoodEntry.objects.filter(user=request.user, date_created__gte=last_week).order_by('date_created')
    for mood in weekly_moods:
        mood_data['labels'].append(mood.date_created.strftime('%Y-%m-%d'))
        mood_data['values'].append(mood.mood_level)
        mood_data['colors'].append(color_map.get(mood.mood_type, '#000000'))
    mood_stats = {
        'count': MoodEntry.objects.filter(user=request.user).count(),
        'avg_level': MoodEntry.objects.filter(user=request.user).aggregate(Avg('mood_level'))['mood_level__avg'] or 0,
    }
    # Add missing context variables for dashboard.html
    journal_count = JournalEntry.objects.filter(user=request.user).count()
    mood_count = MoodEntry.objects.filter(user=request.user).count()
    # Days active: count of unique days with a mood or journal entry
    mood_days = MoodEntry.objects.filter(user=request.user).dates('date_created', 'day')
    journal_days = JournalEntry.objects.filter(user=request.user).dates('date_created', 'day')
    days_active = len(set(mood_days) | set(journal_days))
    # Current streak: consecutive days with at least one entry (mood or journal)
    from datetime import date, timedelta as td
    all_days = sorted(set([d.date() for d in mood_days] + [d.date() for d in journal_days]), reverse=True)
    current_streak = 0
    today = date.today()
    for i, d in enumerate(all_days):
        if i == 0 and d == today:
            current_streak = 1
        elif i > 0 and (all_days[i-1] - d).days == 1:
            current_streak += 1
        elif i == 0 and d != today:
            break
        else:
            break
    context = {
        'recent_journals': recent_journals,
        'recent_moods': recent_moods,
        'mood_data': mood_data,
        'mood_stats': mood_stats,
        'journal_count': journal_count,
        'mood_count': mood_count,
        'days_active': days_active,
        'current_streak': current_streak
    }
    return render(request, 'dashboard.html', context)
