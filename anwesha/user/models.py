from enum import unique
from django.db import models

class User(models.Model):
    anwesha_id              = models.CharField(max_length=10, primary_key=True, unique=True)
    password                = models.CharField(max_length=100)
    phone_number            = models.CharField(max_length=13)
    email_id                = models.EmailField(unique= True)
    full_name               = models.CharField(max_length=100)
    college_name            = models.CharField(max_length=150)
    profile_photo           = models.URLField()
    age                     = models.SmallIntegerField()
    is_email_verified       = models.BooleanField()
    user_type               = models.CharField()
    qr_code                 = models.URLField()
    gender                  = models.CharField(max_length=20)
    accomadation_selected   = models.BooleanField()
    is_profile_completed    = models.BooleanField()
    instagram_id            = models.CharField(max_length=100)
    facebook_id             = models.CharField(max_length=100)
    time_of_registration    = models.DateTimeField(auto_now_add=True)
