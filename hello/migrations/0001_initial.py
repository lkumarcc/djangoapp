# Generated by Django 4.1.2 on 2023-03-20 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addListings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='allinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=22, null=True)),
                ('hometype', models.CharField(blank=True, max_length=100, null=True)),
                ('monthlyprice', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('securitydeposit', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('numbertenants', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('beds', models.IntegerField(blank=True, null=True)),
                ('addrentinfo', models.CharField(blank=True, max_length=300, null=True)),
                ('parking', models.CharField(blank=True, max_length=4, null=True)),
                ('pets', models.CharField(blank=True, max_length=4, null=True)),
                ('laundry', models.CharField(blank=True, max_length=20, null=True)),
                ('addamenityinfo', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, default='images/image_coming_soon.png', null=True, upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
        migrations.CreateModel(
            name='Shome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hometype', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('addy', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('beds', models.IntegerField(blank=True, null=True)),
                ('bath', models.DecimalField(blank=True, decimal_places=1, max_digits=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, max_length=12, null=True)),
                ('firstname', models.CharField(blank=True, max_length=12, null=True)),
                ('lastname', models.CharField(blank=True, max_length=12, null=True)),
                ('username', models.CharField(blank=True, max_length=12, null=True)),
                ('password', models.CharField(blank=True, max_length=12, null=True)),
                ('school', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.allinformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
