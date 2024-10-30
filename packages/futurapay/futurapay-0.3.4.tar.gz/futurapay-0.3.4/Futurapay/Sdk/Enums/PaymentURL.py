from enum import Enum


class PaymentURL(Enum):
    STAGE_DEPOSIT_URL = "https://stage-payment-widget.futurapay.com/widget/deposit/?"
    STAGE_WITHDRAWAL_URL = "https://stage-payment-widget.futurapay.com/widget/withdrawal/?"
    LIVE_DEPOSIT_URL = "https://payment-widget.futurapay.com/widget/deposit/?"
    LIVE_WITHDRAWAL_URL = "https://payment-widget.futurapay.com/widget/withdrawal/?"
