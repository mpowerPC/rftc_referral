from rest_framework import serializers
from rftc_referral.models import RFTCReferral


class RFTCReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFTCReferral
        fields = ('user', 'code',)
