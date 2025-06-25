from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('journal/', views.journal_view, name='journal'),
    path('journal/<int:pk>/', views.journal_entry_detail, name='journal_detail'),
    path('journal/<int:pk>/delete/', views.journal_entry_delete, name='journal_delete'),
    path('mood/', views.mood_tracker_view, name='mood'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]