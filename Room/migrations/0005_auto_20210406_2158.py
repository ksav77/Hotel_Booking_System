# Generated by Django 3.1.7 on 2021-04-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0004_auto_20210406_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('KIN', 'KING'), ('QUE', 'QUEEN'), ('YAC', 'AC'), ('NAC', 'NON-AC')], max_length=3),
        ),
    ]
