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
    article_id = models.AutoField(primary_key=True, db_column='article_id',null=False)
    title = models.CharField(max_length=255, db_column='title',null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_id',null=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, db_column='publisher_id',null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, db_column='topic_id',null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, db_column='owner_id',null=False)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, db_column='newspaper_id',null=False)
    content = models.TextField(db_column='content',null=False)
    analytics = models.OneToOneField(ArticleAnalytics, on_delete=models.CASCADE, db_column='article_analytics_id',null=False)

    class Meta:
        db_table = 'article'
