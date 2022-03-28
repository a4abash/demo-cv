# Generated by Django 2.1 on 2020-01-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0005_auto_20200118_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='objective',
            field=models.TextField(default='hi', help_text='About Yourself'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
