# Generated by Django 4.1.5 on 2023-02-12 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minicrm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_password',
        ),
    ]