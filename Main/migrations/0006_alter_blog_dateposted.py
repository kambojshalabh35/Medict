# Generated by Django 4.0.2 on 2022-04-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_alter_blog_dateposted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dateposted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
