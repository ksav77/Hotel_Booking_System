# Generated by Django 3.2 on 2021-05-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Contactnumber',
            field=models.IntegerField(max_length=10),
        ),
    ]