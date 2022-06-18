from django.test import TestCase
from .models import Article,Comments,Author,Tag
from django.contrib.auth.models import User
# Create your tests here.
class ArticleTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="user",
            password="123"
        )
        UserObj = User.objects.get(id=1)
        Author.objects.create(
            name="Pan",
            surname="surname",
            User=UserObj
        )

        AuthorObj = Author.objects.get(id=1)
        self.Article_title = "title"
        self.Article_content="On the power of showing up and behavioral activation — Conventional wisdom says that positive"
        self.Article_url="https://www.youtube.com/watch?v=eKjmzHN_kSk&ab_channel=Farell"

        Article.objects.create(
            title=self.Article_title,
            content=self.Article_content,
            url=self.Article_url,
            Author = AuthorObj
        )

    def test_get_you_tube_url(self):
        ArticleObject = Article.objects.get(id=1)
        ArticleObject.save()
        self.assertEqual(ArticleObject.get_you_tube_url, 'eKjmzHN_kSk')

    def test_Article_model_create(self):
        AuthorObj = Author.objects.get(id=1)

        Tag.objects.create(
            tag_name="Fajny"
        )
        TagObj = Tag.objects.get(id=1)


        ArticleObj = Article.objects.get(id=1)

        Comments.objects.create(
            content=self.Article_content,
            Author=AuthorObj,
            Article=ArticleObj
        )
        CommentsObj = Comments.objects.get(id=1)

        ArticleObj.Comments.add(CommentsObj)
        ArticleObj.Tags.add(TagObj)

        self.assertEqual(ArticleObj.title, self.Article_title)
        self.assertEqual(ArticleObj.content, self.Article_content)
        self.assertEqual(ArticleObj.url, self.Article_url)
        self.assertEqual(len(ArticleObj.Comments.all()), 1)
        self.assertEqual(len(ArticleObj.Tags.all()), 1)

class CommentsTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="user",
            password="123"
        )
        UserObj = User.objects.get(id=1)
        Author.objects.create(
            name="Pan",
            surname="surname",
            User=UserObj
        )

        AuthorObj = Author.objects.get(id=1)
        Article.objects.create(
            title="title",
            content="On the power of showing up and behavioral activation — Conventional wisdom says that positive "
                    "thinking, enthusiasm, and inspiration are key to living a good and productive life. But that’s"
                    " not entirely true, at least not",
            url="https://www.youtube.com/watch?v=eKjmzHN_kSk&ab_channel=Farell",
            Author = AuthorObj
        )
        ArticleObject = Article.objects.get(title="title")
        self.comment_content='On the power of showing up and behavioral activation — Conventional wisdom says that positive'
        Comments.objects.create(
            content=self.comment_content,
            Article=ArticleObject,
            Author = AuthorObj
        )

    def test_coment_add_to_relation(self):
        first = Article.objects.get(title="title")
        self.assertEqual(len(first.Comments.all()), 1)

    def test_Comments_model_create(self):
        CommentsObj = Comments.objects.get(id=1)
        self.assertEqual(CommentsObj.content, self.comment_content)





