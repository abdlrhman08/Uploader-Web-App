from django.db import models

# Create your models here.

class Accounts(models.Model):
    type = models.IntegerField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.CharField(max_length=255, blank=True, null=True)
    battle_tag = models.CharField(max_length=20, blank=True, null=True)
    phonenum = models.CharField(max_length=15, blank=True, null=True)
    safe_um_user = models.CharField(max_length=30, blank=True, null=True)
    safe_um_pass = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    channelid = models.CharField(max_length=255, blank=True, null=True)
    finished = models.BooleanField()
    taken = models.BooleanField()
    name = models.CharField(max_length=40, blank=True, null=True)
    birthdate = models.CharField(max_length=12, blank=True, null=True)
    creation_date = models.CharField(max_length=12, blank=True, null=True)
    email_password = models.CharField(max_length=40, blank=True, null=True)
    finished_date = models.CharField(max_length=12, blank=True, null=True)
    hex_secret_key = models.CharField(max_length=41, blank=True, null=True)
    serial = models.CharField(max_length=14, blank=True, null=True)
    restore_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'
        unique_together = (('id', 'email'),)


    def __str__(self):
        return self.email

class Payments(models.Model):
    user = models.CharField(max_length=255)
    paymentdate = models.CharField(db_column='paymentDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentnum = models.CharField(db_column='paymentNum', max_length=15)  # Field name made lowercase.
    amount = models.IntegerField(blank=True, null=True)
    channelid = models.CharField(max_length=255, blank=True, null=True)
    payed = models.BooleanField()
    confirmed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'payments'