# Generated by Django 4.2.5 on 2023-10-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='slug',
        ),
    ]
