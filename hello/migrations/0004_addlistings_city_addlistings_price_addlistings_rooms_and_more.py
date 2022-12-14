# Generated by Django 4.1.2 on 2022-11-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_addlistings'),
    ]

    operations = [
        migrations.AddField(
            model_name='addlistings',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='addlistings',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='addlistings',
            name='rooms',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='addlistings',
            name='zip',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='addlistings',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
