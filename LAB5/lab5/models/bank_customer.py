from models.personal_info import PersonalInfo
from models.bank_info import BankInfo

class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self) -> dict:
        """Return the bank details along with transaction history"""
        details = self.bank_details.__dict__
        details['transactions'] = self.bank_details.transaction_list(self.personal_info.account_number)
        return details
