# Generated by Django 3.2.7 on 2021-12-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskMonitoring', '0004_remove_ipr_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipr',
            name='link',
            field=models.TextField(blank=True, null=True, verbose_name='link'),
        ),
    ]
