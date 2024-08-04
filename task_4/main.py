from contact_manager import (
    add_contact,
    change_contacts,
    show_phone,
    get_all_contatcs
)

def parse_input(user_input):
    cmd, *args = user_input.split() # Вона повертає перше слово як команду cmd та решту як список аргументів *args, розділяє рядок на слова.
    cmd = cmd.strip().lower() # видаляє зайві пробіли навколо команди та перетворює її на нижній регістр
    return cmd, *args



def main():
    contacts = {} # додали словник з контактами
    print("Walcome to the assistense bot !")
    while True:
        command = input("Enter a command: ")
        command, *args = parse_input(command)

        if command in ["close", "exit"]:
            print("Good bay!")
            break
        elif command == "hello":
            print("How can I help you ?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contacts(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(get_all_contatcs(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



