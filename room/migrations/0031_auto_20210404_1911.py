# Generated by Django 3.1.7 on 2021-04-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0030_auto_20210404_1907'),
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
            field=models.CharField(choices=[('QUE', 'QUEEN'), ('KIN', 'KING'), ('NAC', 'NON-AC'), ('YAC', 'AC')], max_length=3),
        ),
    ]
