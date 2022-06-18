from django.db import models
from django.core.exceptions import ValidationError
import validators

def url_validator(url):

    if not validators.url(url):
        raise ValidationError('Url is invalid !')
    if url.find("v=")==-1:
        raise ValidationError('Url is invalid !')
    if url.find("youtube.com")==-1:
        raise ValidationError('Url is invalid !')

class Article(models.Model):
    title     = models.CharField(max_length=200, null=True, blank=False)
    content   = models.TextField(default='', null=True, blank=False)
    url       = models.CharField(max_length=200, null=True, blank=True,validators=[url_validator])
    photo     = models.ImageField(upload_to='images', null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title