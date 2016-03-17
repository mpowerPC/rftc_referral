from rftc_referral.models import RFTCReferral
from rftc_referral.serializers import RFTCReferralSerializer
from rest_framework import viewsets
from django.http import HttpResponseRedirect
import random

class AddReferralViewSet(viewsets.ModelViewSet):
    filter_fields = ('user', 'code',)

    serializer_class = RFTCReferralSerializer
    queryset = RFTCReferral.objects.all()


def RandomReferral(request):
    referral_url = "https://robertsspaceindustries.com/enlist?referral="
    random.seed()
    winner_index = random.randint(1, RFTCReferral.objects.count())
    winner = RFTCReferral.objects.get(id=winner_index).code

    return HttpResponseRedirect(referral_url + winner)
