# Generated by Django 5.0.2 on 2024-03-30 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_products_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]