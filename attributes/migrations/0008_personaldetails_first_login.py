# Generated by Django 2.1 on 2020-02-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0007_auto_20200207_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
    ]
