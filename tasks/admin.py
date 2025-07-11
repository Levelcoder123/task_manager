from django.contrib import admin

from tasks.models import Task, User


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'due_date', 'user']
    list_filter = ['status', 'priority', 'due_date', 'user']
    search_fields = ['title', 'description', 'user__username']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'email']
