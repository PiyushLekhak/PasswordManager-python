from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
encryptionKey = Fernet.generate_key()
cipherSuite = Fernet(encryptionKey)


def storeAccountDetails():
    accountName = input("Enter the account name: ")
    accountPassword = input("Enter the password: ")

    # Encrypt the password
    encryptedPassword = cipherSuite.encrypt(accountPassword.encode())

    # Store the account name and encrypted password in a file
    with open("accountDetails.txt", "a") as file:
        file.write(f"{accountName},{encryptedPassword.decode()}\n")


def retrieveAccountDetails():
    # Read the accounts and passwords from the file
    with open("accountDetails.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        accountName, encryptedPassword = line.strip().split(",")

        # Decrypt the password
        decryptedPassword = cipherSuite.decrypt(encryptedPassword.encode()).decode()

        print(f"Account Name: {accountName}, Password: {decryptedPassword}")


def mainMenu():
    while True:
        print("1. Store a password")
        print("2. View passwords")
        print("3. Exit")
        userChoice = input("Enter your choice: ")

        if userChoice == "1":
            storeAccountDetails()
        elif userChoice == "2":
            retrieveAccountDetails()
        elif userChoice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the main function
if __name__ == "__main__":
    mainMenu()
