from System_Random.systemRandom import systemRandom
import secrets

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