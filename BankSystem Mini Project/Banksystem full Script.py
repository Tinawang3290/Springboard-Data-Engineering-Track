
import uuid
import pickle
from datetime import timedelta, date
from random import randint

#1 create Person Parent Class
class Person:
    def __init__(self, first_name, last_name, addr, phone_num):   
        self.first_name = first_name
        self.last_name = last_name
        self.address = addr
        self.phone_num = phone_num
        self.profile_dict ={   #initiate the dictionary here for storage later
            'name': self.first_name + " "+self.last_name,
            'address': self.address,
            'phone': self.phone_num
        }
        print('Welcome user {} to the bank system!!!'.format(self.first_name))
        print('----------------------------------------------------')     
    def display_profile(self):
        '''
        To print out the person object's profile information.
        '''
        print('User Name: {} {} \nAddress: {} \nPhone Number: {}'.format(self.first_name, self.last_name, self.address, self.phone_num))   

class Customer(Person): 
    '''
    Customer is a child class of Person parent class that can inherits everything from Person's class.
    '''
    def __init__(self, first_name, last_name, addr, phone_num):
        Person.__init__(self, first_name, last_name, addr, phone_num)
        self.accounts_available = {}  # key: account_num and values: account obj.
        self.services_available = {}  # key: service_num and values: service obj.
        self.profile_dict['accounts_available'] = self.accounts_available
        self.profile_dict['services_available'] = self.services_available
        
