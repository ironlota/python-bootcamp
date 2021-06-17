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
        self.name = name
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
        self.accounts = {}

    def register_account(self, account_name: str, balance: int):
        """Register account to customer

        Parameters:
            account (Account): account

        Returns: nothing
        """ 
        if account_name in self.accounts:
            print('The account with name {} exists'.format(account_name))
            return

        self.accounts[account_name] = Account(account_name, balance)

    def delete_account(self, account_name: str):
        """Delete account that is connected to customer

        Parameters:
            customer (Customer): customer
            account_name (str): account name
        """
        pass

    def get_account_by_name(self, name: str):
        """Get account by name

        Parameters:
            name (str): Name of customer

        Returns: 
            Account if exist else None
        """ 
        return self.accounts[name] if name in self.accounts else None

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
        self.customers = {}

    def register_customer(self, name: str):
        """Register customer with name

        Parameters:
            name (str): Name of customer

        Returns: 
            Account if exist else None
        """ 
        if name in self.customers:
            print('The customer with name {} exists'.format(account.name))
            return

        self.customers[name] = Customer(name)

    def get_customer_by_name(self, name: str):
        """Get account by name

        Parameters:
            name (str): Name of customer

        Returns: 
            Customer if exist else None
        """ 
        return self.customers[name] if name in self.customers else None

    def delete_customer(self, name: str):
        """Delete customer (with all of his/her accounts)

        Parameters:
            name (str): name of customer
        """
        pass

    def generate_report_per_customer(self, name: str):
        """Generate report of balance from all accounts for specific customer

        Tips:
        Calculate all accounts balance inside dictionary

        Parameters:
            name (str): name of customer
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

def get_customer(bank: Bank):
    customer = None
    while customer is None:
        customer_name = input('Input customer name (type q to return to menu): ')
        if customer_name == 'q':
            break
        customer = bank.get_customer_by_name(customer_name)
        if customer is None:
            print('Customer with name {} does not exist'.format(customer_name))
    return customer

if __name__ == '__main__':
    bank_name = input('Input bank name: ')
    bank   = Bank(bank_name)
    
    while True:
        menu(bank)
        choice = input('Choose menu: ')
        if choice == 'q':
            break
        elif int(choice) == 1:
            customer_name = input('Input new customer name: ')
            bank.register_customer(customer_name)
        elif int(choice) == 2:
            customer = get_customer(bank)
            if customer is not None:
                account_name = input('Input account name: ')
                balance = int(input('Input starting balance: '))
                customer.register_account(account_name, balance)
        elif int(choice) == 3:
            customer = get_customer(bank)
            if customer is not None:
                account_name = input('Input account name: ')
                account = customer.get_account_by_name(account_name)
                if account is not None:
                    money = int(input('Input money to store: '))
                    account.store(money)
        elif int(choice) == 4:
            customer = get_customer(bank)
            if customer is not None:
                account_name = input('Input account name: ')
                account = customer.get_account_by_name(account_name)
                if account is not None:
                    money = int(input('Input money to withdraw: '))
                    account.withdraw(money)
        elif int(choice) == 5:
            customer = get_customer(bank)
            if customer is not None:
                bank.generate_report_per_customer(customer)
        elif int(choice) == 6:
            customer = get_customer(bank)
            if customer is not None:
                account_name = input('Input account name: ')
                customer.delete_account(account_name)
        elif int(choice) == 7:
            customer_name = input('Input new customer name: ')
            bank.delete_customer(customer_name)

    print('Thank you for using our services!')



            
        
        
        