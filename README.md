# Finance

This is a Python command-line project for managing finances.
It allows users to register them and perform various financial operations, such as checking balance, adding balance,
transferring money, and viewing transfer history.
It is built using a PostgreSQL database and stores all the necessary data in tables.
# Features
- User Registration: Register new users by providing their personal information.

- Money Transfers: Perform money transfers between registered users.
# Technologies Used
**Programming Language:** Python

**Database:** PostgreSQL

# Installation and Setup
To use the Finance project, follow these steps:

Clone the repository:  
```bash
git clone https://github.com/shohcodes/finance.git
```
Change into the project directory:
```bash
cd finance
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```
Set up the PostgreSQL database and configure the database connection details

# Usage
To run the Finance project, execute the following command:
```bash
python main.py 
```

The application will present you with a menu where you can choose various options depending on whether you are logged in or not.

# Menu Options
If you are not logged in, you will see the following options:
- Login
- Register

If you are logged in, you will see the following options:
- Show balance
- Top up the balance
- Transfer money
- Transfer history
- Log out

**LOGIN**

To log in, select the 'Login' option and enter your username and password when prompted.

**REGISTER**

To register a new user account, select the 'Register' option and provide the required information, including first name, last name, username, password, and phone number.

**SHOW BALANCE**

This option allows you to view your current balance.

**TOP UP BALANCE**

You can use this option to add funds to your account. Enter the desired amount when prompted.

**TRANSFER MONEY**

To transfer money to another user, enter the receiver's username and the amount to be transferred.

**TRANSFER HISTORY**

This option displays the history of all previous money transfers.

**LOG OUT**

Selecting this option will log you out of your current session.

# Contributing
Contributions to the Finance project are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on the GitHub repository.


## Authors

- [shohcodes](https://www.t.me/shohcodes)
