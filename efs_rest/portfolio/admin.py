from django.contrib import admin
from .models import Task, Feedback, Meeting

class TaskList(admin.ModelAdmin):
    list_display = ('task_number', 'task_name', 'task_description', 'task_priority')
    list_filter = ('task_number', 'task_name')
    search_fields = ('task_number', 'task_name')
    ordering = ['task_number']


class FeedbackList(admin.ModelAdmin):
    list_display = ('task', 'fb_description', 'fb_from')
    list_filter = ('task', 'fb_from')
    search_fields = ('task', 'fb_from')
    ordering = ['task']


class MeetingList(admin.ModelAdmin):
    list_display = ('task','mtg_with', 'mtg_date', 'mtg_description')
    list_filter = ('task')
    search_fields = ('task')
    ordering = ['task']


admin.site.register(Task, TaskList)
admin.site.register(Feedback, FeedbackList)
admin.site.register(Meeting, MeetingList)
