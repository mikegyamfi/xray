# Generated by Django 4.2.4 on 2025-01-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0006_admininfo_ishare_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afaregistration',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='bigtimetransaction',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='isharebundletransaction',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='mtntransaction',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='vodafonetransaction',
            name='reference',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
