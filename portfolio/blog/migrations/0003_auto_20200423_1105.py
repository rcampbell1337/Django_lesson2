# Generated by Django 3.0.4 on 2020-04-23 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_announcements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='announcements',
            new_name='announcement',
        ),
    ]