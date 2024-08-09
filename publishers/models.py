from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class PublisherAnalytics(Analytics):
    class Meta:
        db_table = 'publisher_analytics'

class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True, db_column='publisher_id')
    name = models.CharField(max_length=255, db_column='publisher_name')
    analytics = models.OneToOneField(PublisherAnalytics, on_delete=models.CASCADE, db_column='analytics_id')

    class Meta:
        db_table = 'publisher'
