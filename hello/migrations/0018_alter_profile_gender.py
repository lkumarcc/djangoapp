# Generated by Django 4.1.6 on 2023-04-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]