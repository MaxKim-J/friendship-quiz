# Generated by Django 2.0.13 on 2021-10-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizset',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
