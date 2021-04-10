# Generated by Django 3.1.7 on 2021-04-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0005_auto_20210406_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC'), ('KIN', 'KING'), ('NAC', 'NON-AC'), ('QUE', 'QUEEN')], max_length=3),
        ),
    ]
