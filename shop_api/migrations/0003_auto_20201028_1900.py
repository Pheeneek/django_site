# Generated by Django 3.1.2 on 2020-10-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('fruits', 'fruits'), ('vegetables', 'vegetables')], max_length=20, null=True),
        ),
    ]
