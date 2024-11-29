import string
import secrets
from datetime import datetime

# Function to generate a random password
def generate_password(length, include_special_char):
    """
    Args:
        length (int): Length of the password to generate.
        include_special_chars (str): Whether to include special characters in the password.

    Returns:
        str: A randomly generated password.
    """
    # define character pools for password
    letters = string.ascii_letters    # for uppercase and lowercase letters
    digits = string.digits     # for digits(0-9)
    special_char = string.punctuation    # for special characters

    # combine pools
    if include_special_char == "yes":
        pool = letters + digits + special_char
    else:
        pool = letters + digits

    # generate password
    password = "".join(secrets.choice(pool) for i in range(length))
    return password     # returns generated password

# Function to save password to a file with timestamps
def save_password(passwords):
    file_name = "my_passwords.txt"
    with open(file_name, 'a') as f:
        for password in passwords:
            timestamp = datetime.now().strftime("%Y-%m-%d\t%H:%M-%S")
            f.write(f"{timestamp}:  {password}\n")
        print("\nPassword(s) saved...")

# Main function to interact with the user for password generation.
def main():

    print("\n\tWelcome to The Random Password Generator\n")
    try:
        # prompt the user for desired length
        passwords = []
        while True:
            try:
                length = int(input("Enter password length:"))
                if length <= 0:
                    print("Password length must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input!")

        # ask the user for special characters
        while True:
            include_special_char = input("Wanna include special characters? (yes/no)").strip().lower()
            if include_special_char == "yes" or include_special_char == "no":
                break
            else:
                print("Invalid input!")

        # ask for the number of passwords
        num_of_pass = int(input("Enter the number of passwords you want to generate:"))
        # generate passwords
        for i in range(num_of_pass):
            password = generate_password(length, include_special_char)
            passwords.append(password)
            print(f"{i+1}. Generated password: {password}")

        # ask to save passwords
        choice = input("Wanna save password(s)? (yes/no)").strip().lower()
        if choice == "yes" or choice == "no":
            if choice == "yes":
                save_password(passwords)
        else:
            print("Invalid input!")
    finally:
        print("Thankyou for using it.Goodbye!")

# Entry point for the script
if __name__ == "__main__":
    main()
