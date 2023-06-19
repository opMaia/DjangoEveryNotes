# Generated by Django 3.1.1 on 2021-02-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='firmness',
            field=models.CharField(choices=[('unspecified', 'Unspecified'), ('soft', 'Soft'), ('semi-soft', 'Semi-Soft'), ('semi-hard', 'Semi-Hard'), ('hard', 'Hard')], default='unspecified', max_length=20, verbose_name='Firmness'),
        ),
    ]
