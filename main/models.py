# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from PIL import Image
from django.utils import timezone

class Site(models.Model):
    title = models.CharField(max_length=120)
    ceo = models.CharField(max_length=120)
    email = models.EmailField()
    tel = models.CharField(max_length=100)
    about = HTMLField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    twitter = models.URLField(max_length=120, blank=True, null=True)
    facebook = models.URLField(max_length=120, blank=True, null=True)
    instagram = models.URLField(max_length=120, blank=True, null=True)
    keywords = models.CharField(max_length=250, default="")
    icon = models.ImageField(upload_to='site/', blank=True, null=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    image1 = models.ImageField(upload_to='site/', blank=True, null=True)
    image2 = models.ImageField(upload_to='site/', blank=True, null=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    comment = models.TextField()
    image = models.ImageField(upload_to='review/', blank=True, null=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='sliders/')
    def save(self, *args, **kwargs):
        super(Slider, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            target_w = 768
            target_h = 260
            img_sized = img.resize((target_w, target_h), Image.ANTIALIAS)
            img_sized.save(self.image.path)
    def __str__(self):
        return self.caption[:20]

    class Meta:
        verbose_name_plural = 'Sliders'

class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    items = models.ManyToManyField(to='Item',)
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    image2 = models.ImageField(upload_to='services/', blank=True, null=True)
    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(self.thumbnail.path)
            target_w = 340
            target_h = 200
            img_sized = img.resize((target_w, target_h), Image.ANTIALIAS)
            img_sized.save(self.thumbnail.path)
    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    def __str__(self):
        return self.title

class Item(models.Model):
    title = title = models.CharField(max_length=120)
    def __str__(self):
        return self.title

class Developer(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="doctors/")
    details = models.TextField()
    experience = models.TextField()
    expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
    twitter = models.URLField(max_length=120, blank=True, null=True)
    facebook = models.URLField(max_length=120, blank=True, null=True)
    instagram = models.URLField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class Expertize(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}: {self.email}'
    class Meta:
        ordering = ['-date']


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField(default='', blank=True)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"


