from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json


class Mealplan(models.Model):
    """ Meal Planning module data """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default==timezone)
    breakfast = models.TextField(blank=True)
    lunch = models.TextField(blank=True)
    dinner = models.TextField(blank=True)
    snacks = models.TextField(blank=True)
    water_intake = models.IntegerField(default=0, help_text="Glasses of water")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user.usernmae} - Meal Plan {self.date}"


class CleaningTask(models.Model):
    """" Cleaning schedual module data """
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weeekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    room = models.CharField(max_length=100)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    last_completed = models.DateField(null=True, blank=True)
    next_due =models.DateField()
    notes = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['next_due']

    def __str__(self):
        return f"{self.task_name} - {self.room}"


class Stickers(models.Model):
    """ Digital stickers for diary entries """
    diary = models.ForeignKey('diary.DiaryEntry', on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    size = models.IntegerField(default=100)


    def __str__(self):
        return f"{self.diary_entry} - {self.sticker}"


class HabitTracker(models.Model):
    """ Habit tracker module data """
    user = models.ForeignKey(User, on_delete=True)
    habit_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    target_frecuency = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ])
    color = models.CharField(max_length=7, default='#3498db')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.habit_name}"


class HabitLog(models.Model):
    """ Log entries for Hbit tracking """
    habit = models.ForeignKey( HabitTracker, on_delete=True)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['habit', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.habit.habit_name} - {self.date}"
