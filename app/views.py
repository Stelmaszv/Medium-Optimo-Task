from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

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

class NewComment(CreateView):
    fields = ['content']
    model = Comments
    success_url = '/'

    def form_valid(self,form):
        if self.request.user.is_authenticated:
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
        if self.request.user.is_authenticated:
            form.instance.Author = Author.objects.filter(User=self.request.user).get()
            self.object = form.save()
        else:
            return redirect('/admin/login/')