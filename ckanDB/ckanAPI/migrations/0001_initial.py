# Generated by Django 4.0.4 on 2023-02-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StS2020toCurrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_date', models.TimeField()),
                ('analyte', models.CharField(max_length=70)),
                ('lab_agency', models.CharField(max_length=70)),
                ('lab_batch', models.CharField(max_length=70)),
                ('lab_sample_id', models.CharField(max_length=50)),
                ('matrix_name', models.CharField(max_length=50)),
                ('method_name', models.CharField(max_length=70)),
                ('program', models.CharField(max_length=70)),
            ],
        ),
    ]