# Generated by Django 4.2.16 on 2024-10-30 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pxcp', '0002_remove_item_description_item_link_alter_item_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
