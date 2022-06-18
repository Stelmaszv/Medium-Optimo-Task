from django.contrib import admin

from app.models import Article, Author, Comments, Tag

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments)