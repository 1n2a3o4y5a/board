# Generated by Django 3.0.8 on 2020-09-08 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='auther',
            new_name='author',
        ),
    ]
