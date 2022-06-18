"""medium2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import ArticleListView, TagsListView, ArticleDetailView, NewComment
from medium2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(''                       ,ArticleListView.as_view(),name='Articles'),
    path('article/<int:pk>/'      ,ArticleDetailView.as_view(),name='ArticleDetail'),
    path('new_comment/<int:pk>/'  ,NewComment.as_view(),name='NewComment'),
    path('tags'                   ,TagsListView.as_view(),name='Tags')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)