#1 create Person Parent Class
import uuid
import json
class Person:
    def __init__(self, first_name, last_name, addr, phone_num):   
        self.first_name = first_name
        self.last_name = last_name
        self.address = addr
        self.phone_num = phone_num
        print('Welcome user {}!!!'.format(self.first_name))
        print('----------------------------------------------------')     
    def display_profile(self):
        '''
        To print out the person object's profile information.
        '''
        print('User Name: {} {} \nAddress: {} \nPhone Number: {}'.format(self.first_name, self.last_name, self.address, self.phone_num))
     
# create child classes of the parent class: Person that inherits all the properties and methods from it.

class Customer(Person):
    def __init__(self, first_name, last_name, addr, phone_num):
        Person.__init__(self, first_name, last_name, addr, phone_num)
        self.accounts_available = {}  # key: account_num and values: account obj.
        self.services_available = {}  # key: service_num and values: service obj.
# instantiate the Account types here.
    def create_account(self):
        '''
        This method allows users to create a specified account as an instance of various account classes.
        '''
        request_input = input('Do you need to create accounts? Enter "Y" to create: ')
        while request_input == "Y":
            create_account_input = input('Please type "S" to create SavingsAccount and "C" to create CheckingsAccount: ')
            if create_account_input == 'C':
                account_type = CheckingsAccount()
                print('Welcome to the Account System! Your CheckingsAccount {} has been created!'.format(account_type.account_num))
                self.accounts_available[account_type.account_num] = account_type
                # self.accounts_balance[account_type.account_num] = account_type.balance_amount
                continue
            elif create_account_input == 'S':
                account_type = SavingsAccount()
                print('Welcome to the Account System! Your SavingsAccount {} has been created!'.format(account_type.account_num)) # indicates the SavingsAccount has been created successfully.    
                self.accounts_available[account_type.account_num] = account_type
                # self.accounts_balance[account_type.account_num] = self.account_type.balance_amount
                continue
            else:
                print('You are all set!')  
                break 
        else:
            print('You are all set! Your current available accounts are {}.'.format(account_type.account_num))    
        print('Your current available accounts are {}.'.format(self.accounts_available)) 
        print('----------------------------------------------------')
        # return self.account_type
    
    # instantiate the Service types here.
    def create_service(self):
        '''
        This method allows users to create a specified service as an instance of various service classes.
        '''
        request_input = input('Do you need to create services? Enter "Y" to create: ')
        while request_input == 'Y':
            create_service_input = input('Please type "C" to create CreditCard service and "L" to create Loan service: ')
            if create_service_input == 'C':
                service_type = CreditCard(self.first_name + ' ' + self.last_name,'12/26','009')  # Should I ask for input here for expiration_date and CVV here? Or in the creditcard() method?
                print('Welcome to the Service System! Your ServiceAccount {} has been created!'.format(service_type.service_num))
                self.services_available[service_type.service_num] = service_type
                continue

            elif create_service_input == 'L':
                service_type = Loan()  
                print('Welcome to the Service System! Your ServiceAccount {} has been created!'.format(service_type.service_num))
                self.services_available[service_type.service_num] = service_type
                continue
            else:
                print('You are all set!')  
                break
        else:
            print('You are all set! Your current available services are {}.'.format(service_type.service_num))    
        print('Your current available services are {}.'.format(self.services_available)) 
        print('----------------------------------------------------')

    def close_account(self):
        '''
        This method gives the user the option to close the bank accounts they have created and print out the details.
        '''
        request_input = input('Do you need to close accounts? Enter "Y" to close: ') # Ensure customers' needs are all set!
        while request_input == 'Y': # while loop to enable multiple accounts creating or removing until confirmed.
            acc_num = input('Please enter the account num to remove here: ')
            # need skip the error if the num doesn't match and ensure the code still runs without interruptions.
            if acc_num in self.accounts_available.keys():
                del self.accounts_available[acc_num] 
                continue         
            else:
                print('Oops! Account does not exist. Please try again!') # it doesn't seem this is being executed.
                break    
        else:
            print('You are all set!')
        print('Your updated accounts list {}.'.format(self.accounts_available))  # this is to return the account_available property in the decorator.
        print('----------------------------------------------------')
    
    def transfer(self): # want the customer to be able to select the accounts to transfer from and to.
        '''
        This method gives the user the option to make multiple transfers from one account to another and print out the details.
        '''
        request_input = input('Please enter "Y" to transfer: ')
        while request_input == "Y":
            transfer_from = input('Please select the account that you want to transfer from: ')
            transfer_to = input('Please select the account that you want to transfer to: ')
            transfer_amount = input('Please enter amount to transfer in $: ')
            self.transfer_from = transfer_from
            self.transfer_to = transfer_to
            self.transfer_amount = transfer_amount
            if self.transfer_from in self.accounts_available.keys() and self.transfer_to in self.accounts_available.keys():  
                self.accounts_available[self.transfer_from].withdraw(self.transfer_amount)    # This create an account instance and call its withdraw method. 
                self.accounts_available[self.transfer_to].deposit(self.transfer_amount)  # This create an account instance and call its deposit method.
                print('${} has been transferred from account: {} to account: {}!'.format(self.transfer_amount, self.transfer_from, self.transfer_to))
            else:
                print('The account does not exist. Please try again!')        
            more_input = input('Please enter "Y" for more transfers: ')
            if more_input == 'Y':
                continue
            else:
                break
        print('You are all set!')  
        print('----------------------------------------------------')
    
    def display_profile(self):
        total_account_amount = 0
        total_service_amount = 0
        Person.display_profile(self)
        for acc in self.accounts_available.values():
            total_account_amount += acc.balance_amount
        for ser in self.services_available.values():
            total_service_amount += ser.service_balance
        print('Available Accounts: {} \nAccount Balance: {} \nAvailable Services: {} \nService Balance: {}'.format(self.accounts_available, total_account_amount, self.services_available, total_service_amount))

