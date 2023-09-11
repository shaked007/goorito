# Generated by Django 4.2.4 on 2023-09-08 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gooritouser', '0002_alter_gooritouser_options_alter_gooritouser_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooritouser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='gooritouser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]