# instantiate the Account types here.
    def create_account(self):
        '''
        This method allows users to create a specified account as an instance of various account classes.
        '''
        while True:
            create_account_input = input('Please type "S" to create SavingsAccount and "C" to create CheckingsAccount, else to exit: ')
            if create_account_input == 'C':
                account_obj = CheckingsAccount()
                print('Welcome to the Account System! Your CheckingsAccount {} with account balance of ${} has been created!'.format(account_obj.account_num, account_obj.balance_amount))
                self.accounts_available[account_obj.account_num] = account_obj
                continue
            elif create_account_input == 'S':
                account_obj= SavingsAccount()
                print('Welcome to the Account System! Your SavingsAccount {} with account balance of ${} has been created!'.format(account_obj.account_num, account_obj.balance_amount)) # indicates the SavingsAccount has been created successfully.    
                self.accounts_available[account_obj.account_num] = account_obj
                continue
            else:
                break 
        with open('accounts_available.pkl','wb') as accounts_file:         # using pickle to store accounts  
            pickle.dump(self.profile_dict, accounts_file)
        with open('accounts_available.pkl','rb') as accounts_file:
            display_accounts = pickle.load(accounts_file)
            print(display_accounts) 
        print('Your current available accounts are {}.'.format(self.accounts_available.keys())) 
        print('----------------------------------------------------')
        return self.accounts_available
    
    def create_service(self):     # instantiate the Service types here.
        '''
        This method allows users to create a specified account as an instance of various service classes.
        '''
        while True:
            create_service_input = input('Please type "C" to create CreditCard and "L" to create Loan, else to eixt: ')
            if create_service_input == 'C':
                service_obj = CreditCard()
                service_obj.make_purchase() # trigger the make_purchase method from CreditCard class so that we don't have to create a separate creditcard object for testing.
                self.services_available[service_obj.service_num] = service_obj
                continue
            elif create_service_input == 'L':
                service_obj = Loan()   
                self.services_available[service_obj.service_num] = service_obj
                continue
            else:
                break 
        with open('services_available.pkl','wb') as services_file:         # using pickle to store services  
            pickle.dump(self.profile_dict, services_file)
        with open('services_available.pkl','rb') as services_file:
            display_services = pickle.load(services_file)
            print(display_services) 
        print('Your current available services are {}.'.format(self.services_available.keys())) 
        print('----------------------------------------------------')
        return self.services_available

    def close_account(self): 
        '''
        This method gives the user the option to close the bank accounts they have created and print out the details.
        '''
        while True:
            acc_num = input('Please enter the account num to remove here: ')  
            if acc_num in self.accounts_available.keys():
                del self.accounts_available[acc_num] 
                more_input = input('Enter "Y" to close another account, else to exit: ')
                if more_input == "Y":
                    continue
                else:
                    break       
            else:
                request = input('Oops! Account does not exist. Please enter "Y" to try again, else to exit:')    # need skip the error if the num doesn't match and ensure the code still runs without interruptions.
                if request == 'Y':
                    continue  
                else:
                    break          
        print('Your updated accounts list {}.'.format(self.accounts_available.keys()))  # this is to return the account_available property in the decorator.
        print('----------------------------------------------------')
        return self.accounts_available
    
    def transfer(self): # want the customer to be able to select the accounts to transfer from and to.
        '''
        This method gives the user the option to make multiple transfers from one account to another and print out the details.
        '''
        while True:
            transfer_from = input('Please select the account to transfer moeny from: ')
            transfer_to = input('Please select the account to transfer money to: ')
            transfer_amount = float(input('Please enter amount to transfer in $: '))
            self.transfer_from = transfer_from
            self.transfer_to = transfer_to
            self.transfer_amount = transfer_amount
            if self.transfer_from in self.accounts_available.keys() and self.transfer_to in self.accounts_available.keys():  
                self.accounts_available[self.transfer_from].withdraw(self.transfer_amount)    # This create an account instance and call its withdraw method. 
                self.accounts_available[self.transfer_to].deposit(self.transfer_amount)  # This create an account instance and call its deposit method.
                print('${} has been transferred from account: {} to account: {}!'.format(self.transfer_amount, self.transfer_from, self.transfer_to))
            else:
                print('The account does not exist. Please try again!')        
            more_input = input('Please enter "Y" for more transfers, else to exit: ')
            if more_input == 'Y':
                continue
            else:
                break
        print('----------------------------------------------------')
    
    def make_payment(self):
        '''
        This method allows the user to make payments to their service accounts, this can leverage the receive_payment method from Service class 
        and withdraw method from Account class.
        '''
        while True:
            pay_from = input('Please select the account num to pay from: ')
            pay_to = input('Please select the service num to pay to: ')
            payment_amount = float(input('Please enter payment amount in $: '))
            self.payment_amount = payment_amount
            self.pay_from = pay_from 
            self.pay_to = pay_to
            if pay_from in self.accounts_available.keys() and pay_to in self.services_available.keys():
                self.accounts_available[self.pay_from].withdraw(self.payment_amount)
                self.services_available[self.pay_to].receive_payment(self.payment_amount) 
                print('${} has been made from account {} to service {}!'.format(self.payment_amount, self.pay_from, self.pay_to))
            else:
                print('The account/service does not exist. Please try again!')        
                more_input = input('Please enter "Y" to make another payment, elst to exit: ')
                if more_input == 'Y':
                    continue
                else:
                    break
        print('----------------------------------------------------')
    
    def display_profile(self):
        '''
        This method is used to display the total account amount and total service amount.
        '''
        total_account_amount = 0
        total_service_amount = 0
        Person.display_profile(self)
        for acc in self.accounts_available.values():
            total_account_amount += acc.balance_amount
            print('Account {} has a balance amount of ${}'.format(acc.account_num, acc.balance_amount))
        for ser in self.services_available.values():
            total_service_amount += ser.service_balance
            print('Service {} has a service balance amount of ${}'.format(ser.service_num, ser.service_balance))
        print('Available Accounts: {} \nTotal Account Balance: {} \nAvailable Services: {} \nTotal Service Balance: {}'.format(self.accounts_available, total_account_amount, self.services_available, total_service_amount))

class Employee(Customer): # Employee is a child class of Customer class since it can inherit from Customer class if employee is also a customer.
    def __init__(self, first_name, last_name, addr, phone_num, salary):
        Customer.__init__(self, first_name, last_name, addr, phone_num) #inherit from parent class Customer
        self.salary = salary   

    def adjust_salary(self, change_amount):
        self.salary += change_amount
        print('Your current annual salary is ${}.'.format(self.salary))
        print('----------------------------------------------------')
    def display_profile(self):
        Customer.display_profile(self)
        print('Current Annual Salary: ${} '.format(self.salary))
        print('----------------------------------------------------')

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

