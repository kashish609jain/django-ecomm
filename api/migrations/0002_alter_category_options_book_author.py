# Generated by Django 5.0.1 on 2024-01-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Kashish jain', max_length=100),
        ),
    ]
