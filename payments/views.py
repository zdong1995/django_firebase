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
    data = json.loads(request.body)
    customer_id = data.get('customer_id')

    if request.method == 'GET':

        try:
            response = stripe.Customer.retrieve(customer_id)
        except:
            message = "Customer not exists. Please try again."
            return JsonResponse({'message': message}, status=status.HTTP_404_NOT_FOUND)

        dict = {}

        dict["name"] = response["name"]
        dict["email"] = response["email"]
        dict["customer_id"] = response['id']
        dict["default_source"] = response["default_source"]
        if response.get("source"):
            dict["address"] = response["sources"]["data"][0]["owner"]["address"]

        return JsonResponse(dict, status=status.HTTP_200_OK)

    if request.method == 'POST':
        del data['customer_id']

        try:
            stripe.Customer.modify(customer_id, description=data.get('description'))
        except:
            message = "Customer not exists. Please try again."
            return JsonResponse({'message': message}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'message': "Update successfully!"}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            stripe.Customer.delete(customer_id)
        except:
            message = "Customer not exists. Please try again."
            return JsonResponse({'message': message}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'message': "Delete successfully!"}, status=status.HTTP_200_OK)


@csrf_exempt
def add_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_id = data.get('customer_id')
        card = data.get('card')
        owner = data.get('owner')

        # create source object
        created_source = stripe.Source.create(
            type='card',
            currency='usd',
            owner=owner,
            card=card
        )

        source_id = created_source['id']
        fingerprint = created_source.get('card').get('fingerprint')
        brand = created_source.get('card').get('brand')
        last4 = created_source.get('card').get('last4')

        # link created source to existed customer
        stripe.Customer.create_source(
            customer_id,
            source=source_id
        )

        return JsonResponse({'source_id': source_id, 'fingerprint': fingerprint,
                             'brand': brand, 'last4': last4}, status=status.HTTP_200_OK)


@csrf_exempt
def card(request):
    data = json.loads(request.body)
    customer_id = data.get('customer_id')
    source_id = data.get('source_id')

    if request.method == 'GET':
        response = stripe.Source.retrieve(source_id)

        return JsonResponse(response.get('card'), status=status.HTTP_200_OK)

    if request.method == 'POST':
        card = data.get('card')

        stripe.Source.modify(source_id, card=card)

        return JsonResponse({'message': "Update successfully!"}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        stripe.Customer.delete_source(customer_id, source_id)

        return JsonResponse({'message': "Delete successfully!"}, status=status.HTTP_200_OK)


@csrf_exempt
def list_cards(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        customer_id = data.get('customer_id')

        # retrieve customer data
        customer = stripe.Customer.retrieve(customer_id)

        # extract card information
        sources = customer.get("sources")

        # the key of sources pair is "data"
        response = {"Number of Cards": len(sources["data"])}

        i = 1

        for info in sources["data"]:
            card = info["card"]
            source_id = info['id']
            fingerprint = card['fingerprint']
            brand = card['brand']
            last4 = card['last4']

            cur_card = {'brand': brand, 'last4': last4,
                        'source_id': source_id,
                        'fingerprint': fingerprint
                        }

            response["card" + str(i)] = cur_card
            i += 1

        return JsonResponse(response, status=status.HTTP_200_OK)


@csrf_exempt
def default_card(request):
    data = json.loads(request.body)
    customer_id = data.get('customer_id')
    source_id = data.get('source_id')

    if request.method == 'POST':
        del data['customer_id']

        try:
            stripe.Customer.modify(customer_id, default_source=source_id)
        except:
            message = "Card not exists. Please try again."
            return JsonResponse({'message': message}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'message': "Default card set successfully!"}, status=status.HTTP_200_OK)


@csrf_exempt
def add_charge(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = data.get('amount')
        currency = data.get('currency')
        source = data.get('source_id')
        customer = data.get('customer_id')

        response = stripe.Charge.create(amount=int(amount), currency=currency,
                                        source=source, customer=customer)
        charge_id = response['id']

        return JsonResponse({'charge_id': charge_id}, status=status.HTTP_200_OK)


@csrf_exempt
def charge(request):
    data = json.loads(request.body)
    charge_id = data.get('charge_id')

    if request.method == 'GET':
        response = stripe.Charge.retrieve(charge_id)

        dict = {}

        dict["amount"] = response["amount"]
        dict["currency"] = response["currency"]
        dict["customer"] = response["customer"]
        dict["status"] = response["status"]
        card = response["payment_method_details"]["card"]
        dict["payment_method"] = {"card_type": card["brand"], "last 4": card["last4"]}

        return JsonResponse(dict, status=status.HTTP_200_OK)


@csrf_exempt
def transaction(request):
    pass


@csrf_exempt
def add_refund(request):
    pass


@csrf_exempt
def refund(request):
    pass