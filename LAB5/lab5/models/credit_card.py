import hashlib

class CreditCard:
    def __init__(self, client: str, account_number: str, credit_limit: float, grace_period: int, cvv: str):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = None
        self.cvv = cvv  # setter and getter for cvv will call encrypt/decrypt

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, value: str):
        self.encrypt(value)

    def encrypt(self, value: str):
        """Hash the CVV value"""
        self._cvv = hashlib.sha256(value.encode()).hexdigest()

    def decrypt(self):
        """Decrypt would be not possible for hashed data, but we can just return the hash"""
        return self._cvv

    def give_details(self) -> dict:
        """Return details of the credit card as a dictionary"""
        return {
            'client': self.client,
            'account_number': self.account_number,
            'credit_limit': self.credit_limit,
            'grace_period': self.grace_period,
            'cvv': self.decrypt(),
        }
