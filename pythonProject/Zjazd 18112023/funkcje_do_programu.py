user_dict = {
    'majki': '123',
    'Kamil': '124',
    'Kamil1': '234',
    'Kamil11': '765',
    'Kamil111': 'mama',
    'Kamil001': 'eee',
    'Rafcio': '876',
    'Betty': 'betty'
}

def is_user_available(user):
    if user not in user_dict.keys():
        print(f"Nazwa {user} jest dostępna")
        return True
    else:
        print(f"Nazwa {user} jest niedostępna")
        return False

def password_has_CAP_small_letter(password):
    if password != password.lower() and password != password.upper():
        print("Hasło posiada dużą i małą literę")
        return True
    print("Hasło nie posiada dużej lub małej litery")
    return False

def password_has_special_character(password):
    set_of_special_character = set(",./;[]\"\\'")
    if len(set(password) & set_of_special_character) > 0:
        return True
    return False

def password_has_digit(password):
    return any(char.isdigit() for char in password)

def suggest_username(user):
    return user + "1"

def add_user(user):
    while True:
        password1 = input("Podaj hasło: ")
        password2 = input("Potwierdź hasło: ")
        if password1 == password2 and password_has_CAP_small_letter(password1) \
                and password_has_digit(password1) and password_has_special_character(password1):
            user_dict[user] = password1
            break
        else:
            print("Źle, jeszcze raz")


