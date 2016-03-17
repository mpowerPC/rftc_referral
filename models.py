from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RFTCReferral(models.Model):
    user = models.CharField(max_length=100)
    code = models.CharField(max_length=25)

    class Meta:
        db_table = "rftc_referrals"
        unique_together = ("user", "code")
        app_label = "rftc_referral"
