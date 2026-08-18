import time
from System_Random.systemRandom import tokenRandom
from Password_Generation.passwordGeneration import passwordGeneration, password_length_check, password_strength_check
from User_Menu.interface import user_interface

def main(): 
    symbols = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏" ]
    i = 0
    for _ in range(11):
        i = (i + 1) % len(symbols)
        print("\r\033[K%s Loading... " % symbols[i], flush=True, end=" ")
        time.sleep(.3)
    print(" \n ")
    
if __name__ == '__main__':
    main()
    user_interface()
    password_length_check()
    password_strength_check()
    passwordGeneration()
    tokenRandom()
   
