# Generated by Django 4.0 on 2022-01-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_userextension_favorites_alter_userextension_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]