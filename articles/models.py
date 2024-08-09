from django.db import models
from authors.models import Author
from publishers.models import Publisher
from topics.models import Topic
from owners.models import Owner
from newspapers.models import Newspaper
from core.models import Analytics  # Import the abstract Analytics class

class ArticleAnalytics(Analytics):
    class Meta:
        db_table = 'article_analytics'

class Article(models.Model):
    article_id = models.AutoField(primary_key=True, db_column='article_id')
    title = models.CharField(max_length=255, db_column='title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, db_column='publisher_id')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, db_column='topic_id')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='owner_id')
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, db_column='newspaper_id')
    content = models.TextField(db_column='content')
    analytics = models.OneToOneField(ArticleAnalytics, on_delete=models.CASCADE, db_column='article_analytics_id')

    class Meta:
        db_table = 'article'
