# Generated by Django 3.2.3 on 2021-05-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20210515_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='product',
        ),
    ]