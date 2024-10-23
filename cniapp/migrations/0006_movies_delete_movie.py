# Generated by Django 4.2.16 on 2024-10-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cniapp', '0005_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotten_tomatoes_link', models.TextField(blank=True, null=True)),
                ('movie_title', models.TextField(blank=True, null=True)),
                ('movie_info', models.TextField(blank=True, null=True)),
                ('critics_consensus', models.TextField(blank=True, null=True)),
                ('content_rating', models.TextField(blank=True, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('directors', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('actors', models.TextField(blank=True, null=True)),
                ('original_release_date', models.TextField(blank=True, null=True)),
                ('streaming_release_date', models.TextField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('production_company', models.TextField(blank=True, null=True)),
                ('tomatometer_status', models.TextField(blank=True, null=True)),
                ('tomatometer_rating', models.IntegerField(blank=True, null=True)),
                ('tomatometer_count', models.IntegerField(blank=True, null=True)),
                ('audience_status', models.TextField(blank=True, null=True)),
                ('audience_rating', models.IntegerField(blank=True, null=True)),
                ('audience_count', models.IntegerField(blank=True, null=True)),
                ('tomatometer_top_critics_count', models.IntegerField(blank=True, null=True)),
                ('tomatometer_fresh_critics_count', models.IntegerField(blank=True, null=True)),
                ('tomatometer_rotten_critics_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
