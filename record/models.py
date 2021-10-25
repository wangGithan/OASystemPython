# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WorkTime(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    work_begin = models.CharField(db_column='work_begin', max_length=30, blank=True, null=True)  # Field name made lowercase.
    work_end = models.CharField(db_column='work_end', max_length=30, blank=True, null=True)  # Field name made lowercase.
    total = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_time'
