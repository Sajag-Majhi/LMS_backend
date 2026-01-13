from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User'

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=13, unique=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Book'
    
class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Borrow ID: {self.borrow_id}"
    
    class Meta:
        verbose_name_plural = 'Borrow'

