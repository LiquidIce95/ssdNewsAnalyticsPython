# Generated by Django 4.2.15 on 2024-08-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerAnalytics',
            fields=[
                ('analytics_id', models.AutoField(db_column='analytics_id', primary_key=True, serialize=False)),
                ('bias', models.CharField(db_column='bias', max_length=255)),
                ('views', models.IntegerField(db_column='views')),
                ('shares', models.IntegerField(db_column='shares')),
                ('likes', models.IntegerField(db_column='likes')),
                ('engagement_rate', models.FloatField(db_column='engagement_rate')),
            ],
            options={
                'db_table': 'owner_analytics',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.AutoField(db_column='owner_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='owner_name', max_length=255)),
                ('analytics', models.OneToOneField(db_column='analytics_id', on_delete=django.db.models.deletion.CASCADE, to='owners.owneranalytics')),
            ],
            options={
                'db_table': 'owner',
            },
        ),
    ]
