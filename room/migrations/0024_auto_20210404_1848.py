# Generated by Django 3.1.7 on 2021-04-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0023_auto_20210404_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='caption',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('QUE', 'QUEEN'), ('KIN', 'KING'), ('NAC', 'NON-AC'), ('YAC', 'AC')], max_length=3),
        ),
    ]
