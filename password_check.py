passwrod = input("Enter your password: ")
while len(passwrod) <= 2:
    print("The password cannot less than 3 characters")
    passwrod = input("Enter your password: ")
print("Your password:","*"*len(passwrod))