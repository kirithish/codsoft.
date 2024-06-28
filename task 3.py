import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

