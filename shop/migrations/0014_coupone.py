# Generated by Django 3.1.1 on 2020-10-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_cart_create_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('value', models.IntegerField()),
                ('min_coast', models.IntegerField()),
            ],
        ),
    ]
