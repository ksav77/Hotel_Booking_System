# Generated by Django 3.2 on 2021-05-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0009_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15)),
                ('room', models.CharField(max_length=30)),
                ('checkin', models.CharField(max_length=30)),
                ('checkout', models.CharField(max_length=30)),
            ],
        ),
    ]
