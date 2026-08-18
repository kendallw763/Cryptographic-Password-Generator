import time
from System_Random.systemRandom import tokenRandom
from Password_Generation.passwordGeneration import passwordGeneration, password_strength_check, password_length_check

# ------------------------------------------------------------
# INTERACTIVE USER LOOP
# ------------------------------------------------------------
def user_interface():
    token_gen = tokenRandom()

    while True:
        print("============================================")
        print("======= Password/Hex token Generator =======")
        print("1. Generate Password")
        print("2. Generate Hex Token ")
        print("3. Exit Program")
        print("============================================ \n ")

        choice = input("Select an option (1-3): ").strip()

        # ------------------------------------------------------------
        # OPTION 1: PASSWORD GENERATION
        # ------------------------------------------------------------
        if choice == "1":
            length_input = input("Enter password length (or press Enter for default): ").strip()

            if length_input == "":
                length = password_length_check()
            else:
                length = int(length_input)

            password = passwordGeneration(length)
            strength = password_strength_check(password)

            print("\nGenerated Password:", password)
            print("Password Strength:", strength)

        # ------------------------------------------------------------
        # OPTION 2: TOKEN GENERATION
        # ------------------------------------------------------------
        elif choice == "2":
            nbytes = int(input("Enter number of bytes for token: "))
            token = token_gen.generate(nbytes)
            print("\nGenerated Token:", token)

        # ------------------------------------------------------------
        # OPTION 3: EXIT
        # ------------------------------------------------------------
        elif choice == "3":
            print("\nExiting program...\n" )
            time.sleep(1.50)
            print("\nThank you for using the Secure Generator. Goodbye!")
            break

        else:
            print("Invalid selection. Try again.")