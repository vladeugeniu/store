from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Category(models.Model):
	
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Book(models.Model):

	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey(Category)
	price = models.BigIntegerField()
	amount = models.BigIntegerField()

	def sell(self):

		self.amount = self.amount -1

	def __str__(self):

		return self.name

class Sell(models.Model):

	name = models.CharField(max_length=100)
	surrname = models.CharField(max_length=100)
	adress = models.TextField(max_length=250)
	mentions = models.TextField()
	book = models.ForeignKey(Book)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):

		return self.book.name
class Buy(models.Model):

	book_name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey(Category)
	price = models.BigIntegerField()
	amount = models.BigIntegerField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=16,validators=[phone_regex], blank=True) # validators should be a list
	email = models.CharField(max_length=150)


	def __str__(self):

		return self.book_name