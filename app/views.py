from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from app.models import Article, Tag, Comments, Author


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 5
    ordering = ['-create_at']

class TagsListView(ListView):
    model = Tag
    template_name = 'tags_list.html'
    paginate_by = 5
    ordering = ['-create_at']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

class NewComment(LoginRequiredMixin,CreateView):
    fields = ['content']
    model = Comments
    success_url = '/'

    def form_valid(self,form):
        form.instance.Article = Article.objects.get(id=self.kwargs['pk'])
        form.instance.Author  = Author.objects.filter(User=self.request.user).get()
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ArticleDetail',kwargs={'pk':self.kwargs['pk']})

class BaseEdit:

    def can_edit(self):
        return self.object.Author.User == self.request.user

    def on_form_valid(self,form):
        form.instance.Author = Author.objects.filter(User=self.request.user).get()
        self.object = form.save()
        return redirect('/admin/login/')

class ArticleCreateView(LoginRequiredMixin,CreateView,BaseEdit):
    fields = ['title', 'content', 'Tags', 'url', 'photo']
    success_url = '/'
    model = Article

    def form_valid(self, form):
        self.on_form_valid(form)
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,UpdateView,BaseEdit):
    fields = ['title','content','Tags','url','photo']
    success_url = '/'
    model = Article

    def form_valid(self, form):
        if self.can_edit():
            self.on_form_valid(form)
        return super().form_valid(form)