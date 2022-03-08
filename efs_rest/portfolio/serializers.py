from rest_framework import serializers
from .models import Task, Feedback, Meeting


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
            model = Task

            fields = ('pk', 'task_number', 'task_name', 'task_description', 'task_priority')

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
            model = Feedback
            fields = ('pk', 'fb_description', 'fb_from')


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
            model = Meeting
            fields = ('pk', 'mtg_with', 'mtg_date', 'mtg_description')
