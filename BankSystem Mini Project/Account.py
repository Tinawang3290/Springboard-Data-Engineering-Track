import uuid
import pickle

class Account:  #2 Create Account Parent Class.
    def __init__(self):
        account_num = str(uuid.uuid4())[:8] # system generated uuid
        self.account_num = account_num 
        self.balance_amount = 5000  # be mindful of the variable naming here not confuse with the function names since it throws error (TypeError: 'int' object is not callable)
        self.deposit_amount = 0
        self.withdraw_amount = 0
        print('----------------------------------------------------')

    def deposit(self, deposit_amount = 0):
        if deposit_amount != 0:
            self.balance_amount += deposit_amount
            self.deposit_amount += deposit_amount
        else:
            request_input = input('Please enter "Y" to deposit: ')
            while request_input == 'Y':
                amount = float(input('Please enter amount to deposit in $: '))
                self.balance_amount += amount
                self.deposit_amount += amount
                print('Your deposit amount is ${} and total balance amount is ${}.'.format(self.deposit_amount, self.balance_amount))
                more_input = input('Please enter "Y" for more deposit: ')
                if more_input == 'Y':
                    continue
                else:
                    break
        print('----------------------------------------------------')
           
    def withdraw(self, withdraw_amount = 0):
        if withdraw_amount != 0:
            self.balance_amount -= withdraw_amount
            self.withdraw_amount += withdraw_amount
        else: 
            request_input = input('Please enter "Y" to withdraw: ')
            while request_input == 'Y':
                amount = float(input('Please enter amount to withdraw in $:'))
                if amount <= self.balance_amount:    
                    self.balance_amount -= amount
                    self.withdraw_amount += amount
                    print('Your withdraw amount is ${} and total balance amount is ${}.'.format(self.withdraw_amount, self.balance_amount))
                    more_input = input('Please enter "Y" for more withdraw: ')
                    if more_input == 'Y':
                        continue
                    else:
                        break
                else:
                    print('Insufficient balance! Your current available balance amount is ${}.'.format(self.balance_amount)) # low balance reminder
        print('----------------------------------------------------')

    def display_account(self):
        print("Accounts Display: \nAccount_num: {} \nTotal Available Balance Amount: ${} \nTotal Deposit Amount: ${} \nTotal Withdraw Amount: ${} \nTotal Interest Accrued Amount: ${}".format(self.account_num,self.balance_amount,self.deposit_amount,self.withdraw_amount,self.int_accrued_amount))

class CheckingsAccount(Account):
    '''
    CheckingsAccount is the child class of Account parent class that can inherits all attributes and methods from Account.
    '''
    def __init__(self):
        Account.__init__(self) 

class SavingsAccount(Account):
    '''
    SavingsAccount is the child class of Account parent class that can inherits all attributes and methods from Account.
    '''
    def __init__(self):
        Account.__init__(self)  

    def interest_accrued(self): 
        int_rate = float(input('Please enter interest rate: '))
        self.int_accrued_amount = int_rate * self.balance_amount 
        self.balance_amount += self.int_accrued_amount 
        return self.int_accrued_amount
