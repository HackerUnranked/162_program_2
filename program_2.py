# Obtain these things about the user
# 1. last name
# 2. pet's name
# 3. birthdate
# 4. favorite number
#
# Constraints
# 1. Each of the things should not be greater than 40 characters
# 2. The password must start with a letter
# 3. There must be atleast 1 uppercase character
# 4. There must be at least one symbol
# 5. There can't be any spaces or tabs
# 6. If the user fails any 5 of the above then ask them to re-enter again
# 7. After 5 failures remind the users of the rule before trying again 

# Password Strength
# 1. WEAK: The password is weak if the first letter is the same as the last name
# 2. WEAKER: If the birth year is in the password it is also weak
# 3. WEAKER: If the character's in the pet's name appear in the same order
# 4. WEAKER: Each time the favorite number appears


def contains_uppercase(words: str):

    for x in words:
        if x.isupper():
            return True

    return False


def findss(c: str, b: str):
    
    found =  False
    idx = -1

    for x in range(len(c)):
        for y in range(len(b)):
            # we found the letter
            found = False
            if c[x] == b[y]:
                # is the letter in the correct sequence?
                if idx < y:
                    idx = y
                    found = True
                    break
                else:
                    found = False
        
        if found == False:
            break
        
    return found

def main():
    start_prog = True
    print("\n\nPlease enter your password information, below are the following contsraints:")
    print("Each of the things should not be greater than 40 characters")
    print("The password must start with a letter")
    print("There must be atleast 1 uppercase character")
    print("There must be at least one symbol")
    print("There can't be any spaces or tabs")
    print("Press Q to quit")
    
    last_name = input("Enter your Last Name: ")
    pet_name = input("Enter your pet's name: ")
    bday = input("Enter your birthdate ex: 11/11/11 : ")
    fav_num = input("Enter your favorite number :")
    num_wrong = 0
    
    while start_prog:
        
        pw = input("Enter your password: ")
        
        if len(pw) > 40:
            print("Greater than 40 characters")
        elif ord(pw[:1]) < 65 or ord(pw[:1]) > 122:
            print("First character is not a letter")
        elif contains_uppercase(pw) == False:
            print("No Uppercase")
        elif pw.isalnum() == True:
            print("No special characters")
        elif " " in pw:
            print("Has spaces")
        elif len(pw) == 1:
            if pw == 'Q':
                return

main()