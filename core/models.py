from django.db import models

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True, db_column='analytics_id',null=False)
    bias = models.CharField(max_length=255, db_column='bias',null=False)
    views = models.IntegerField(db_column='views',null=False)
    shares = models.IntegerField(db_column='shares',null=False)
    likes = models.IntegerField(db_column='likes',null=False)
    engagement_rate = models.FloatField(db_column='engagement_rate',null=False)

    class Meta:
        abstract = True
        db_table = 'analytics'
