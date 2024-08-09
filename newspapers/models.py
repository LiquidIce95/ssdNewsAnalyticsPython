from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class NewspaperAnalytics(Analytics):
    class Meta:
        db_table = 'newspaper_analytics'

class Newspaper(models.Model):
    newspaper_id = models.AutoField(primary_key=True, db_column='newspaper_id',null=False)
    name = models.CharField(max_length=255, db_column='newspaper_name',null=False)
    analytics = models.OneToOneField(NewspaperAnalytics, on_delete=models.CASCADE, db_column='newspaper_analytics_id',null=False)

    class Meta:
        db_table = 'newspaper'
