
def first_character_type(pw):
    if not isinstance(pw, str) or not pw:
        return "unknown"

    ch = pw[0]

    if ch.isdigit():
        return "digit"
    if ch.isalpha():
        return "letter"
    return "symbol"


def split_credentials(text):
    if not isinstance(text, str) or ':' not in text:
        return "", ""

    user, password = text.split(':', 1)
    return user.strip(), password.strip()


def digit_ratio(pw):
    if not isinstance(pw, str) or not pw:
        return 0.0

    return sum(c.isdigit() for c in pw) / len(pw)


def main():
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    print("First Character Type:", result)

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    print("User and Password:", result)

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result)


if __name__ == "__main__":
    main()
