# Generated by Django 3.1.4 on 2021-01-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210122_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookDescription',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
    ]