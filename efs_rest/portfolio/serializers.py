from rest_framework import serializers
from .models import Task, Feedback, Meeting


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
            model = Task

            fields = ('pk', 'task_number', 'task_name', 'task_description', 'task_priority')

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
            model = Feedback
            fields = ('pk', 'task', 'fb_description', 'fb_from')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
            model = Meeting
            fields = ('pk', 'task','mtg_with', 'mtg_date', 'mtg_description')
