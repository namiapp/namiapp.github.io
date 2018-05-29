from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


# Student extends User
class CustomUser(AbstractUser):
	name = models.CharField(blank=True, max_length=255)

	def __str__(self):
		return self.email

# # Universities model
# class University(models.Model):

# 	name    = models.CharField(max_length=200)
# 	email   = models.EmailField()
# 	address = models.CharField(max_length=50)
# 	country = models.CharField(max_length=50)

# 	# many users to many universities
# 	# student    = models.ManyToManyField('Student')

# 	# Meta's verbose_name_plural pluralizes universities correctly
# 	class Meta:
# 		verbose_name = "University"
# 		verbose_name_plural = "Universities"


# 	def __str__(self):
# 		return self.name

# # a university can have multiple organizations,
# # but organizations cannot be shared
# class Organization(models.Model):

# 	name    = models.CharField(max_length=200)
# 	email   = models.EmailField()
# 	address = models.CharField(max_length=50)
# 	country = models.CharField(max_length=50)
# 	university = models.ForeignKey(University, on_delete=models.CASCADE)
# 	# student    = models.ManyToManyField('Student')

# 	def __str__(self):
# 		return self.name