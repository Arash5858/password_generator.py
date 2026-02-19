import random
import string


def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generate a secure random password based on selected options.
    """

    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password


if __name__ == "__main__":
    print("Smart Password Generator")
    print("------------------------")

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length=length)
        print(f"\nGenerated Password:\n{password}")
    except ValueError as error:
        print(f"Error: {error}")
        
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length=length)
        print(f"\nGenerated Password:\n{password}")
    except ValueError as error:
        print(f"Error: {error}")

