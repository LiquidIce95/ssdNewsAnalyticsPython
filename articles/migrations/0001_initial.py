# Generated by Django 4.2.15 on 2024-08-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('topics', '0001_initial'),
        ('newspapers', '0001_initial'),
        ('publishers', '0001_initial'),
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAnalytics',
            fields=[
                ('analytics_id', models.AutoField(db_column='analytics_id', primary_key=True, serialize=False)),
                ('bias', models.CharField(db_column='bias', max_length=255)),
                ('views', models.IntegerField(db_column='views')),
                ('shares', models.IntegerField(db_column='shares')),
                ('likes', models.IntegerField(db_column='likes')),
                ('engagement_rate', models.FloatField(db_column='engagement_rate')),
            ],
            options={
                'db_table': 'article_analytics',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(db_column='article_id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=255)),
                ('content', models.TextField(db_column='content')),
                ('analytics', models.OneToOneField(db_column='analytics_id', on_delete=django.db.models.deletion.CASCADE, to='articles.articleanalytics')),
                ('author', models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
                ('newspaper', models.ForeignKey(db_column='newspaper_id', on_delete=django.db.models.deletion.CASCADE, to='newspapers.newspaper')),
                ('owner', models.ForeignKey(db_column='owner_id', on_delete=django.db.models.deletion.CASCADE, to='owners.owner')),
                ('publisher', models.ForeignKey(db_column='publisher_id', on_delete=django.db.models.deletion.CASCADE, to='publishers.publisher')),
                ('topic', models.ForeignKey(db_column='topic_id', on_delete=django.db.models.deletion.CASCADE, to='topics.topic')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
