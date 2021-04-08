# Generated by Django 3.1.7 on 2021-04-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0032_auto_20210404_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=3),
        ),
    ]
