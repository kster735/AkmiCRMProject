# Generated by Django 4.1.5 on 2023-02-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicrm', '0002_remove_contact_contact_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_username',
        ),
        migrations.AddField(
            model_name='agent',
            name='agent_levelaccess',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
