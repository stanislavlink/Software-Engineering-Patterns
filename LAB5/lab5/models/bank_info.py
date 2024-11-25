from typing import List, Dict

class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, account_numbers: List[str], credit_history: Dict):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.account_numbers = account_numbers
        self.credit_history = credit_history

    def transaction_list(self, account_number: str) -> List[str]:
        """An arbitrary implementation of transaction list"""
        return ["Transaction 1", "Transaction 2", "Transaction 3"]
