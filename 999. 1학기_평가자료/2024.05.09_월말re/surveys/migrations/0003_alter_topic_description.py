# Generated by Django 4.2.11 on 2024-05-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_question_good_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
