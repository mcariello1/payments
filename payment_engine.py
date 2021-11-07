
import csv


class Client:

    def __init__(self): 
        self.__account_data = {'transactions':{},'available':0, 'held': 0, 'locked':False}

    def is_locked(self):
        return self.__account_data['locked']
    
    def get_account_information(self):
        total = self.get_total_funds()
        available = self.__account_data["available"]
        held = self.__account_data["held"]
        locked = self.__account_data["locked"]
        return f"{available},{held},{total},{locked}\n"

    
    def get_total_funds(self):
        return self.__account_data['available'] + self.__account_data['held']

    def deposit(self, tx: int, amount: float) -> None:

        
        self.__account_data['available'] += amount
        self.__account_data['transactions'][tx] = [amount, 'deposit']

    def withdrawal(self, tx: int, amount: float):
        
        if amount > self.__account_data['available']:
                #If a client does not have sufficient available funds the withdrawal should fail and the total amount of funds should not change
            pass
                #print(f"Transaction {tx} cannot be performed due to insufficient funds")
        else:
            self.__account_data['available'] -= amount
            self.__account_data['transactions'][tx] = [amount, 'withdrawal']
            

    def dispute(self, tx: int): 
        """
        Disputed holds the funds until a resolve or chargeback is performed on that transaction
        Args: 
        tx (int): The transaction id of the disputed transaction
        """
    
        # alternative if withdrawal or deposit from clients account is disputed
        
        '''
        if self.__account_data['transactions'][tx][1] == 'withdrawal':
            # increase held by amount
            self.__account_data['held'] += self.__account_data['transactions'][tx][0]

            #
        if self.__account_data['transactions'][tx][1] == 'deposit':
            self.__account_data['held'] += self.__account_data['transactions'][tx][0]
            self.__account_data['available'] -= self.__account_data['transactions'][tx][0]
        '''

        # as per description

        self.__account_data['held'] += self.__account_data['transactions'][tx][0]
        self.__account_data['available'] -= self.__account_data['transactions'][tx][0]




    def resolve(self, tx: int):
        """
        Resolve allows original transaction to complete back to its original state. 
        Args:
        tx (int): transaction id of disputed transaction
        """
        if tx in self.__account_data['transactions']:

            self.__account_data['held'] -= self.__account_data['transactions'][tx][0]
            self.__account_data['available'] += self.__account_data['transactions'][tx][0]
        else:
            #ignore as faulty message 
            pass


    def chargeback(self, tx: int):
        """
        Chargeback reverses the transaction and flags the account as locked. 
        Args:
        tx (int): transaction id of disputed transaction
        """ 
        if tx in self.__account_data['transactions']:
            self.__account_data['held'] -= self.__account_data['transactions'][tx][0]
            self.__account_data['locked'] = True
        else:
            #ignore as faulty message 
            pass




class PaymentsProcessing:
    def __init__(self, transactions_filename:str):

        self.transactions_filename = transactions_filename
        self.clients = {}


    def process_transactions(self) -> str:
        with open(self.transactions_filename) as transactions_csv:
            reader = csv.reader(transactions_csv)
            for row in reader:
                row = [col.strip() for col in row]
                transaction= row[0]
                if row[1] == 'client':
                    #ignore header
                    continue

                client_id = str(row[1])
                row[0] = transaction.lower()

                if len(row[3]) == 0 or row[3]== "''":
                    args = [int(row[2])]
                else:
                    args = [int(row[2]), float(row[3])]

                args = tuple(args)
                
                if client_id in self.clients:
                    try:
                
                        if not self.clients[client_id].is_locked():
                            getattr(self.clients[client_id], transaction)(*args)
                    except Exception as exception:

                        #print(f"{transaction} failed to process due to: {exception}, make sure input, input types and valid transactions are given")
                        pass
                else:
                    self.clients[client_id] = Client()
                    try:
                        getattr(self.clients[client_id], transaction)(*args)
                    except Exception as exception:
                        #print(f"{row} failed to process due to: {exception}, make sure input, input types and valid transactions are given")
                        pass
        


        output_string = "client, available, held, total, locked\n"

        for client in self.clients:
            client_account_string = f"{client}," + self.clients[client].get_account_information()
            output_string  = output_string+client_account_string

        print(output_string[:-1])
        return output_string




if __name__ == "__main__":
    
    import sys
    
    payments_processor = PaymentsProcessing(str(sys.argv[1]))
    payments_processor.process_transactions()