# Generated by Django 4.2.4 on 2024-09-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0004_admininfo_telecel_api_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentvodabundleprice',
            name='geosams_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='superagentvodabundleprice',
            name='geosams_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vodabundleprice',
            name='geosams_active',
            field=models.BooleanField(default=False),
        ),
    ]
