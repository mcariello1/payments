
from payments_processing import PaymentsProcessing
from payments_processing import Client


class Test_Payments_Processing:


    def test_deposit_and_withdrawal_no_disputes():
        """Does two withdrawals and two deposits"""
        payments_processing = PaymentsProcessing('tests/deposit_and_withdrawal_no_disputes.csv')
        string = payments_processing.process_transactions()
        print(string)
        assert string == "client, available, held, total, locked\n1,0.0,0,0.0,False\n1,0.0,0,0.0,False"


    def deposit_and_withdrawal_insufficient_funds(self):
        """Deposits and tries to withdrawal too much"""
        pass

    def deposit_dispute(self):
        """
        Deposits money then dispute opens against it
        """
        pass

    def withdrawal_dispute(self):
        """Withdrawal money and dispute transaction"""
        pass

    def resolve_disputes(self):
        """Resolve both a withdrawal and a deposit dispute """
        pass


    def chargeback_dispute(self):
        """Chargeback a dispute"""
        pass

    def chargeback_dispute_transaction_frozen(self):
        """"chargeback a dispute and validate that further transactions are disabled"""
        pass

    def multiple_disputes_charged_back(self):
        """Have multiple client dispute charges"""

        pass

    def multiple_disputes_with_withdraw_rejection(self):
        """have multiple disputes with a withdrawal rejection due to disputed money"""
        pass





