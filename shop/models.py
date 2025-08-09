from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Categories for shop modules """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)


    class Meta:
        verbose_name_plural = 'Catigories'


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name


class Module(models.Model):
    """ Purchaseable modules for diary """
    MODULE_TYPES = [
        ('meal_planner', 'Meal Planner'),
        ('cleaning_schedule', 'Cleaning Schedule'),
        ('stickers', 'Stickers'),
        ('habit_tracker', 'Habit Tracker'),
        ('budget_planner', 'Budget Planner'),
        ('workout_planner', 'Workout planner'),
        ('goal_tracker', 'Goal Tracker'),
    ]

    category = models.ForeignKey('Catigory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    module_type = models.CharField(max_length=50, choices=MODULE_TYPES)
    description = models.TextField()
    features = models.TextField(help_text="list features separated by new lines")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = modelsImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creat_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    class UserModule(models.Model):
        """ Tracks which moduels a user has purchased """
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        module = models.ForeignKey(Module, on_delete=models.CASCADE)
        purchased_date = models.DateTimeField(auto_now_add=True)
        is_active = models.BooleanField(default=True)

        class Meta:
            unique_togethr = ['user', 'module']

        def __str__(self):
            return f"{self.user.username} - {self.module.name}"
