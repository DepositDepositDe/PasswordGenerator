import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None
    
    # Generate password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt user for password length and complexity
    length = int(input("Enter password length: "))
    complexity = input("Enter complexity level (low/medium/high): ").lower()
    
    # Generate password
    password = generate_password(length, complexity)
    
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()



# Need to add a "new password"