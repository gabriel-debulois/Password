import string
import hashlib

password = ""


def user_input():
    global password
    password = input("Veuillez entrer votre mot de passe: ")


def in_password_punctuation():
    for i in password:
        if i in string.punctuation:
            return True


def in_password_lower():
    for i in password:
        if i in string.ascii_lowercase:
            return True


def in_password_upper():
    for i in password:
        if i in string.ascii_uppercase:
            return True


def in_password_digit():
    for i in password:
        if i in string.digits:
            return True


def h():
    h = hashlib.new('sha256')
    h.update(password.encode())


def check_password():
    global password

    while True:
        check_condition = (len(password) >= 8,
                           in_password_punctuation(),
                           in_password_lower(),
                           in_password_upper(),
                           in_password_digit())

        if all(check_condition):
            h()
            print("Mot de passe valide")
            break

        else:
            print("Mot de passe invalide")
            user_input()



user_input()
check_password()

