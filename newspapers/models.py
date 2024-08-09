from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class NewspaperAnalytics(Analytics):
    class Meta:
        db_table = 'newspaper_analytics'

class Newspaper(models.Model):
    newspaper_id = models.AutoField(primary_key=True, db_column='newspaper_id')
    name = models.CharField(max_length=255, db_column='newspaper_name')
    analytics = models.OneToOneField(NewspaperAnalytics, on_delete=models.CASCADE, db_column='newspaper_analytics_id')

    class Meta:
        db_table = 'newspaper'
