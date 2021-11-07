
from payment_engine import PaymentsProcessing
from payment_engine import Client


class Test_Payments_Processing:

    def test_deposit_and_withdrawal_no_disputes(self):
        """Does two withdrawals and two deposits"""
        payments_processing = PaymentsProcessing('tests/deposit_and_withdrawal_no_disputes.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,0,0.0,False" == parsed_response[1]
        assert "2,0.0,0,0.0,False" == parsed_response[2]
        print('Success')


    def test_deposit_and_withdrawal_insufficient_funds(self):
        """Deposits and tries to withdrawal too much"""
        payments_processing = PaymentsProcessing('tests/deposit_and_withdrawal_insufficient_funds.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,5.0,0,5.0,False" == parsed_response[1]
        assert "2,5.0,0,5.0,False" == parsed_response[2]
        print('Success')

    def test_deposit_dispute(self):
        """
        Deposits money then dispute opens against it
        """
        payments_processing = PaymentsProcessing('tests/deposit_and_dispute.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,5.0,5.0,False" == parsed_response[1]
        print('Success')
        

    def test_withdrawal_dispute(self):
        """Withdrawal money and dispute transaction"""
        payments_processing = PaymentsProcessing('tests/withdrawal_dispute.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,5.0,5.0,False" == parsed_response[1]
        print('Success')
        

    def test_resolve_disputes(self):
        """Resolve both a withdrawal and a deposit dispute """
        payments_processing = PaymentsProcessing('tests/resolve_disputes.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,5.0,0.0,5.0,False" == parsed_response[1]
        print('Success')
        


    def test_chargeback_dispute(self):
        """Chargeback a dispute"""
        payments_processing = PaymentsProcessing('tests/chargeback_disputes.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,0.0,0.0,True" == parsed_response[1]
        assert "2,-5.0,0.0,-5.0,True" == parsed_response[2]
        print('Success')
        

    def test_chargeback_dispute_transaction_frozen(self):
        """"chargeback a dispute and validate that further transactions are disabled"""
        payments_processing = PaymentsProcessing('tests/chargeback_disputes_frozen.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,0.0,0.0,True" == parsed_response[1]
        assert "2,-5.0,0.0,-5.0,True" == parsed_response[2]
        print('Success')
        

    def test_multiple_disputes_charged_back_withdrawal(self):
        """Have multiple client dispute charges"""
        payments_processing = PaymentsProcessing('tests/multiple_disputes_chargeback_withdrawal_denial.csv')
        string_value = payments_processing.process_transactions()
        parsed_response = string_value.split('\n')
        assert "client, available, held, total, locked" == parsed_response[0]
        assert "1,0.0,5.0,5.0,True" == parsed_response[1]
        assert "2,-15.0,15.0,0.0,False" == parsed_response[2]
        print('Success')

     
if __name__ == "__main__":
    testing = Test_Payments_Processing()
    testing.test_deposit_and_withdrawal_no_disputes()
    testing.test_deposit_and_withdrawal_insufficient_funds()
    testing.test_deposit_dispute()
    testing.test_withdrawal_dispute()
    testing.test_resolve_disputes()
    testing.test_chargeback_dispute()
    testing.test_chargeback_dispute_transaction_frozen()
    testing.test_multiple_disputes_charged_back_withdrawal()
    




