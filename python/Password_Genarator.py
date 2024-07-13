import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("~~~ Password Generator ~~~")
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Length should be greater than zero.")
            return
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
