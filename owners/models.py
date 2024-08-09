from django.db import models
from core.models import Analytics  # Import the abstract Analytics class

class OwnerAnalytics(Analytics):
    class Meta:
        db_table = 'owner_analytics'

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True, db_column='owner_id')
    name = models.CharField(max_length=255, db_column='owner_name')
    analytics = models.OneToOneField(OwnerAnalytics, on_delete=models.CASCADE, db_column='owner_analytics_id')

    class Meta:
        db_table = 'owner'
