from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
class MyUser(AbstractBaseUser):
	name=models.CharField(max_length=200)
	email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['date_of_birth']