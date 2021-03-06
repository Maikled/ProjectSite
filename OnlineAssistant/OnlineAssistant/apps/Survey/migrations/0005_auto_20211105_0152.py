# Generated by Django 3.2.8 on 2021-11-04 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0004_auto_20211105_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id_right_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id_survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.survey'),
        ),
        migrations.AlterField(
            model_name='question',
            name='material_link',
            field=models.TextField(blank=True, null=True, verbose_name='materials_link'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_topic',
            field=models.TextField(blank=True, null=True, verbose_name='question_topic'),
        ),
    ]
