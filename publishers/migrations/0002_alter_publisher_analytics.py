# Generated by Django 4.2.15 on 2024-08-09 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='analytics',
            field=models.OneToOneField(db_column='publisher_analytics_id', on_delete=django.db.models.deletion.CASCADE, to='publishers.publisheranalytics'),
        ),
    ]
