# Generated by Django 4.0.2 on 2022-04-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_alter_blog_dateposted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
