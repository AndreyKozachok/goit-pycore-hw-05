from decorator import input_error


@input_error
def add_contact(args: list, contacts: dict) -> str: # Функція add_contact призначена для додавання нового контакту до словника контактів.
    if len(args) != 2:
        raise ValueError("Exactly 2 arguments (name and phone) are required.")
    name, phone = args # args, який є списком і містить ім'я та телефонний номер
    contacts[name] = phone #  який є словником, де зберігаються контакти
    return "Contact added."
    

@input_error
def change_contacts(args, contacts):
    if len(args) != 2:
        raise ValueError("Exactly 2 arguments (name and phone) are required.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Contacts not exist.")
    contacts[name] = phone
    return "Contacts updated."
   

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Exactly 1 argument (name) is required.")
    name = args[0]
    if name not in contacts:
        return "Contact does not exist"
    return contacts[name]
    
    
@input_error
def get_all_contatcs(contacts):
    if not contacts:
        return "Contacts are empty."
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output




    