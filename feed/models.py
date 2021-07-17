from django.db import models
from user.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse


class Post(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to='post_images')
	comments = GenericRelation(Comment)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('post_details', kwargs={'post_id': self.id})

	def __str__(self):
		return f"{self.user.username}'s post ID: {self.id}"	
