# Generated by Django 3.1.7 on 2021-04-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0016_auto_20210404_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, upload_to='db.sqlite3'),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('QUE', 'QUEEN'), ('KIN', 'KING'), ('YAC', 'AC')], max_length=3),
        ),
    ]
