# Generated by Django 3.2.2 on 2021-05-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=False, max_length=20, unique=True)),
                ('user_pw', models.CharField(default=False, max_length=20)),
            ],
            options={
                'verbose_name': '로그인 테이블',
                'db_table': 'login_user',
            },
        ),
    ]
