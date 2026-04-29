contact_list = [['Jerry Seinfeld', 'seinfeld@yahoo.com', '22 33 4567 4587'],
                ['Harry Potter', 'sorcecode@gmail.com', '+11 22 3456 7890']]
def intro():
    print('Contact Manager\n')
    print('COMMAND MENU')
    print('list    - Display all contacts')
    print('view - View a contact')
    print('add   - Add a contact')
    print('del    - delete a contact')
    print('exit   - Exit program')
    print()

def display(contact_list):
    print('Command: list')
    if len(contact_list) == 0:
        print('There are no contacts in the list.\n')
        return
    else:
        i = 1
        for contact in contact_list:
            print(str(i)+'. ' + contact[0])
            i += 1
        print()

def view(contact):
    print('Command: view')
    number = int(input('Number: '))
    if number < 1 or number > len(contact):
        print('Please enter a valid number.\n')
    else:
        print('Name: '  + contact[number - 1][0])
        print('Email: ' + contact[number - 1][1])
        print('Phone: ' + contact[number - 1][2])
        print()

def add(contact_list):
    print('Command: add')
    name  = input('Name: ')
    email = input('Email: ')
    phone = input('Phone: ')
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
    print(contact[0] + ' was added.\n')

def delete(contact_list):
    print('Command: del')
    number = int(input('Number: '))
    if number < 1 or number > len(contact_list):
        print('Please enter a valid number.\n')
    else:
        contact = contact_list.pop(number - 1)
        print(contact[0] + ' was deleted.\n')

def main():
    intro()

    while True:
        command = input('Command: ')
        print()
        if command.lower() == 'list':
            display(contact_list)
        elif command.lower() == 'view':
            view(contact_list)
        elif command.lower() == 'add':
            add(contact_list)
        elif command.lower() == 'del':
            delete(contact_list)
        elif command.lower() == 'exit':
            print('Bye!')
            break
        else:
            print('That is not a valid command. Please try again. \n')

if __name__ == '__main__':
    main()

