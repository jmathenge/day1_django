# Generated by Django 4.1.1 on 2022-09-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='town',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
