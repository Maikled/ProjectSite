# Generated by Django 3.2.8 on 2021-11-04 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0003_auto_20211105_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id_right_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Survey.answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id_survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Survey.survey'),
        ),
    ]