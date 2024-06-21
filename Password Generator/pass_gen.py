import random
import string


def generate_password(length):
    # Define the character sets to use 
    character = string.ascii_letters + string.digits

    # Generate a random password
    password = ''.join(random.choice(character) for i in range(length))
    return password


def main():
    # Ask the user for the desired length of the PASSWORD
    while True:
        try:
            length = int(input("Enter the length for the password: "))
            if length < 1:
                print("PLEASE ENTER A VALID NUMBER")
            else:
                break
        except ValueError:
            print("INVALID INPUT")
    
    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password is: {password}")


if __name__ == "__main__":
    main()