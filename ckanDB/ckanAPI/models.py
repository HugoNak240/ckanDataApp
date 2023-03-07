from django.db import models

""" Created table model with fields from safe_to_swim_ """


class StS2020toCurrent(models.Model):
    analysis_date = models.TimeField(null=True)
    analyte = models.CharField(max_length=70, null=True)
    lab_agency = models.CharField(max_length=70, null=True)
    lab_batch = models.CharField(max_length=70, null=True)
    lab_sample_id = models.CharField(max_length=50, null=True)
    matrix_name = models.CharField(max_length=50, null=True)
    method_detection_limit = models.SmallIntegerField(null=True)
    method_name = models.CharField(max_length=70, null=True)
    program = models.CharField(max_length=70, null=True)
    project = models.CharField(max_length=250, null=True)
    result = models.BigIntegerField(null=True)
    reporting_limit = models.CharField(max_length=30, null=True)


