# Generated by Django 3.2.3 on 2021-05-30 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_user_post_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='user',
        ),
    ]