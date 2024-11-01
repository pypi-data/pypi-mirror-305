from ratelimit import limits, sleep_and_retry
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import time
import re

PEPPER = "jdafhpoahsofdashjp"



def is_strong_password(passW):
    # Check password length
    if len(passW) < 12:
        return False, "Password must be at least 12 characters long."

    # Check for uppercase
    if not re.search(r'[A-Z]', passW):
        return False, "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r'[a-z]', passW):
        return False, "Password must contain at least one lowercase letter."

    # Check for digit
    if not re.search(r'[0-9]', passW):
        return False, "Password must contain at least one digit."

    # Check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', passW):
        return False, "Password must contain at least one special character."

    return True, "Password is strong."



ONE_MINUTE = 60

# Initialize the PasswordHasher with custom parameters
ph = PasswordHasher(
    time_cost=12,          # Number of iterations
    memory_cost=2 ** 16,    # Memory cost
    parallelism=1,          # Number of parallel threads
    hash_len=64,            # Length of the resulting hash
    salt_len=16
)

# Rate-limited function to hash the password
@sleep_and_retry  # Ensures that the function sleeps if the limit is reached
@limits(calls=5, period=ONE_MINUTE)
def bis_hash(name, passwrd):
    combined_input = name + passwrd + PEPPER
    return ph.hash(combined_input)

# Function to verify a password
def verify_password(stored_hash, name, entered_password):
    # Combine the username and entered password
    combined_input = name + entered_password + PEPPER
    try:
        ph.verify(stored_hash, combined_input)
        return True
    except VerifyMismatchError:
        return False

# Simulate user reg
userName = input("Username: ").strip()  # either email or username
password = input("Password: ").strip()

is_valid, message = is_strong_password(password)

hashed_password = None

if is_valid:
    try:
        hashed_password = bis_hash(userName, password)
        print("Hashed Password:", hashed_password)
    except Exception as e:
        print("Password hashing failed:", str(e))
else:
    print(f"Invalid password: {message}")


if hashed_password:
    # Simulate login
    login_userName = input("Enter your username: ").strip()
    login_password = input("Enter your password: ").strip()

    # Verify password
    is_password_valid = verify_password(hashed_password, login_userName, login_password)

    if is_password_valid:
        print("Password is valid! You are logged in.")
    else:
        print("Invalid password. Please try again.")


    def simulate_hashing(username, password):
        for i in range(7):  # Simulate Rate limiting
            try:
                print(f"\nAttempt {i + 1}")
                hashed_value = bis_hash(username, password)
                print("Hashed Password:", hashed_value)
            except Exception as e:
                print("Error:", e)
            time.sleep(1)

simulate_hashing(userName, password)
