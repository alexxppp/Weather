# weather_app.py
import os
import random
import string
import requests
import logging
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from geonamescache import GeonamesCache


# Configure logging to suppress debug output from the requests library
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Database
db = SQL('sqlite:///weather.db')

# Constants and global variables
PASSWORD_LENGTH = 12

def main():
    # Main logic loop
    while True:
        print("Do you have an account?")
        option = get(["1", "2"], "1. Yes, login\n2. No, register\n")

        if option == "1":
            username = login_menu()
        else:
            register_menu()
            username = login_menu()

        # User's main menu
        while username:
            clear()
            # If user has favorites
            if favorites := db.execute("SELECT * FROM favorites WHERE username = ?", username):
                print("### Your favorites ###\n")
                for fav in favorites:
                    print(f"{fav["location"]}: {fetch(fav["location"])[2]} degrees Celsius")
            print("\n### Menu ###")
            print("\nWhat would you like to do?")
            option = get(
                ["1", "2", "3", "4"], "1. Consult current weather of a location\n2. Add/Remove favorite location\n3. Log out\n4. Exit\n")
            # Options management
            if option == "1":

                location = input(
                    "Type the location (or type 'l' and enter if you are feeling lucky): ")
                if location.lower() == "l":
                    location = im_feeling_lucky()
                data = fetch(location)
                if data:
                    print(f"At the moment in {data[1]} there are {data[2]} degrees Celsius")
                else:
                    print("Location not available")
                tm = input("Enter to continue.")

            elif option == "2":

                action = get(["1", "2"], "1. Add, 2. Delete\n")
                location = input("Type the location: ")
                to_from = ""
                if action == "1":
                    action, to_from = "add", "to"
                else:
                    action, to_from = "remov", "from"
                if favorite(action, username, location):
                    print(f"{location} {action}ed {to_from} your favorites.")
                tm = input("Enter to continue.")

            elif option == "3":

                print("Logged out.")
                tm = input("Enter to continue.")
                username = None

            elif option == "4":

                print("Exiting the application.")
                return

            clear()


# IMPORTANT HELPERS FUNCTIONS
# To get a value inside a list, and keep prompting if not given
def get(options, message):
    value = input(message)
    if value in options:
        return value
    print("Invalid option. Try again.")
    return get(options, message)


# To clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# To manage the registration and make sure the user registers correctly
def register_menu():
    print("### REGISTRATION ###")
    username = input("Provide a username: ")
    password = input("Provide a password (or type 'r' and enter to generate a random password): ")

    if password.lower() == "r":
        password = generate_password()
        rep_password = password
        print("Your password is: ", password, ". Please save it.")
    else:
        rep_password = input("Repeat your password: ")

    if not register(username, password, rep_password):
        return register_menu()
    print("Successfully registered. Please, login.")


# To manage the registration and make sure the user registers correctly
def login_menu():
    print("### LOGIN ###")
    username = input("Your username: ")
    password = input("Your password: ")

    valid, username = login(username, password)
    if not valid:
        return login_menu()
    return username


# To generate a random 12 character password
def generate_password():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(PASSWORD_LENGTH))


# To register the user in the system
def register(username, password, rep_password):
    if not username or not password or not rep_password:
        print("Please fill out all the fields.")
        return False
    if db.execute("SELECT username FROM users WHERE username = ?", username):
        print("Username already taken.")
        return False
    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return False
    if password != rep_password:
        print("Passwords must be the same")
        return False

    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   username, generate_password_hash(password))
        return True
    except:
        print("Error with database query. Please try again.")
        return False


# To log the user in the app
def login(username, password):
    if not username or not password:
        print("Please fill out all the fields.")
        return False, None

    user = db.execute("SELECT * FROM users WHERE username = ?", username)
    if not user or not check_password_hash(user[0]["password"], password):
        print("Username or password not correct.")
        return False, None

    return True, username


# To retrieve data from the weatherAPI for location and temperature
def fetch(location):
    if not location:
        print("Please fill out all the fields.")
        return None

    params = {"key": "64e6702d54b34e40999175829240608", "q": location.strip().title(), "aqi": "no"}
    response = requests.get("http://api.weatherapi.com/v1/current.json", params=params)

    if response.status_code == 200:
        loc = response.json()['location']['name']
        temperature = response.json()['current']['temp_c']
        return True, loc, temperature

    print("Invalid location.")
    return None


# Returns a random location from a list of aprox. 7.000 locations
def im_feeling_lucky():
    return random.choice([city["name"] for city in GeonamesCache().get_cities().values()])


# To add/delete a favorite city to/from the database
def favorite(action, username, location):
    if not fetch(location):
        return False

    try:
        if action == "add":
            db.execute("INSERT INTO favorites (username, location) VALUES (?, ?)", username, location)
        elif action == "remov":
            db.execute("DELETE FROM favorites WHERE username = ? AND location = ?", username, location)
        return True
    except:
        print("Error with database query. Please try again.")
        return False


# To call main
if __name__ == "__main__":
    main()
