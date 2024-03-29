# Generated by Django 4.0.4 on 2023-02-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckanAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='analysis_date',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='analyte',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='lab_agency',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='lab_batch',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='lab_sample_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='matrix_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='method_name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sts2020tocurrent',
            name='program',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