#3 Create Service Parent Class
class Service:
    '''
    Service is a third parent class that can contains sub-services such as credit cards and loans, etc.
    '''
    def __init__(self):
        service_num = str(uuid.uuid4())[:8] # system generated uuid
        self.service_num = service_num
        self.service_balance = 0
        self.received_payment = 0
        print('----------------------------------------------------')
    
    def receive_payment(self, payment_amount = 0):
        if payment_amount != 0:
            self.service_balance -= payment_amount
            self.received_payment += payment_amount
            print('Service number: {} has received ${} total payments and the current service balance is ${}.'.format(self.service_num, self.received_payment, self.service_balance))
            print('----------------------------------------------------')
            return self.service_balance

class CreditCard(Service):
    '''
    Creditcard is a sub-service, which contains a unique num, 3-digits cvv, with a fixed 10 years expiration duration since the application,
    and credit limits bands, which depend on the salary of the user.
    '''
    def __init__(self): 
        Service.__init__(self)
        salary = float(input('Please enter the annual salary in $: '))
        credit_limit=5000
        cvv = randint(100, 999)
        expiration_date = date.today() + timedelta(days = 3650)
        self.expiration_date = expiration_date
        self.credit_limit = credit_limit
        self.salary = salary
        self.cvv = cvv
        self.credit_limit = credit_limit
        if self.salary > 0 and self.salary < 100000: # how to link salary from Employee class to the credit limit here
            self.credit_limit = 5000
        elif self.salary >= 100000 and self.salary < 150000:
            self.credit_limit = 10000
        elif self.salary >= 150000 and self.salary < 200000:
            self.credit_limit = 15000
        else:
            self.credit_limit = 20000
        print('Hi, your credit card num {} with credit limit of ${} and expiration date of {} and cvv of {} has been created.'.format(self.service_num,self.credit_limit,self.expiration_date, self.cvv))
        print('----------------------------------------------------')

    def make_purchase(self):
        '''
        This method allows user to make purchases, it accumulates service balances when there is a purchase incurring.
        '''
        request_input = input('Enter "Y" to make a purchase, else to exit: ')
        self.available_balance = self.credit_limit # this should be placed outside of the while loop
        while request_input == 'Y': # enable multiple purchases.
            vendor = input('Please enter the vendor name: ')
            purchase_amount = float(input('Please enter purchase amount in $: ')) 
            self.vendor = vendor
            self.purchase_amount = purchase_amount
            if self.available_balance >0 and self.purchase_amount <= self.available_balance:
                self.service_balance += purchase_amount # accumulated balance amount on the card
                self.available_balance = self.credit_limit - self.service_balance  # available balanace to borrow based on the credit_limit.
                print('You have made a purchase at {} with the amount of ${} and your current available credit card balance is ${}'.format(self.vendor, self.purchase_amount,self.available_balance)) # to confirm the purchase has been made.
                more_input = input('Enter "Y" to make another purchase, else to exit: ')
                if more_input == 'Y':
                    continue
                else:
                    break
            else: 
                print('Your purchase amount exceeds the limit! Your remaining available credit balance amount is ${}.'.format(self.available_balance)) 
                print('----------------------------------------------------')
                break    
        print('Your current Total Credit Card service balance is ${}'.format(self.service_balance))
        print('----------------------------------------------------')

class Loan(Service):
    '''
    Loan is another sub-service, which requires interest rate, loan amount inputs from users.
    '''
    def __init__(self):
        Service.__init__(self)
        int_rate = input('Please enter the interest rate: ')
        loan_amount = float(input('Please enter the loan amount in $: '))
        self.service_balance += loan_amount
        self.int_rate = int_rate
        print('Your loan num {} with loan amount of ${} and interest rate of {} has been created.'.format(self.service_num,self.service_balance,self.int_rate))
        print('----------------------------------------------------')

p1 = Employee('Jenny', 'Fan', '2042 Water St', '415-607-9343', 200000)
p1.create_account()
p1.close_account()
p1.transfer()
p1.adjust_salary(10000)
p1.create_service()
p1.display_profile()
p1.make_payment()
p1.display_profile()
