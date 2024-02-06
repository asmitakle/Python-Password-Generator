import random
import string

def generate_password(length=12):
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each category
    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters)
    )

    # Fill the remaining length with random characters
    remaining_length = length - 4
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Shuffle the password characters for randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if num_passwords <= 0:
        print("Number of passwords must be greater than 0.")
        return
    
    try:
        len_password = int(input("Enter length of each password: "))
        if len_password < 12:
            raise ValueError
    except ValueError:
        print("Minimum password length should be 12")
        return
    
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(len_password)
        print(password)

if __name__ == "__main__":
    main()