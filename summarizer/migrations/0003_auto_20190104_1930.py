# Generated by Django 2.1.4 on 2019-01-04 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0002_summarizer_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summarizer',
            name='email',
        ),
        migrations.AddField(
            model_name='summarizer',
            name='title',
            field=models.CharField(default='Old', max_length=50),
        ),
        migrations.AlterField(
            model_name='summarizer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
