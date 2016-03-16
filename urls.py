from django.conf.urls import url, include
from rftc_referral import views as rftc_referral_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'add_referral', rftc_referral_views.AddReferralViewSet)

# views no longer in use
# router.register(r'ttrwindow', data_collector_views.TtrWindowViewSet)
# router.register(r'ttridle', data_collector_views.TtrIdleViewSet)
# router.register(r'album', data_collector_views.AlbumViewSet)
urlpatterns = [
    url(r'^', include(router.urls), name="rftc_referral"),
]