# Generated by Django 5.0.6 on 2024-06-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_authorprofile_user_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='user_github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
