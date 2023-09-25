from django.db import models

class Card(models.Model):
    image = models.ImageField(upload_to='card_images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=50, default='')  # Set your desired default value

    def get_full_link_url(self):
        base_url = "http://127.0.0.1:8000/"
        return base_url + self.link + ".html"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

