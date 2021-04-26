import uuid
import pickle
from datetime import timedelta, date
from random import randint
from Person import Customer,Employee

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
