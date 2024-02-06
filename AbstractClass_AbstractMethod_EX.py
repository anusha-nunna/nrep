#Bank Account Management System: Design a Python class hierarchy for a bank account management system.
#-There should be a base class Account with subclasses SavingsAccount and CheckingAccount. 
#-Each account should have attributes such as account number, balance, and account holder name. Implement methods for deposit, withdrawal, and balance inquiry. 
#-Ensure that the minimum balance requirements are enforced for both savings and checking accounts.


from abc import ABC,abstractmethod
class Account(ABC):
    @abstractmethod
    def __init__(self,account_number, balance, account_holder_name):
        pass
        
class SavingsAccount(Account):
    def __init__(self,account_number, balance, account_holder_name):
        super().__init__(account_number, balance, account_holder_name)
        self.balance = balance
        
   
    def deposit(self):
        print("user can add funds to their account")
        
    
    def withdrawl(self):
        withdrawl_amount = float(int(input("enter the selected amount: ")))
        print("User can withdraw funds from their account")          

        if self.balance - withdrawl_amount < 1000:
            print("withdrawal is not allowed because it would cause the balance to fall below the minimum threshold")
        else:
            print("withdrawal is allowed")
        
    def balance_inquiry(self):
        print("current balance of the account to the user")
        
    def minimum_balance_requirements(self):
        print("balance in the account should never fall below this minimum threshold")


class CheckingAccount(Account):
    def __init__(self,account_number, balance, account_holder_name):
        super().__init__(account_number, balance, account_holder_name)
        self.balance = balance

            
    def deposit(self):
        print("user can add funds to their account")
        

    def withdrawl(self):
        withdrawl_amount = float(int(input("enter the selected amount: ")))
        print("User can withdraw funds from their account")     

        if self.balance - withdrawl_amount < 1000:
            print("withdrawal is not allowed because it would cause the balance to fall below the minimum threshold")
        else:
            print("withdrawal is allowed")

        
    def balance_inquiry(self):
        print("current balance of the account to the user")

    def minimum_balance_requirements(self):
        print("balance in the account should never fall below this minimum threshold")


object = SavingsAccount(account_number = 12345, balance = 40000, account_holder_name = "Anusha Nunna")
object.deposit()
object.withdrawl()
object.balance_inquiry()
object.minimum_balance_requirements()

object_1 = CheckingAccount(account_number = 67890, balance = 50000, account_holder_name = "Harish Nunna")
object_1.deposit()
object_1.withdrawl()
object_1.balance_inquiry()
object_1.minimum_balance_requirements()






