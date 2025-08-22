from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUserRegistration(AbstractUser):
    firstname = models.CharField(blank=True, max_length=255)
    lastname = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    province = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    postal_code = models.CharField(max_length=10,
                                   validators=[
                                       RegexValidator(r'^\d{10}$', 'Postal code must be exactly 10 digits.')
                                   ],
                                   blank=True
                                   )
    extrainfo = models.TextField(blank=True)

    def __str__(self):
        return self.username

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None

    def is_old_enough(self):
        return self.age is not None and self.age >= 14
    #TODO: maybe delete age restriction, not really needed.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    province = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    extrainfo = models.TextField(blank=True)

    def __str__(self):
        return self.full_name or str(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)
