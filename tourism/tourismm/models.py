from django.db import models

# Create your models here.


class Discover(models.Model):
    name = models.CharField(max_length=250, null=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    activities = models.CharField(max_length=250, null=True)
    cost = models.TextField(max_length=50, null=True)
    first_image = models.ImageField(null=True, blank=True)
    second_image = models.ImageField(null=True, blank=True)
    third_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def first_image_URL(self):
        try:
            url = self.first_image.url
        except:
            url = ''
        return url

    def second_image_URL(self):
        try:
            url = self.second_image.url
        except:
            url = ''
        return url

    def third_image_URL(self):
        try:
            url = self.third_image.url
        except:
            url = ''
        return url


class Ttd(models.Model):
    name = models.CharField(max_length=250, null=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    activities = models.CharField(max_length=250, null=True)
    cost = models.TextField(max_length=50, null=True)
    first_image = models.ImageField(null=True, blank=True)
    second_image = models.ImageField(null=True, blank=True)
    third_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def first_image_URL(self):
        try:
            url = self.first_image.url
        except:
            url = ''
        return url

    def second_image_URL(self):
        try:
            url = self.second_image.url
        except:
            url = ''
        return url

    def third_image_URL(self):
        try:
            url = self.third_image.url
        except:
            url = ''
        return url


PLACE_CHOICES = (
    ('Family Package', 'Family Package'),
    ('Solo Package', 'Solo Package'),
    ('Complete Guided Package', 'Complete Guided Package')


)

AIRLINE_CHOICES = (
    ('Buddha Airlines', 'Buddha Airlines'),



)

HOTEL_CHOICES = (
    ('HeavenView Hotel', 'HeavenView Hotel'),
    ('NepStay', 'NepStay')



)


class Book(models.Model):
    name = models.CharField(max_length=250, null=True)
    package = models.CharField(
        max_length=100, choices=PLACE_CHOICES, default='Family Package')
    no_Of_People = models.CharField(max_length=100, null=True)
    check_In_Date = models.DateField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)


class Flight(models.Model):
    name = models.CharField(max_length=250, null=True)
    airlines = models.CharField(
        max_length=100, choices=AIRLINE_CHOICES, default='Buddha Airlines')
    no_Of_People = models.CharField(max_length=100, null=True)
    check_In_Date = models.DateField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=250, null=True)
    hotel = models.CharField(
        max_length=100, choices=HOTEL_CHOICES, default='NepStay')
    no_Of_People = models.CharField(max_length=100, null=True)
    check_In_Date = models.DateField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
