# Generated by Django 4.1.1 on 2022-09-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0002_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='costumer',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dept',
            name='note',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]