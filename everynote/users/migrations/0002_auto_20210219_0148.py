# Generated by Django 3.1.1 on 2021-02-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='soccer',
            field=models.CharField(blank=True, max_length=255, verbose_name='Soccer Team of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='Email of User'),
        ),
    ]