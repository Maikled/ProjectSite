# Generated by Django 3.2.7 on 2021-12-13 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0012_alter_question_text_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Survey.question'),
        ),
    ]
