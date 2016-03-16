from django.conf.urls import url, include
from rftc_referral import views as rftc_referral_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'add_referral', rftc_referral_views.AddReferralViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name="rftc_referral"),
]