# Generated by Django 4.0.2 on 2022-04-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('metadesc', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('thumbimg', models.ImageField(blank=True, null=True, upload_to='blogs/thumbnail')),
                ('featureimg', models.ImageField(blank=True, null=True, upload_to='blogs/')),
            ],
        ),
    ]
