from django.db import models

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True, db_column='analytics_id')
    bias = models.CharField(max_length=255, db_column='bias')
    views = models.IntegerField(db_column='views')
    shares = models.IntegerField(db_column='shares')
    likes = models.IntegerField(db_column='likes')
    engagement_rate = models.FloatField(db_column='engagement_rate')

    class Meta:
        abstract = True
        db_table = 'analytics'
