import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # !@#$%^&* etc.

    # Combine all characters
    all_chars = letters.upper() + letters.lower() + digits + symbols

    # Generate random password
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
        if length < 5:
            print("❌ Password length should be at least 4 characters!")
            return
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return

    password = generate_password(length)
    print(f"\n✅ Generated Password: {password}")

if __name__ == "__main__":
    main()
