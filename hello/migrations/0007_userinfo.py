# Generated by Django 4.1.2 on 2022-12-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_addressinformation_amenityinfo_rentinformation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfirst', models.CharField(blank=True, max_length=12, null=True)),
                ('userlast', models.CharField(blank=True, max_length=12, null=True)),
                ('username', models.CharField(blank=True, max_length=12, null=True)),
                ('userpass', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
