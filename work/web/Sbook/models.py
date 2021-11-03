from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    username =models.CharField('username', max_length=200, null=True)
    email = models.CharField('email', max_length=200, null=True)
    password = models.CharField('password', max_length=200, null=True)

    def __str__(self):
        return self.username
class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, null=True)
    discription = models.TextField()
    posted_Date = models.DateField(default=date.today)
    good_name = models.CharField(max_length=200, null=True)


class Coment(models.Model):
    message = models.TextField('message')
    date_coment = models.DateField(default=date.today)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id =  models.ForeignKey(Blog, on_delete=models.CASCADE)

class Contant(models.Model):
    name = models.CharField(max_length=200 )
    country = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)




