# Generated by Django 3.2.7 on 2021-12-14 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskMonitoring', '0003_ipr_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipr',
            name='link',
        ),
    ]