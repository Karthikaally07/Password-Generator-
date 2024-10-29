import secrets 
import string 

def generate(length=10, letters=True, digits=True , special_char=True):
    selection = string.ascii_letters
    if digits:
        selection += string.digits
    if special_char :
        selection += string.punctuation
    password_generation = ''.join(secrets.choice(selection)for _ in range(length))
    return password_generation
input = int(input("Enter the Password length :"))
password_generation = generate(input)
print("Password Generation",password_generation)
     