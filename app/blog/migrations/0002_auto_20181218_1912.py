# Generated by Django 2.1.4 on 2018-12-18 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publushed_date',
            new_name='published_date',
        ),
    ]
