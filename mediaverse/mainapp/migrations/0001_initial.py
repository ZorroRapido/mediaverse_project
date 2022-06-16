# Generated by Django 3.2.13 on 2022-06-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('isbn', models.CharField(max_length=64, null=True)),
                ('title', models.CharField(max_length=512)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=512)),
                ('image', models.ImageField(upload_to='images/books/<django.db.models.fields.IntegerField>/<django.db.models.fields.CharField>')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('genres', models.ManyToManyField(db_table='book_genre', related_name='books', to='mainapp.BookGenre')),
            ],
        ),
    ]
