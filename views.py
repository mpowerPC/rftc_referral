from rftc_referral.models import RFTCReferral
from rftc_referral.serializers import RFTCReferralSerializer
from rest_framework import viewsets

class AddReferralViewSet(viewsets.ModelViewSet):
    filter_fields = ('user', 'code',)

    serializer_class = RFTCReferralSerializer
    queryset = RFTCReferral.objects.all()

