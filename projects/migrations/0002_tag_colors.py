# Generated by Django 2.1.2 on 2018-11-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='colors',
            field=models.CharField(blank=True, default=None, max_length=10, verbose_name='Colour (HEX with #)'),
        ),
    ]
