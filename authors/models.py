from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class AuthorAnalytics(Analytics):
    class Meta:
        db_table = 'author_analytics'

class Author(models.Model):
    author_id = models.AutoField(primary_key=True, db_column='author_id',null=False)
    name = models.CharField(max_length=255, db_column='author_name',null=False)
    age = models.IntegerField(db_column='author_age',null=False)
    analytics = models.OneToOneField(AuthorAnalytics, on_delete=models.CASCADE, db_column='author_analytics_id',null=False)

    class Meta:
        db_table = 'author'
