# Generated by Django 4.1.6 on 2023-03-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0011_alter_profile_bio_alter_profile_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/profilepics/default_profile_pic.jpg', max_length=500, null=True, upload_to='images/profilepics/'),
        ),
    ]
