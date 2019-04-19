from django.conf.urls import url
from .views import OfferView, Crawloffer

app_name = 'scrap'

urlpatterns = [
	url(r'^$', OfferView.as_view(), name='offerview'),
	url(r'^crawl_offers/$', Crawloffer.as_view(), name='crawl_offers'),
    ]