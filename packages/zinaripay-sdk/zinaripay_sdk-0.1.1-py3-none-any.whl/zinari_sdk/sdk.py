import requests

class ZinariPaySDK:
    BASE_URL = "https://openapi.zinari.io/v1/"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _post(self, endpoint, data):
        response = requests.post(self.BASE_URL + endpoint, json=data, headers=self.headers)
        return response.json()

    def _get(self, endpoint):
        response = requests.get(self.BASE_URL + endpoint, headers=self.headers)
        return response.json()

    def get_payment_link(self, fiat_amount, notification_email, details=None, success_redirect_uri=None, failure_redirect_uri=None):
        data = {
            "fiatAmount": fiat_amount,
            "notificationEmailAddress": notification_email,
            "details": details,
            "successRedirectUri": success_redirect_uri,
            "failureRedirectUri": failure_redirect_uri
        }
        return self._post("paylink", data)

    def create_transaction(self, cryptocurrency, fiat_amount, notification_email, details=None):
        data = {
            "cryptocurrency": cryptocurrency,
            "fiatAmount": fiat_amount,
            "notificationEmailAddress": notification_email,
            "details": details
        }
        return self._post("create-transaction", data)

    def get_transaction_by_id(self, transaction_id):
        return self._get(f"transaction/{transaction_id}")

    def list_transactions(self, mode="prod"):
        endpoint = "transactions" if mode == "prod" else "transactions/dev"
        return self._get(endpoint)

    def get_wallets(self):
        return self._get("wallets")

    def get_wallet_by_id(self, wallet_id):
        return self._get(f"wallet/{wallet_id}")

    def withdraw_from_wallet(self, wallet_id, amount, address):
        data = {
            "amount": amount,
            "address": address
        }
        return self._post(f"withdraw/{wallet_id}", data)

    def get_exchange_rate(self, from_currency, to_currency):
        endpoint = f"exchange-rate?from={from_currency}&to={to_currency}"
        return self._get(endpoint)