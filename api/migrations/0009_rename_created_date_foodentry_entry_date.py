# Generated by Django 4.0.5 on 2022-06-30 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_user_foodentry_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodentry',
            old_name='created_date',
            new_name='entry_date',
        ),
    ]