# Generated by Django 4.2.4 on 2023-08-16 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news2', '0002_rename_category_category2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='News2',
        ),
    ]