from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class TopicAnalytics(Analytics):
    class Meta:
        db_table = 'topic_analytics'

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True, db_column='topic_id',null=False)
    name = models.CharField(max_length=255, db_column='topic_name',null=False)
    analytics = models.OneToOneField(TopicAnalytics, on_delete=models.CASCADE, db_column='topic_analytics_id',null=False)

    class Meta:
        db_table = 'topic'
