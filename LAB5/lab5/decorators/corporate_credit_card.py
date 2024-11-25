from decorators.credit_card_decorator import CreditCardDecorator

class CorporateCreditCard(CreditCardDecorator):
    def __init__(self, credit_card):
        super().__init__(credit_card)

    def give_details(self) -> dict:
        details = super().give_details()
        details['type'] = 'Corporate Credit Card'
        return details
