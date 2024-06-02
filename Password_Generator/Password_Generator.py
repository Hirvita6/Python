import random
import string


def passwordGenerator(length):
    lowercaseLetters = string.ascii_lowercase
    uppercaseLetters = string.ascii_uppercase
    digits = string.digits
    specialCharacter = string.punctuation

    # combine all character sets
    allCharacters = lowercaseLetters + uppercaseLetters + digits + specialCharacter

    # Generate a random password
    password = "".join(random.choice(allCharacters) for _ in range(length))
    return password


def main():
    while True:
        try:
            # take a input for a length of password from user
            lengthOfPassword = int(input("Enter the Length of the Password : "))
            if lengthOfPassword <= 0:
                print("Invalid Length. Please enter a valid Positive length.")
                return

            else:
                password = passwordGenerator(lengthOfPassword)
                print(f"Generated Password : {password}")

        except ValueError:
            print("Invalid Input.")

        anotherPassword = input("Do you want to generate another password? (yes/no) : ")
        if anotherPassword.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


