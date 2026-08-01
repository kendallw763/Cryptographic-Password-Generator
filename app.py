import secrets
import time

def main(): 
       print( 
             '\nCryptologically secure generator ~\n' 
             'Used for managing data such as passwords, account auth, security tokens, and related secrets')
       print(' \n...Loading') 
       time.sleep(1.50) 
       print('\nReady...')

# ------------------------------------------------------------## --------------------------
#MODULE FOR GENERATING RANDOM 'SECURE' strings, numbers, bits, and bytes using CRYPOGRAPHY 
# ------------------------------------------------------------## --------------------------
class systemRandom:
    def choose_random_element(self, sequence):
        return secrets.choice(sequence) # Randomly choses element (non empty).
    # -------------------------------------------------------------------------
    def random_below(self, upper_limit):
        return secrets.randbelow(upper_limit) # Randomly selected in within [0, upper_bonds].
    # ---------------------------------------------------------------------------------------       
    def random_bits(self, bit_count):
        return secrets.randbits(bit_count) # Randomly seleced non negative int with random bits 
    # ------------------------------------------------------------------------------------------       
    def generate_token_hex(self, nbytes):
        return secrets.token_hex(nbytes) # Randomly selects a byte string    
    # ------------------------------------------------------------------------------------------       
      

# ------------------------------------------------------------
# TOKEN GENERATION LOGIC (token_hex)
# ------------------------------------------------------------
class tokenRandom:
    def generate(self, nbytes):
      RAW_BYTES = secrets.token_bytes(nbytes) # Convert each byte into two hexidecimal chars
# -------------------------------------------------------------------------------------------       
      HEX_STRING = RAW_BYTES.hex() # Combine all hex characters into one long string
# ------------------------------------------------------------------------------------      
      return HEX_STRING

# ------------------------------------------------------------
# CHARACTER POOLS FOR PASSWORD / TOKEN CREATION
# ------------------------------------------------------------
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '012344567890'
SYMBOLS = '!@#$%^&*()-=_+}[{|?/<>'
ALL_POOLS = UPPERCASE + LOWERCASE.lower() + DIGITS + SYMBOLS # Random password generated from pools
# -----------------------------------------------------------------------------------------------------


# ------------------------------------------------------------
# PASSWORD LENGTH RULES
# ------------------------------------------------------------
def password_length_check(user_length = None):
    if user_length is not None:
        return user_length
    return secrets.randbelow(5) + 12 # Verifies user input is not none, within 0 & upper bounds 
# ----------------------------------------------------------------------------------------------        
        
# ------------------------------------------------------------
# PASSWORD GENERATION LOGIC
# ------------------------------------------------------------

def passwordGeneration(length):
    secure = systemRandom()
    
    PASSWORD_CONTAIN = [ ]
    for _ in range(length):
        PASSWORD_CONTAIN.append(secure.choose_random_element(ALL_POOLS))

    # ensure catagrory coverage
    # create a function named 'contains'
    def contains(pool):
        return any(c in pool for c in PASSWORD_CONTAIN)
    
    MISSING = []

    if not contains(UPPERCASE):  
        MISSING.append(UPPERCASE)
            
    if not contains(LOWERCASE):
        MISSING.append(LOWERCASE)
    
    if not contains(DIGITS):
        MISSING.append(DIGITS)
        
    if not contains.append(SYMBOLS):
        MISSING.append(SYMBOLS)            
        
    for pool in MISSING:
        INDEX = secure.choose_random_element(length)
        PASSWORD_CONTAIN [INDEX] = secure.choose_random_element(pool)
    return "".join(PASSWORD_CONTAIN) 

# ------------------------------------------------------------
# PASSWORD STRENGTH CHECKER
# ------------------------------------------------------------
def password_stregnth_check(password):
# - Start with a score of zero.
    PASS_SCORE = 0
#
# - Check if the password contains uppercase letters.
#       If yes, add one point.
    if any(c in password for c in UPPERCASE):PASS_SCORE +=1
    if any(c in password for c in LOWERCASE):PASS_SCORE +=1
    if any(c in password for c in DIGITS):PASS_SCORE +=1        
    if any(c in password for c in SYMBOLS):PASS_SCORE +=1        

    if PASS_SCORE == 1:
        return "Weak"
     
    elif PASS_SCORE (2,3):
        return "Moderated"
   
    else:
        return "Strong"
 
if __name__ == '__main__':
    main()