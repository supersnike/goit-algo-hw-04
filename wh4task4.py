def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add username phone"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

def change_contact_phone(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change username phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact '{name}' changed."
    else:
        return f"Contact '{name}' not found."

def display_contact_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone username"
    name = args[0]
    if name in contacts:
        return f"Phone number for contact '{name}': {contacts[name]}"
    else:
        return f"Contact '{name}' not found."

def display_all_contacts(contacts):
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact_phone(args, contacts))
        elif command == "phone":
            print(display_contact_phone(args, contacts))
        elif command == "all":
            display_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
