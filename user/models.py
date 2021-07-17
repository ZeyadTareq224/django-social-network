from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

GENDER = [
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other')
]
class User(AbstractUser):

	
	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='images/profile_pics', default='images/profile_pics/default.jpg')
	gender = models.CharField(choices=GENDER, max_length=6)
	location = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=16)
	bio = models.TextField()

	def get_absolute_url(self):
		return reverse('user_profile', kwargs={'user_id': self.user.id})


	def __str__(self):
		return f"{self.user.username}'s profile"