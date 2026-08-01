import secrets
import time

# ------------------------------------------------------------
# PROGRAM INTRO
# ------------------------------------------------------------
def main(): 
    print('\nCryptologically secure generator ~')
    print('Used for managing data such as passwords, account auth, security tokens, and related secrets')
    print('\n...Loading')
    time.sleep(1.50)
    print('\nReady...')

# ------------------------------------------------------------
# SECURE RANDOM MODULE
# ------------------------------------------------------------
class systemRandom:
    def choose_random_element(self, sequence):
        return secrets.choice(sequence)

    def random_below(self, upper_limit):
        return secrets.randbelow(upper_limit)

    def random_bits(self, bit_count):
        return secrets.randbits(bit_count)

    def generate_token_hex(self, nbytes):
        return secrets.token_hex(nbytes)

# ------------------------------------------------------------
# TOKEN GENERATION (RAW BYTES → HEX)
# ------------------------------------------------------------
class tokenRandom:
    def generate(self, nbytes):
        RAW_BYTES = secrets.token_bytes(nbytes)
        HEX_STRING = RAW_BYTES.hex()
        return HEX_STRING

# ------------------------------------------------------------
# CHARACTER POOLS
# ------------------------------------------------------------
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SYMBOLS = '!@#$%^&*()-=_+}[{|?/<>'
ALL_POOLS = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS

# ------------------------------------------------------------
# PASSWORD LENGTH RULES
# ------------------------------------------------------------
def password_length_check(user_length=None):
    if user_length is not None:
        return user_length
    return secrets.randbelow(5) + 12  # default range 12–16

# ------------------------------------------------------------
# PASSWORD GENERATION
# ------------------------------------------------------------
def passwordGeneration(length):
    secure = systemRandom()
    PASSWORD_CONTAIN = []

    # Fill password with random characters
    for _ in range(length):
        PASSWORD_CONTAIN.append(secure.choose_random_element(ALL_POOLS))

    # Helper: check if password contains at least one char from a pool
    def contains(pool):
        return any(c in pool for c in PASSWORD_CONTAIN)

    MISSING = []

    if not contains(UPPERCASE):
        MISSING.append(UPPERCASE)

    if not contains(LOWERCASE):
        MISSING.append(LOWERCASE)

    if not contains(DIGITS):
        MISSING.append(DIGITS)

    if not contains(SYMBOLS):
        MISSING.append(SYMBOLS)

    # Fix missing categories by replacing random positions
    for pool in MISSING:
        INDEX = secrets.randbelow(length)
        PASSWORD_CONTAIN[INDEX] = secure.choose_random_element(pool)

    return "".join(PASSWORD_CONTAIN)

# ------------------------------------------------------------
# PASSWORD STRENGTH CHECKER
# ------------------------------------------------------------
def password_strength_check(password):
    PASS_SCORE = 0

    if any(c in UPPERCASE for c in password): PASS_SCORE += 1
    if any(c in LOWERCASE for c in password): PASS_SCORE += 1
    if any(c in DIGITS for c in password): PASS_SCORE += 1
    if any(c in SYMBOLS for c in password): PASS_SCORE += 1

    if PASS_SCORE == 1:
        return "Weak"
    elif PASS_SCORE in (2, 3):
        return "Moderate"
    else:
        return "Strong"

# ------------------------------------------------------------
# INTERACTIVE USER LOOP
# ------------------------------------------------------------
def user_interface():
    token_gen = tokenRandom()

    while True:
        print("\n=== Secure Generator Menu ===")
        print("1. Generate Password")
        print("2. Generate Token (hex)")
        print("3. Exit Program")

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

# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
    user_interface()
   
