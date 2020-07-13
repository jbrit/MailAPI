from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class EmailAdded(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(person=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
