# Generated by Django 4.2.5 on 2023-11-01 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='timeStamp',
            new_name='timestamp',
        ),
    ]