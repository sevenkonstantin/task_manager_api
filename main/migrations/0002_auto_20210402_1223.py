# Generated by Django 3.1.2 on 2021-04-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='importance_type',
            field=models.IntegerField(choices=[(1, 'Высокая'), (2, 'Средняя'), (3, 'Низкая')], default=2, verbose_name='Важность'),
        ),
    ]
