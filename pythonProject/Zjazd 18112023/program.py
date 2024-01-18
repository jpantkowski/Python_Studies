# dana jest baza użytkowników z hasłami
# program pozwala na dodanie użytkownika oraz zmianę hasła
# program sprawdza, czy nazwa użytkownika jest dostępna
# program wymaga dwukrotne wprowadzenia hasła przy dodawaniu nowego użytkownika
# program pyta, czy zakończyć, czy kontynuowac dodawanie użytkowników

# w przypadku niedostępnej nazwy użytkownika, program proponuję nazwę
# program sprawdza poziom skomplikowania hasła

from funkcje_do_programu import *
username = input("Podaj użytkownika: ")
while True:
    if is_user_available(username):
        add_user(username)
        break
    else
        print(f"Sugeruję nazwę {suggest_username(username)}")
        decision = input("Chcesz wprowadzić inną nazwę (N), czy skorzystać z zaproponowanej nazwy (P)?")
        if decision == "P":
            username = suggest_username(username):
        else:
            username = input("Podaj nową nazwę użytkownika")
print(user_dict)