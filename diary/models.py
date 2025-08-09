from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DiaryEntry(models.Model):
    """ Main diary enrty model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(max_length=50, choices=[
        ('happy', '😊 Happy'),
        ('sad', '😢 Sad'),
        ('neutral', '😐 Neutral'),
        ('excited', '🤩 Excited'),
        ('anxious', '😰 Anxious'),
        ('angry', '😠 Angry'),
        ('grateful', '🙏 Grateful'),
    ], null=True, blank=True)
    weather = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(
        max_length=200, blank=True, help_text="Comma-separateted tags"
        )
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        unique_together = ['user', 'date']
        verbose_name_plural = 'Diary entries'

    def __str__(self):
        return f"{self.user.username} - {self.date}"
