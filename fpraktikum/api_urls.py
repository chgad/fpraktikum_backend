from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from fpraktikum.api_views import *


router = SimpleRouter()
router.register(r'user_registrant', UserRegistrantViewset)
router.register(r'user_partner', UserPartnerViewset)
router.register(r'waitlist', WaitlistView)

app_name = "api"
urlpatterns = [
    url(r'^registration/', RegistrationView.as_view(), name=RegistrationView.name),
    url(r'^user/(?P<user_login>.+)/', UserCheckView.as_view(), name=UserCheckView.name),
    # url(r'^register/{pk}/', SetRegistrationView.as_view(), name=SetRegistrationView.name),
    url(r'^check_partner/', CheckPartnerView.as_view(), name=CheckPartnerView.name),
    # url(r'^accept/', AcceptDeclinePartnershipView.as_view(), name=AcceptDeclinePartnershipView.name),
    # url(r'^waitlist/', WaitlistView.as_view(), name=WaitlistView.name),
    url(r'test/', TestIlDbView.as_view()),
]

urlpatterns += router.urls