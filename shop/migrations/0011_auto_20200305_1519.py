# Generated by Django 3.0.3 on 2020-03-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adress',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='summ',
            field=models.IntegerField(),
        ),
    ]
