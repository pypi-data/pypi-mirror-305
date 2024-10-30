from urllib.parse import urlencode
import webbrowser  # For opening the URL in a browser
from ..Contract.GatewayInterface import GatewayInterface
from ..Enums.PaymentURL import PaymentURL
from ..Utils.Encryptions import Encryptions


class FuturaPay(GatewayInterface):
    def __init__(self, merchant_key: str, api_key: str, site_id: str):
        self.merchant_key = merchant_key
        self.api_key = api_key
        self.site_id = site_id
        self.environment = "sandbox"
        self.payment_type = "deposit"

    def set_env(self, environment: str):
        self.environment = environment

    def set_type(self, payment_type: str):
        self.payment_type = payment_type

    def initialize(self, payment_payload: dict):
        payment_payload["merchant_key"] = self.merchant_key
        payment_payload["api_key"] = self.api_key
        payment_payload["site_id"] = self.site_id

        finalPayload = Encryptions.make(
            merchant_key=self.merchant_key,
            api_key=self.api_key,
            site_id=self.site_id,
            payload=payment_payload,
        )
        query_string = urlencode(finalPayload)

        # Create the full payment URL
        payment_url = self.get_payment_url()

        payment_url = payment_url + query_string

        # Open the payment URL in the default web browser
        webbrowser.open(payment_url)

    def get_payment_url(self):
        if self.environment == "live":
            url = PaymentURL.LIVE_DEPOSIT_URL.value
            if self.payment_type == "withdraw":
                url = PaymentURL.LIVE_WITHDRAWAL_URL.value
        else:
            url = PaymentURL.STAGE_DEPOSIT_URL.value
            if self.payment_type == "withdraw":
                url = PaymentURL.STAGE_WITHDRAWAL_URL.value
        return url

    def get_payment(self, hashtoken: str):
        pass

    def get_status(self, hashtoken: str):
        pass
