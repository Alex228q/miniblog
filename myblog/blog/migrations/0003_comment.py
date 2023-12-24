# Generated by Django 5.0 on 2023-12-24 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text_comment', models.TextField(max_length=2000, verbose_name='Текст комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]