class Employee(Customer):
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

#2 Create Account Parent Class.
class Account:
    def __init__(self):
        account_num = input('Please enter the account num: ')
        # account_num = uuid.uuid1()
        self.account_num = account_num # for transfer method purpose
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
        print('You are all set!')
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
        print('You are all set!')
        print('----------------------------------------------------')

    def display(self):
        print('----------------------------------------------------')
        print("Account_num: {} \nTotal Available Balance Amount: ${} \nTotal Deposit Amount: ${} \nTotal Withdraw Amount: ${} \nTotal Interest Accrued Amount: ${}".format(self.account_num,self.balance_amount,self.deposit_amount,self.withdraw_amount,self.int_accrued_amount))

class CheckingsAccount(Account):
    def __init__(self):
        Account.__init__(self) # how to rename the variable to differentiate types here? 

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)  # invoking the __init__ of the parent class 

    def interest_accrued(self): 
        int_rate = float(input('Please enter interest rate: '))
        self.int_accrued_amount = int_rate * self.balance_amount # could be more sophisticated by 
        self.balance_amount += self.int_accrued_amount 
        return self.int_accrued_amount


#3 Create Service Parent Class
class Service:
    def __init__(self):
        service_num = input('Please enter the service num: ')  
        # service_num = uuid.uuid1()  
        self.service_num = service_num
        self.service_balance = 0
        print('Service num: {} with service balance of {}.'.format(self.service_num,self.service_balance))

    def make_payment(self):
        description = input('Please enter "C" to make CreditCard payment and "L" to make Loan payment: ')  # Specify creditCards or loans, this can be replaced when the service objects can be called from Customer class. Customer should be able to decide which ones to call. 
        payment_amount = input('Please enter payment amount in $: ')
        self.description = description
        self.payment_amount = payment_amount                   
        self.service_balance -= self.payment_amount  # service_balance is basically accumulated debts from various services
       # print('Your Total Service Balance is ${}'.format(self.service_balance))
        print('----------------------------------------------------')
        return self.service_balance

class CreditCard(Service):
    def __init__(self, name, expiration_date, cvv, credit_limit=10000, salary = 0): 
        Service.__init__(self)
        self.credit_limit = credit_limit
        self.name = name
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.credit_limit = credit_limit
        if salary > 0 and salary < 100000: # how to link salary from Employee class to the credit limit here
            self.credit_limit = 5000
        elif salary >= 100000 and salary < 150000:
            self.credit_limit = 10000
        elif salary >= 150000 and salary < 200000:
            self.credit_limit = 15000
        else:
            self.credit_limit = 20000
        print('{}, your credit card with credit limit of ${} and expiration date of {} has been created.'.format(self.name, self.credit_limit,self.expiration_date))

    def make_purchase(self):
        request_input = input('Enter "Y" to make a purchase: ')
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
                more_input = input('Enter "Y" to make another purchase: ')
                if more_input == 'Y':
                    continue
                else:
                    break
            else: 
                print('Your purchase amount exceeds the limit! Your remaining available credit balance amount is ${}.'.format(self.available_balance)) 
                break
            print('----------------------------------------------------')
        else:
            print('You are all set!')
        print('----------------------------------------------------')
        print('Your current Total Credit Card service balance is ${}'.format(self.service_balance))
        print('----------------------------------------------------')
   

class Loan(Service):
    def __init__(self, loan_amount = 100000):
        Service.__init__(self)
        self.service_balance += loan_amount
        print('----------------------------------------------------')

    def take_loan(self):   # change the method to something else. 
        request_input = input('Please enter "Y" to take loans: ')
        while request_input == "Y":
            loan_amount = float(input('Please enter the loan amount in $: '))
            self.service_balance += loan_amount
            print('You got a new loan! Loan ID: {} with a loan amount of ${}.'.format(self.service_num,loan_amount))
            request_input = input('Please enter "Y" to take another loan: ')
            if request_input == 'Y':
                continue
            else: 
                break
        print('Your current total loan amount is ${}.'.format(self.service_balance))
        print('----------------------------------------------------')
        return self.service_balance

p1 = Employee('Jenny', 'Wang', '2042 Water St', '123-456-6789', 200000)
#p1.adjust_salary(20000)
#p1.close_account()
#s0 = p1.create_account()
#s0.withdraw()
# p1.transfer()
p1.create_service()
s1 = CreditCard(p1.first_name + ' ' + p1.last_name, '01/23','004', salary = p1.salary) # for testing purposes, can do this.
s1.make_purchase()
# s1.take_loan()
p1.display_profile()



