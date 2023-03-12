# Generated by Django 4.1.2 on 2023-03-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_rename_images_allinformation_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allinformation',
            name='aircond',
        ),
        migrations.RemoveField(
            model_name='allinformation',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='allinformation',
            name='heating',
        ),
        migrations.RemoveField(
            model_name='allinformation',
            name='internet',
        ),
        migrations.RemoveField(
            model_name='allinformation',
            name='size',
        ),
        migrations.RemoveField(
            model_name='allinformation',
            name='streamingservices',
        ),
        migrations.AddField(
            model_name='allinformation',
            name='state',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]