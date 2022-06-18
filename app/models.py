from django.db import models
from django.core.exceptions import ValidationError
from django.conf.global_settings import AUTH_USER_MODEL
import validators

def url_validator(url):

    if not validators.url(url):
        raise ValidationError('Url is invalid !')
    if url.find("v=")==-1:
        raise ValidationError('Url is invalid !')
    if url.find("youtube.com")==-1:
        raise ValidationError('Url is invalid !')

class Author(models.Model):
    name    = models.CharField(max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    User = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return  self.name+' '+self.surname

class Article(models.Model):
    title     = models.CharField(max_length=200, null=True, blank=False)
    content   = models.TextField(default='', null=True, blank=False)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    url       = models.CharField(max_length=200, null=True, blank=True,validators=[url_validator])
    photo     = models.ImageField(upload_to='images', null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title