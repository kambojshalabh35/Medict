# Generated by Django 4.0.2 on 2022-04-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='metadesc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
