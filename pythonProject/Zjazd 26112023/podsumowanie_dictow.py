dictionary = {
    "key" : "value",
    "key2" : "value2"
}

# porównanie do seta:
a_set = {"value", "value2", "value3"}

# inicjaizacja - przy stworzeniu z pustymi klamrami {} python domyślnie stworzy słownik:
empty_dict = {}
empty_set = set()

# znamy "key" i chcemy value:
print(dictionary["key"])

# znamy "value" i chcemy key 1 - tutaj zwrócony zostanie tylko pierwszy klucz:
for key in dictionary:
    if dictionary[key] == "value":
        print(key)
        break

# znamy "value" i chcemy key 2 - tutaj tworzymy listę pasujących kluczy:
list_of_matching_keys = []
for key in dictionary:
    if dictionary[key] == "value":
        list_of_matching_keys.append(key)
print(list_of_matching_keys)

# znamy "value" i chcemy key 3 - klasyczne iterowanie po tuplach:
list_of_matching_keys = []
for key, value in dictionary.items():
    if value == "value":
        list_of_matching_keys.append(key)
print(list_of_matching_keys)