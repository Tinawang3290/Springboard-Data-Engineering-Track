<img width="583" alt="Screen Shot 2021-04-24 at 11 53 16 PM" src="https://user-images.githubusercontent.com/37784402/115983797-4ba8f080-a558-11eb-8646-f8ea75a2a1ba.png">

We regularly interact with banks in our day-to-day lives, but rarely think about the systems that power them. Banks power global finance, and the online systems that enable this are incredibly complex.
In this project, we are required to create a simpler version of a banking system by using Python OOP techniques. In the bank model, we have entities for customers, accounts, employees, and services like loans and credit cards. Each of these entities have their distinct properties and methods.

The final project should be structured in the manner outlined https://docs.python-guide.org/writing/structure/. The project should be executable via the command line. It should accept user inputs and return results from the command line.

### Step 1: Using UML diagram to design the bank system (full diagram: https://app.diagrams.net/#G1DZt7EXBSnK95bnUacIYB5cMsqa6Hz0fM)
The project encompasses three main parent classes:

1. Person (Child classes: Customer, note: Employee is a subclass of Customer class since an Employee could be a customer or non-customer)
2. Account (Child classes: CheckingAccount, SavingsAccount)
3. Services (Child classes: CreditCard, Loan)

Diagram #1: Person (Child classes: Customer, note: Employee is a subclass of Customer class since an Employee could be a customer or non-customer)

<img width="530" alt="Screen Shot 2021-04-25 at 9 33 01 PM" src="https://user-images.githubusercontent.com/37784402/116029349-f9c2a200-a60d-11eb-92a5-06d4321193bd.png">

Diagram #2: Account (Child classes: CheckingAccount, SavingsAccount)

<img width="470" alt="Screen Shot 2021-04-25 at 9 33 14 PM" src="https://user-images.githubusercontent.com/37784402/116029362-02b37380-a60e-11eb-805c-f2f014681ac5.png">

Diagram #3: Services (Child classes: CreditCard, Loan)

<img width="569" alt="Screen Shot 2021-04-25 at 9 33 25 PM" src="https://user-images.githubusercontent.com/37784402/116029367-0515cd80-a60e-11eb-98da-b6cd080e22d1.png">

### Step 2: Write scripts in Python OOP manner based on the UML diagram
The code are devided into three parts based on it's parent classes.
You can find each part with `name.py` file saved.

### Step 3: Unit testing each part to ensure it's working properly respectively, then run the full script together to ensure the whole logic can be linked and function smoothly as a whole.

Below is the test result snapshot if you run the `Banksystem full script.py`, the project is completely executable via the command line. It not only accepts user inputs but also return results from the command line. The logic and functionalities are working correctly and smoothly as I originally desired, tho it's a bit sophisticated than the original assignment requirements, it's definitely a great practice to enhance my understanding of Python OOP approach, leverage the usage of some exisiting built-in modules, etc.

