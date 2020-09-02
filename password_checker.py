import requests
import hashlib
import re


def is_password_complex_enough(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\W]{8,}$"
    return bool(re.findall(pattern, password))


def hash_user_password(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest()


def get_password_from_txt(file):
    f = open(file, "r")
    return f.read()


def get_pwned_password(first_5_hash_chars):
    request = requests.get(
        f'https://api.pwnedpasswords.com/range/{first_5_hash_chars}')
    return request.text


def if_pwd_pawned():
    password_value = get_password_from_txt("pwd.txt")
    if is_password_complex_enough(password_value):
        hashed_password = hash_user_password(password_value)

        first_5_chars, tail = hashed_password[:5], hashed_password[5:]
        results = get_pwned_password(first_5_chars)

        for line in results.splitlines():
            splited_result = line.split(":")

            if splited_result[0] == tail.upper():
                print(
                    f'You\'re password had beed pawned {splited_result[1]} times. Maybe you should change your password to more secure one')
            else:
                print("Great! You have really strong password")
                break
    else:
        print("Make sure that your password contains at least 1 upper character, 1 digit and minimum 8 characters long and return to check if your password was pawned")


if __name__ == "__main__":
    if_pwd_pawned()
