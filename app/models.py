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
    name      = models.CharField(max_length=100,null=True,blank=True)
    surname   = models.CharField(max_length=100, null=True, blank=True)
    User      = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return  self.name+' '+self.surname

class Tag(models.Model):
    tag_name = models.CharField(max_length=100,null=True,blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.tag_name

class Article(models.Model):
    title     = models.CharField(max_length=200, null=True, blank=False)
    content   = models.TextField(default='', null=True, blank=False)
    Author    = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=False)
    Tags      = models.ManyToManyField(to='app.Tag', related_name='Tags', blank=True)
    Comments = models.ManyToManyField(to='app.Comments', related_name='Comments', blank=True)
    url       = models.CharField(max_length=200, null=True, blank=True,validators=[url_validator])
    photo     = models.ImageField(upload_to='images', null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    @property
    def get_you_tube_url(self):
        code = ''
        index = self.url.find("v=")
        add = True
        for i in range(index + 2, len(self.url)):
            if self.url[i] == '&':
                add = False

            if self.url[i] and add == True:
                code = code + self.url[i]
        return code

    def __str__(self):
        return  self.title

class Comments(models.Model):
    content  = models.TextField(default='', null=False, blank=False)
    Author   = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=True)
    Article  = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False, null=True)
    create_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.Article:
            super(Comments, self).save()
            self.Article.Comments.add(self)
        else:
            super(Comments, self).save()

    def __str__(self):
        return  str(self.Author)+' - '+self.content