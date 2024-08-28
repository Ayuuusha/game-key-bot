from yookassa import Payment
from yookassa.domain.request import PaymentRequest
import uuid


async def create_payment(amount,description,currency='RUB'):
    payment = Payment.create(
        {
            'amount': {
                'value': str(amount),
                'currency': currency
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': 'https://webhook.site/a4d34b82-a64d-4367-aabe-22468352b7c0'
            },
            "capture": True,
                "description": description,
                "metadata": {
                'order_id': str(uuid.uuid4())
        },
        })
    
    return payment


async def get_payment(payment_id):
    payment = Payment.find_one(payment_id)
    return payment.status


