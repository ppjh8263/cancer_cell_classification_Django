# Generated by Django 3.2.2 on 2021-05-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_id',
            field=models.CharField(default=False, max_length=20, unique=True),
        ),
    ]
