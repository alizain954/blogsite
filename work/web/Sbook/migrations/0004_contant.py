# Generated by Django 3.2.1 on 2021-05-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sbook', '0003_coment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
    ]
