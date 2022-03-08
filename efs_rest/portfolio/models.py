from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_number = models.CharField(max_length=50)
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=250)
    task_priority = models.CharField(max_length=50)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.task_number)


class Feedback(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='feedback')
    fb_description = models.CharField(max_length=200)
    fb_from = models.CharField(max_length=200)


    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.task)





class Meeting(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='feedback')
    mtg_with = models.CharField(max_length=50)
    mtg_date = models.DateField(default=timezone.now, blank=True, null=True)
    mtg_description = models.CharField(max_length=200)
   

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.task)


    def cust_number(self):
        return self.task.task_number

