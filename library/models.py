from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages = models.PositiveIntegerField() 
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title