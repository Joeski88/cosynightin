# Generated by Django 4.2.16 on 2024-10-08 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cniapp', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on']},
        ),
    ]