# Generated by Django 3.2.9 on 2021-12-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
