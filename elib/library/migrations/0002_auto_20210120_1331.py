# Generated by Django 3.1.4 on 2021-01-20 05:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(max_length=100)),
                ('yearPublished', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('bookFile', models.FileField(blank=True, null=True, upload_to='books')),
                ('bookImage', models.ImageField(blank=True, upload_to='covers')),
                ('isbn', models.IntegerField(blank=True)),
                ('pages', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('featured', models.BooleanField()),
                ('bookAuthor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.AddField(
            model_name='book',
            name='bookCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.category'),
        ),
    ]
