from django.db import models

class Publisher (models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    state_province=models.CharField(max_length=30)
    country=models.CharField(max_length=50)
    website=models.URLField()

    def __str__(self):
        return 'Publisher {}; address - {}'.format(self.name, self.address)


class Author (models.Model):
    salutation=models.CharField(max_length=10)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    headshot=models.ImageField(upload_to='img')

    def __str__(self):
        return 'Author {} {}'.format(self.first_name, self.last_name)


class Book (models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date=models.DateTimeField()

    def __str__(self):
        return 'Book {}'.format(self.title)
