class CreditCardDecorator:
    def __init__(self, credit_card):
        self._credit_card = credit_card

    def give_details(self) -> dict:
        return self._credit_card.give_details()
