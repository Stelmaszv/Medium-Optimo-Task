from django.views.generic import ListView, DetailView

from app.models import Article, Tag


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