```
/usr/bin/python /Users/tinawang/Downloads/BankSystemTesting.py
tinawang@Tinas-MacBook-Pro VSC Test % /usr/bin/python /Users/tinawang/Downloads/BankSystemTesting.py
Welcome user Jenny to the bank system!!!
----------------------------------------------------
Please type "S" to create SavingsAccount and "C" to create CheckingsAccount, else to exit: 'S'
----------------------------------------------------
Welcome to the Account System! Your SavingsAccount d0559593 with account balance of $5000 has been created!
Please type "S" to create SavingsAccount and "C" to create CheckingsAccount, else to exit: 'S'
----------------------------------------------------
Welcome to the Account System! Your SavingsAccount c1d15f77 with account balance of $5000 has been created!
Please type "S" to create SavingsAccount and "C" to create CheckingsAccount, else to exit: 'C'
----------------------------------------------------
Welcome to the Account System! Your CheckingsAccount 4f30bbe4 with account balance of $5000 has been created!
Please type "S" to create SavingsAccount and "C" to create CheckingsAccount, else to exit: 'V'
{'phone': '415-607-9343', 'services_available': {}, 'name': 'Jenny Fan', 'accounts_available': {'d0559593': <__main__.SavingsAccount instance at 0x10b836bd8>, 'c1d15f77': <__main__.SavingsAccount instance at 0x10b836b90>, '4f30bbe4': <__main__.CheckingsAccount instance at 0x10b836b48>}, 'address': '2042 Water St'}
Your current available accounts are ['4f30bbe4', 'c1d15f77', 'd0559593'].
----------------------------------------------------
Please enter the account num to remove here: '4f30bbe4'
Enter "Y" to close another account, else to exit: 'V'
Your updated accounts list ['c1d15f77', 'd0559593'].
----------------------------------------------------
Please select the account to transfer moeny from: 'c1d15f77'
Please select the account to transfer money to: 'd0559593'
Please enter amount to transfer in $: 2000
----------------------------------------------------
----------------------------------------------------
$2000.0 has been transferred from account: c1d15f77 to account: d0559593!
Please enter "Y" for more transfers, else to exit: 'V'
----------------------------------------------------
Your current annual salary is $210000.
----------------------------------------------------
Please type "C" to create CreditCard and "L" to create Loan, else to eixt: 'C'
----------------------------------------------------
Please enter the annual salary in $: 210000
Hi, your credit card num 02c37f3a with credit limit of $20000 and expiration date of 2031-04-23 and cvv of 552 has been created.
----------------------------------------------------
Enter "Y" to make a purchase, else to exit: 'Y'
Please enter the vendor name: 'APPLE'
Please enter purchase amount in $: 1500
You have made a purchase at APPLE with the amount of $1500.0 and your current available credit card balance is $18500.0
Enter "Y" to make another purchase, else to exit: 'Y'
Please enter the vendor name: 'GOOGLE'
Please enter purchase amount in $: 5000
You have made a purchase at GOOGLE with the amount of $5000.0 and your current available credit card balance is $13500.0
Enter "Y" to make another purchase, else to exit: 'Y'
Please enter the vendor name: 'IKEA'
Please enter purchase amount in $: 14000
Your purchase amount exceeds the limit! Your remaining available credit balance amount is $13500.0.
----------------------------------------------------
Your current Total Credit Card service balance is $6500.0
----------------------------------------------------
Please type "C" to create CreditCard and "L" to create Loan, else to eixt: 'L'
----------------------------------------------------
Please enter the interest rate: 0.3
Please enter the loan amount in $: 15000
Your loan num 0bb18166 with loan amount of $15000.0 and interest rate of 0.3 has been created.
----------------------------------------------------
Please type "C" to create CreditCard and "L" to create Loan, else to eixt: 'V'
{'phone': '415-607-9343', 'services_available': {'0bb18166': <__main__.Loan instance at 0x10b836bd8>, '02c37f3a': <__main__.CreditCard instance at 0x10b836998>}, 'name': 'Jenny Fan', 'accounts_available': {'c1d15f77': <__main__.SavingsAccount instance at 0x10b836c68>, 'd0559593': <__main__.SavingsAccount instance at 0x10b836c20>}, 'address': '2042 Water St'}
Your current available services are ['0bb18166', '02c37f3a'].
----------------------------------------------------
User Name: Jenny Fan 
Address: 2042 Water St 
Phone Number: 415-607-9343
Account c1d15f77 has a balance amount of $3000.0
Account d0559593 has a balance amount of $7000.0
Service 0bb18166 has a service balance amount of $15000.0
Service 02c37f3a has a service balance amount of $6500.0
Available Accounts: {'c1d15f77': <__main__.SavingsAccount instance at 0x10b8368c0>, 'd0559593': <__main__.SavingsAccount instance at 0x10b836878>} 
Total Account Balance: 10000.0 
Available Services: {'0bb18166': <__main__.Loan instance at 0x10b836b48>, '02c37f3a': <__main__.CreditCard instance at 0x10b836908>} 
Total Service Balance: 21500.0
Current Annual Salary: $210000 
----------------------------------------------------
Please select the account num to pay from: 'c1d15f77'
Please select the service num to pay to: '0bb18166'
Please enter payment amount in $: 900 
----------------------------------------------------
Service number: 0bb18166 has received $900.0 total payments and the current service balance is $14100.0.
----------------------------------------------------
$900.0 has been made from account c1d15f77 to service 0bb18166!
Please select the account num to pay from: '0559593'
Please select the service num to pay to: '02c37f3a'
Please enter payment amount in $: 3300
The account/service does not exist. Please try again!
Please enter "Y" to make another payment, elst to exit: 'Y'       
Please select the account num to pay from: 'd0559593'    
Please select the service num to pay to: '02c37f3a'
Please enter payment amount in $: 3200
----------------------------------------------------
Service number: 02c37f3a has received $3200.0 total payments and the current service balance is $3300.0.
----------------------------------------------------
$3200.0 has been made from account d0559593 to service 02c37f3a!
Please select the account num to pay from: '00'
Please select the service num to pay to: '00'
Please enter payment amount in $: 0  
The account/service does not exist. Please try again!
Please enter "Y" to make another payment, elst to exit: 'V'
----------------------------------------------------
User Name: Jenny Fan 
Address: 2042 Water St 
Phone Number: 415-607-9343
Account c1d15f77 has a balance amount of $2100.0
Account d0559593 has a balance amount of $3800.0
Service 0bb18166 has a service balance amount of $14100.0
Service 02c37f3a has a service balance amount of $3300.0
Available Accounts: {'c1d15f77': <__main__.SavingsAccount instance at 0x10b8368c0>, 'd0559593': <__main__.SavingsAccount instance at 0x10b836878>} 
Total Account Balance: 5900.0 
Available Services: {'0bb18166': <__main__.Loan instance at 0x10b836b48>, '02c37f3a': <__main__.CreditCard instance at 0x10b836908>} 
Total Service Balance: 17400.0
Current Annual Salary: $210000 
----------------------------------------------------
```

### Step 4: Data storage
For data storage, mostly, it's in-memory excution, Python Pickle is a good tool for the storage of this project.  Given it is primarily used in serializing and deserializing a Python object structure. In other words, it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network.



