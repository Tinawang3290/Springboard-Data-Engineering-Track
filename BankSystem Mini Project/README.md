<img width="583" alt="Screen Shot 2021-04-24 at 11 53 16 PM" src="https://user-images.githubusercontent.com/37784402/115983797-4ba8f080-a558-11eb-8646-f8ea75a2a1ba.png">

We regularly interact with banks in our day-to-day lives, but rarely think about the systems that power them. Banks power global finance, and the online systems that enable this are incredibly complex.
In this project, we are required to create a simpler version of a banking system by using Python OOP techniques. In the bank model, we have entities for customers, accounts, employees, and services like loans and credit cards. Each of these entities have their distinct properties and methods.

The final project should be structured in the manner outlined https://docs.python-guide.org/writing/structure/. Your project should be executable via the command line. It should accept user inputs and return results from the command line.

### Step 1: Using UML diagram to design the bank system
it encompasses three parent classes:

1. Person (Child classes: Customer, Employee)
2. Account (Child classes: CheckingAccount, SavingsAccount)
3. Services (Child classes: CreditCard, Loan)

Diagram #1: Person (Child classes: Customer, Employee)

<img width="520" alt="Screen Shot 2021-04-24 at 11 37 08 PM" src="https://user-images.githubusercontent.com/37784402/115983466-0daacd00-a556-11eb-83ca-8b57812201e7.png">

Diagram #2: Account (Child classes: CheckingAccount, SavingsAccount)

<img width="412" alt="Screen Shot 2021-04-24 at 11 44 27 PM" src="https://user-images.githubusercontent.com/37784402/115983604-0fc15b80-a557-11eb-9ba3-f5c68a81c4f7.png">

Diagram #3: Services (Child classes: CreditCard, Loan)

<img width="506" alt="Screen Shot 2021-04-24 at 11 46 17 PM" src="https://user-images.githubusercontent.com/37784402/115983646-4bf4bc00-a557-11eb-8159-fc48c1366918.png">

### Step 2: Write scripts in Python OOP manner based on the UML diagram
The code are devided into three parts based on it's parent classes.
You can find each part with `name.py` file saved.

### Step 3: Unit testing each part to ensure it's working properly and logically correct.

### Step 4: Data storage
For data storage, we have seleced Python Pickle.  Given it is primarily used in serializing and deserializing a Python object structure. In other words, it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network.



