class Customer:
    """
    Customer
    """

    def __init__(self, name: str):
        """Construct a new 'Customer' object

        Parameters:
            name (str): Name of customer

        Returns: nothing
        """ 
        self.name = name

class Account:
    """
    Account
    """

    def __init__(self, name: str, balance: int):
        """Construct a new 'Account' object

        Parameters:
            name    (str): name of account
            balance (int): Balance of account

        Returns: nothing
        """
        self.balance = balance

    def store(self, money: int):
        """Store money into balance

        Tips:
        Should check if money inputted is more than zero or not

        Parameters:
            money (int): money to store

        Returns: nothing
        """
        pass
    
    def withdraw(self, money: int):
        """Store money into balance

        Tips:
        Should check if amount of money is lesser than balance

        Parameters:
            money (int): money to withdraw

        Returns: nothing
        """
        pass

class Bank:
    """
    Bank
    """

    def __init__(self, name: str):
        """Construct a new 'Bank' object

        Parameters:
            name (str): Name of bank

        Returns: nothing
        """
        self.name = name

        # Here is the data structure to save accounts
        # You may save the "Person name" as key
        # The value may varies, but to ease the problems
        # Save value of dictionary as dictionary of accounts
        self.accounts = {}

    def register_account(self, customer: Customer, account_name: str, balance: int):
        """Register customer's account with balance

        Parameters:
            customer (Customer): customer
            account_name (str): account name
            balance (int): account starting balance 
        """
        if customer.name not in self.accounts:
            self.accounts[customer.name] = {}
        self.accounts[customer.name][account_name] = Account(account_name, balance)

    def delete_customer(self, customer: Customer):
        """Delete customer (with all of his/her accounts)

        Parameters:
            customer (Customer): customer
        """
        pass

    def delete_account(self, customer: Customer, account_name: str):
        """Delete account that is connected to customer

        Parameters:
            customer (Customer): customer
            account_name (str): account name
        """
        pass

    def store(self, customer: Customer, account_name: str, money: int):
        """Store money to account that is connected to customer

        Tips:
        Call method `store` of account in here

        Parameters:
            customer (Customer): customer
            account_name (str): account name
            money (int): money to store
        """
        pass

    def withdraw(self, customer: Customer, account_name: str, money: int):
        """Withdraw money from account that is connected to customer

        Tips:
        Call method `withdraw` of account in here

        Parameters:
            customer (Customer): customer
            account_name (str): account name
            money (int): money to store
        """
        pass

    def generate_report_per_customer(self, customer: Customer):
        """Generate report of balance from all accounts for specific customer

        Tips:
        Calculate all accounts balance inside dictionary

        Parameters:
            customer (Customer): customer
        """
        pass

def menu(bank: Bank):
    print()
    print('-----------------')
    print('Welcome to Bank {}'.format(bank.name))
    print('-----------------')
    print('1. Create new customer')
    print('2. Create new customer\'s account')
    print('3. Store money to customer\'s account')
    print('4. Withdraw money from customer\'s account')
    print('5. Generate new report from customer (total balance)')
    print('6. Delete account connected to customer')
    print('7. Delete customer')
    print('q. Quit')
    print('-----------------')

def get_customer(customers: dict):
    customer_exist = False
    customer_name = ''
    while not customer_exist:
        customer_name = input('Input customer name (type q to return to menu): ')
        if customer_name == 'q':
            break
        customer_exist = customer_name in customers
        if not customer_exist:
            print('Customer does not exist!')
    return customers[customer_name] if customer_name in customers else None

if __name__ == '__main__':
    customers = {}
    bank_name = input('Input bank name: ')
    bank   = Bank(bank_name)
    
    while True:
        menu(bank)
        choice = input('Choose menu: ')
        if choice == 'q':
            break
        elif int(choice) == 1:
            customer_name = input('Input new customer name: ')
            customers[customer_name] = Customer(customer_name)
        elif int(choice) == 2:
            customer = get_customer(customers)
            if customer is not None:
                account_name = input('Input account name: ')
                balance = int(input('Input starting balance: '))
                bank.register_account(customer, account_name, balance)
        elif int(choice) == 3:
            customer = get_customer(customers)
            if customer is not None:
                account_name = input('Input account name: ')
                money = int(input('Input money to store: '))
                customer = customers[customer_name]
                bank.store(customer, account_name, money)
        elif int(choice) == 4:
            customer = get_customer(customers)
            if customer is not None:
                account_name = input('Input account name: ')
                money = int(input('Input money to withdraw: '))
                bank.withdraw(customer, account_name, money)
        elif int(choice) == 5:
            customer = get_customer(customers)
            if customer is not None:
                bank.generate_report_per_customer(customer)
        elif int(choice) == 6:
            customer = get_customer(customers)
            if customer is not None:
                account_name = input('Input account name: ')
                bank.delete_account(customer, account_name)
        elif int(choice) == 7:
            customer = get_customer(customers)
            if customer is not None:
                bank.delete_customer(customer)

    print('Thank you for using our services!')



            
        
        
        