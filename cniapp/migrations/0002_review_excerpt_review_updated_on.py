# Generated by Django 4.2.16 on 2024-10-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cniapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]