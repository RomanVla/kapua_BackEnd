from django.db import models
from django.utils import timezone

class Employees(models.Model):
	emp_id = models.IntegerField()
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	created_date = models.DateTimeField(
            default=timezone.now)

	def __str__(self):
		return self.firstname +' '+ self.lastname

class Task(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Product(models.Model):
    owner = models.ForeignKey('testApp.Product', on_delete=models.CASCADE, blank = True, null=True)
    name = models.CharField(max_length=100) 
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name