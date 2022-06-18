from django.views.generic import ListView

from app.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 5
    ordering = ['-create_at']