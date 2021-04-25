import pickle
from Account import CheckingAccount, SavingsAccount

class Person:
    def __init__(self, first_name, last_name, addr, phone_num):   
        self.first_name = first_name
        self.last_name = last_name
        self.address = addr
        self.phone_num = phone_num
        self.profile_dict ={   #initiate the dictionary here for storage later
            'name': self.first_name + self.last_name,
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
     
# create child classes of the parent class: Person that inherits all the properties and methods from it.

class Customer(Person):
    def __init__(self, first_name, last_name, addr, phone_num):
        Person.__init__(self, first_name, last_name, addr, phone_num)
        self.accounts_available = {}  # key: account_num and values: account obj.
        self.services_available = {}  # key: service_num and values: service obj.
        #
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
                account_type = CheckingsAccount()
                print('Welcome to the Account System! Your CheckingsAccount {} has been created!'.format(account_type.account_num))
                self.accounts_available[account_type.account_num] = account_type
                continue
            elif create_account_input == 'S':
                account_type = SavingsAccount()
                print('Welcome to the Account System! Your SavingsAccount {} has been created!'.format(account_type.account_num)) # indicates the SavingsAccount has been created successfully.    
                self.accounts_available[account_type.account_num] = account_type
                continue
            else:
                print('You are all set!')  
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
                service_type = CreditCard(self, first_name, last_name, salary, credit_limit=10000)
                print('Welcome to the Service System! Your CreditCard {} has been created!'.format(service_type.service_num))
                self.services_available[service_type.service_num] = service_type
                continue
            elif create_service_input == 'L':
                service_type = Loan(self, first_name, last_name, int_rate = 0.35, loan_amount = 100000)
                print('Welcome to the Service System! Your Loan {} has been created!'.format(service_type.service_num))     
                self.accounts_available[service_type.account_num] = service_type
                continue
            else:
                print('You are all set!')  
                break 
        with open('services_available.pkl','wb') as serivces_file:         # using pickle to store services  
            pickle.dump(self.profile_dict, services_file)
        with open('services_available.pkl','rb') as services_file:
            display_services = pickle.load(services_file)
            print(display_services) 
        print('the account is {}'.format(self.services_available.values()))
        print('Your current available accounts are {}.'.format(self.services_available.keys())) 

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
            payment_amount = input('Please enter payment amount in $: ')
            self.payment_amount = payment_amount
            self.pay_from = pay_from 
            self.pay_to = pay_to
            if pay_from in self.profile_dict[accounts_available].keys() and pay_to in self.profile_dict[services_available].keys():
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
        print('You are all set!')  
        print('----------------------------------------------------')
        self.service_balance -= self.payment_amount  # service_balance is basically accumulated debts from various services
       # print('Your Total Service Balance is ${}'.format(self.service_balance))
        print('----------------------------------------------------')
        return self.service_balance
    
    def display_profile(self):
        '''
        This method is used to display the total account amount and total service amount.
        '''
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

