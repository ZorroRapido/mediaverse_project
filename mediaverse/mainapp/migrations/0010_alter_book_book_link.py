# Generated by Django 3.2.13 on 2022-06-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_book_book_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_link',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Ссылка на livelib'),
        ),
    ]
