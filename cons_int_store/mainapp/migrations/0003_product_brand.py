# Generated by Django 3.2.8 on 2023-05-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20230227_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='No Name', max_length=200, verbose_name='брэнд продукта'),
        ),
    ]