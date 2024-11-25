from models.credit_card import CreditCard
from models.bank_info import BankInfo
from models.bank_customer import BankCustomer
from models.personal_info import PersonalInfo
from decorators.golden_credit_card import GoldenCreditCard
from decorators.corporate_credit_card import CorporateCreditCard

# Creating a CreditCard instance
card = CreditCard(client="John Doe", account_number="123456789", credit_limit=10000, grace_period=30, cvv="123")

# Creating a BankInfo instance
bank_info = BankInfo(bank_name="Bank ABC", holder_name="John Doe", account_numbers=[card.account_number], credit_history={})

# Creating PersonalInfo
personal_info = PersonalInfo(client_name="John Doe", account_number=card.account_number)

# Creating a BankCustomer (Adapter)
customer = BankCustomer(personal_info, bank_info)

# Printing details of the customer
print(customer.give_details())

# Applying Decorators
golden_card = GoldenCreditCard(card)
print(golden_card.give_details())

corporate_card = CorporateCreditCard(card)
print(corporate_card.give_details())
