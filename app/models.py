from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    
    
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Address(models.Model):
    addressid = models.IntegerField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Donetasks(models.Model):
    taskid = models.IntegerField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    postdate = models.DateField(db_column='PostDate', blank=True, null=True)  # Field name made lowercase.
    donedate = models.DateField(db_column='DoneDate', blank=True, null=True)  # Field name made lowercase.
    doer = models.ForeignKey('Student', models.DO_NOTHING, db_column='Doer', blank=True, null=True, related_name='donetasks_doer')  # Field name made lowercase.
    poster = models.ForeignKey('Student', models.DO_NOTHING, db_column='Poster', blank=True, null=True, related_name='donetasks_poster')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoneTasks'


class Hasaddress(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', primary_key=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID')  # Field name made lowercase.
    isprimaryaddress = models.CharField(db_column='isPrimaryAddress', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HasAddress'
        unique_together = (('studentid', 'addressid'),)


class Leaderboard(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', primary_key=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    inmonth = models.CharField(db_column='inMonth', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imageid = models.IntegerField(db_column='imageId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeaderBoard'


class Pendingtasks(models.Model):
    taskid = models.IntegerField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    poster = models.ForeignKey('Student', models.DO_NOTHING, db_column='Poster', blank=True, null=True, related_name='pendingtasks_poster')  # Field name made lowercase.
    postdate = models.DateField(db_column='PostDate', blank=True, null=True)  # Field name made lowercase.
    doer = models.ForeignKey('Student', models.DO_NOTHING, db_column='Doer', blank=True, null=True, related_name='pendingtasks_doer')  # Field name made lowercase.
    done = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PendingTasks'


class Perdaytasks(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', primary_key=True)  # Field name made lowercase.
    postnum = models.IntegerField(db_column='PostNum', blank=True, null=True)  # Field name made lowercase.
    optnum = models.IntegerField(db_column='OptNum', blank=True, null=True)  # Field name made lowercase.
    donenum = models.IntegerField(db_column='DoneNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerDayTasks'


class Reports(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', primary_key=True)  # Field name made lowercase.
    repdesc = models.CharField(db_column='repDesc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateissued = models.DateField(blank=True, null=True)
    kind = models.CharField(db_column='Kind', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reports'


class Routine(models.Model):
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    hostelite = models.CharField(db_column='Hostelite', max_length=3, blank=True, null=True)  # Field name made lowercase.
    allnighter = models.CharField(db_column='AllNighter', max_length=3, blank=True, null=True)  # Field name made lowercase.
    animefan = models.CharField(db_column='AnimeFan', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gamegeek = models.CharField(db_column='GameGeek', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Routine'


class University(models.Model):
    uniname = models.CharField(db_column='UniName', primary_key=True, max_length=60)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=20)  # Field name made lowercase.
    campuslocation = models.CharField(db_column='CampusLocation', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'University'
        unique_together = (('uniname', 'campus'),)


class Student(models.Model):
    studentid = models.IntegerField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=30)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', unique=True)  # Field name made lowercase.
    dp_name = models.CharField(db_column='DP_Name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    blacklist = models.CharField(db_column='Blacklist', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pic = models.CharField(db_column='Pic', max_length=200, blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    uniname = models.ForeignKey(University, models.DO_NOTHING, db_column='UniName', blank=True, null=True, related_name='students_uniname')  # Field name made lowercase.
    campus = models.ForeignKey(University, models.DO_NOTHING, db_column='Campus', blank=True, null=True, related_name='students_campus')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressId', blank=True, null=True)  # Field name made lowercase.
    refsid = models.ForeignKey('self', models.DO_NOTHING, db_column='refSid', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)