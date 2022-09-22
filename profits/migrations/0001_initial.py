# Generated by Django 4.1.1 on 2022-09-17 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ruya', models.CharField(blank=True, max_length=12, null=True)),
                ('karma', models.CharField(blank=True, max_length=12, null=True)),
                ('adil', models.CharField(blank=True, max_length=12, null=True)),
                ('taim', models.CharField(blank=True, max_length=12, null=True)),
                ('efix', models.CharField(blank=True, max_length=12, null=True)),
                ('ashab', models.CharField(blank=True, max_length=12, null=True)),
                ('turkpin', models.CharField(blank=True, max_length=12, null=True)),
                ('razer', models.CharField(blank=True, max_length=12, null=True)),
                ('alfurat', models.CharField(blank=True, max_length=12, null=True)),
                ('musaab', models.CharField(blank=True, max_length=12, null=True)),
                ('abutalal', models.CharField(blank=True, max_length=12, null=True)),
                ('kuvyet', models.CharField(blank=True, max_length=12, null=True)),
                ('ziraat', models.CharField(blank=True, max_length=12, null=True)),
                ('codes', models.CharField(blank=True, max_length=12, null=True)),
                ('bayilar', models.CharField(blank=True, max_length=12, null=True)),
                ('total', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]