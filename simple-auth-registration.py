import re
import pickle

DATA_FILE="user_data.pkl" #File to store usernames and passwords

#Load existing data from the file or create an empty dictionary
try:
    with open (DATA_FILE, 'rb') as file:
        user_data=pickle.load(file)
except FileNotFoundError:
    user_data={}

#Function to save user data to the file
def save_user_data():
    with open (DATA_FILE, 'wb') as file:
        pickle.dump(user_data, file)

#Function to display the menu
def display_menu():
    print("Welcome to the System")
    print ("1. Existing customers -Login")
    print ("2. New customers - Register")
    print ("0. Exit")

#Function to validate and create a username
def create_username(first_name, last_name, dob):
    username = (first_name[:3] + last_name[:3] + dob[-4:]).lower()
    return username

#Function to validate and create a password
def create_password():
    while True:
        password = input ("Enter a password (6-12 characters, at least one uppercase, one lowercase, and one digit)")
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,12}$', password):
            return password
        else:
            print ("Invalid password. Please follow the password requirments.")

#Function to handle existing customer login
def existing_customer_login():
    username = input ("Enter your username:")

    if username in user_data:
        stored_password=user_data[username]
        attempts=0
        while attempts < 3:
            password = input("Enter your password: ")
            if password ==stored_password:
                print("Login successful!")
                return
            else:
                attempts += 1
                print (f"Incorrect password. {3 - attempts} attempts left.")
        print("Access denied. Too many incorrect attempts.")
    else:
        print("Username not found. Access denied.")

#Function to handle new customer registration
def new_customer_registration():
    print("New Customer Registration:")
    first_name=input("Enter your first name:")
    last_name=input("Enter your last name:")
    dob=input("Enter your date of birth (DD/MM/YYYY):")

    username = create_username(first_name,last_name,dob)
    password = create_password ()

    user_data[username]=password
    save_user_data()

    print ("Registration successful!")
    print (f"Your username is: {username}")

#Main program
while True:
    display_menu()
    choice=input("Enter your choice (0-2):")

    if choice == "1":
        existing_customer_login()
    elif choice == "2":
        new_customer_registration ()
    elif choice == "0":
        print ("Exiting the system. Goodbye!")
        break
    else:
        print ("Invalid choice. Please enter a valid option.")