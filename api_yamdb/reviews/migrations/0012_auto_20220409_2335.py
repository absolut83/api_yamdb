# Generated by Django 2.2.16 on 2022-04-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20220408_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('id',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст отзыва'),
        ),
    ]
