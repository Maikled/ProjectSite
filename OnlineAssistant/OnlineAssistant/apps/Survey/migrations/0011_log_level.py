# Generated by Django 3.2.7 on 2021-11-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0010_question_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='level',
            field=models.IntegerField(null=True, verbose_name='level'),
        ),
    ]
