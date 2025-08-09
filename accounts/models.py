from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ Extended user profile with additonal information """
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    date_of_brith = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(uppload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    #Address informaton for shipping
    street_address1 = models.CharField(max_length=80, blank=True)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=80, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=80, blank=True)

    ceated_at = models.DateTimeField(auto_now_add=True)
    uppdated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        retun f"{self.user.usernsme}'s profile"


    @recever(post_save, sender=User)"
    def creat_or_update_user_prifile(sender, instance, created, **kwargs):
        """ Create or uppdate the user profile """
        if created:
            UserProfile.objects.create(user=instance)
        instance.Userprofile.save()
