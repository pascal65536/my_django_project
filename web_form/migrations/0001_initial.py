# Generated by Django 3.1.3 on 2020-11-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголвок статьи ')),
                ('user_name', models.CharField(max_length=30, verbose_name='Имя пользователя ')),
                ('text', models.TextField(verbose_name='Текст ')),
                ('date_send', models.DateField(auto_now=True)),
            ],
        ),
    ]