# Generated by Django 4.2.2 on 2023-06-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
