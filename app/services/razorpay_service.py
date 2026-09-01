import os
import razorpay

from dotenv import load_dotenv

load_dotenv()


RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")


if not RAZORPAY_KEY_ID or not RAZORPAY_KEY_SECRET:
    raise RuntimeError(
        "RAZORPAY_KEY_ID or RAZORPAY_KEY_SECRET is missing"
    )


client = razorpay.Client(
    auth=(
        RAZORPAY_KEY_ID,
        RAZORPAY_KEY_SECRET
    )
)


def create_razorpay_order(
    amount_paise: int,
    receipt: str,
    notes: dict | None = None
):
    data = {
        "amount": amount_paise,
        "currency": "INR",
        "receipt": receipt,
    }

    if notes:
        data["notes"] = notes

    return client.order.create(data)


def verify_payment_signature(
    razorpay_order_id: str,
    razorpay_payment_id: str,
    razorpay_signature: str
):
    client.utility.verify_payment_signature({
        "razorpay_order_id": razorpay_order_id,
        "razorpay_payment_id": razorpay_payment_id,
        "razorpay_signature": razorpay_signature,
    })

    return True