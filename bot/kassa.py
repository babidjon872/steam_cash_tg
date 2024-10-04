import json
from decouple import config
from pprint import pprint
from yookassa import Configuration,Payment
import asyncio


Configuration.account_id = config("SHOP_ID")
Configuration.secret_key = config("SECRET_KEY")


async def create_payment(description, value):
	payment = Payment.create({
    "amount": {
        "value": value,
        "currency": "RUB"
    },
    "payment_method_data": {
        "type": "bank_card"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://t.me/SteamWalletReplenishmentBot"
    },
    "capture": True,
    "description": f"{description}"
	})
	return json.loads(payment.json())


async def check_payment(payment_id):
	payment = json.loads(Payment.find_one(payment_id).json())
	return True if payment["status"] == "succeeded" else False


# json response 
# {'amount': {'currency': 'RUB', 'value': '100.00'},
#  'confirmation': {'confirmation_url': 'https://yoomoney.ru/checkout/payments/v2/contract?orderId=2e8e8625-000f-5000-a000-1c3eada4472e',
#                   'return_url': 'урл редиректа',
#                   'type': 'redirect'},
#  'created_at': '2024-10-01T22:06:29.083Z',
#  'description': '1',
#  'id': '2e8e8625-000f-5000-a000-1c3eada4472e',
#  'metadata': {'cms_name': 'yookassa_sdk_python'},
#  'paid': False,
#  'payment_method': {'id': '2e8e8625-000f-5000-a000-1c3eada4472e',
#                     'saved': False,
#                     'type': 'bank_card'},
#  'recipient': {'account_id': '467837', 'gateway_id': '2323744'},
#  'refundable': False,
#  'status': 'pending',
#  'test': True}


# pprint(create_payment(100, "1"))