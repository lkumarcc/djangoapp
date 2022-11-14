# Generated by Django 4.1.2 on 2022-11-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_addlistings_city_addlistings_price_addlistings_rooms_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addListForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.IntegerField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('rooms', models.IntegerField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
