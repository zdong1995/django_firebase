import stripe
import json

from rest_framework import status
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = 'sk_test_51H5tgoB5uFLcZ9OT4rZWkLsW2VIG6mcLW2wb8sIuk2amm5who22JABbw44RQar1q3GSISv9aWKxPtManvrTG0eKd007Scymw5M'


@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        name = data.get("name")

        try:
            response = stripe.Customer.create(name=name, email=email, )
        except:
            message = "Customer information has already existed. Please try again."
            return JsonResponse({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        customer_id = response['id']
        return JsonResponse({'customer_id': customer_id}, status=status.HTTP_201_CREATED)


@csrf_exempt
def customers(request):
    pass


@csrf_exempt
def add_card(request):
    pass


@csrf_exempt
def card(request):
    pass


@csrf_exempt
def list_cards(request):
    pass


@csrf_exempt
def default_card(request):
    pass


@csrf_exempt
def add_charge(request):
    pass


@csrf_exempt
def charge(request):
    pass


@csrf_exempt
def transaction(request):
    pass


@csrf_exempt
def add_refund(request):
    pass


@csrf_exempt
def refund(request):
    pass