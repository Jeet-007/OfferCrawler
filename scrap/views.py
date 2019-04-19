from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import AllowAny
from .models import Offer
from .utils import crawl_offers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

class OfferView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        page = request.GET.get('page_no')
        product_type_value = request.GET.get('product_category')
        coupon_type_value = request.GET.get('coupon_type')
        all_offers = Offer.objects.all().order_by('-id')
            
        product_set = set()
        coupon_type_set = set()
        for offer in all_offers:
            product_set.add(offer.product)
            coupon_type_set.add(offer.offer_value)

        if product_type_value and coupon_type_value:
            all_offers = all_offers.filter(product=product_type_value, offer_value=coupon_type_value).order_by('-id')
        elif product_type_value:
            all_offers = all_offers.filter(product=product_type_value).order_by('-id')
        elif coupon_type_value:
            all_offers = all_offers.filter(offer_value=coupon_type_value).order_by('-id')

        paginator = Paginator(all_offers, 25)
        if not page:
            page = 1
        try:
            all_offers = paginator.page(page)
        except:
            page = 1
            all_offers = paginator.page(page)
        return render(request, "scrap/offers.html", {"offers":all_offers, "product_set": product_set, "coupon_type_set": coupon_type_set, "product_type_value": product_type_value, "coupon_type_value": coupon_type_value})


class Crawloffer(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        _ = crawl_offers()
        offer_objects = list()
        # _.append({"offer_id":"offer_id", "amount":"amount", "offer_value":"offer_value", "verified_on": "verified_on", "product":"product", "description":"description", "offer_code":"offer_code"})
        _.reverse()
        for offer in _:
            offer_objects.append(Offer(coupon_id=offer['offer_id'], amount=offer['amount'], offer_value=offer['offer_value'], verified_on=offer['verified_on'], product=offer['product'], description=offer['description'], code=offer['offer_code']))
        # try:
        Offer.objects.bulk_create(offer_objects, ignore_conflicts=True)
        return redirect("scrap:offerview")