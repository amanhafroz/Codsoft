import string
import random

if __name__ == "__main__":
    easy = string.ascii_lowercase
    medium = string.ascii_lowercase + string.ascii_uppercase + string.digits
    hard = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
   
    passlen = int(input("Enter Password Length : "))
    complexity = input("Enter the Complexity (easy / medium / hard): ").lower()
    if complexity == "easy":
        chars = easy
    elif complexity == "medium":
        chars = medium
    elif complexity == "hard":
        chars = hard
    else:
        print("Invalid!! choose easy, medium ,hard ")
        exit()
    
    pwd = ''.join(random.choice(chars) for _ in range(passlen))
    print("Generated Password : ",pwd)