# Generated by Django 3.2.8 on 2021-11-07 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
        ('Survey', '0005_auto_20211105_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answers', models.TextField(blank=True, null=True, verbose_name='right_answers')),
                ('wrong_answers', models.TextField(blank=True, null=True, verbose_name='right_answers')),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.survey')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.employee')),
            ],
        ),
    ]
