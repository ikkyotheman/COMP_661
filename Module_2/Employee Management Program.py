def display_menu():
    print('Welcome to the Employee Management Program')
    print()
    print('COMMAND MENU')
    print('show - Show all employees')
    print('add - Add an employee')
    print('del - delete an employee')
    print('exit - Exit the program')

def display():
    print(employee_list)

def add():
    new = input('Who do you want to add?')
    employee_list.extend([new])
    print(employee_list)
def delete():
    remove = input('Who do you want to delete?')
    employee_list.remove(remove)
    print(employee_list)
def main():
    employee_list = ['Peter Kindrachuk',
                     'Heather Kindrachuk',
                     'Master Jin'
                     'Roy Orbison']
    display_menu()
    while True:
        command = input('Enter a command: ')
        if command.lower() == 'show':
            display(employee_list)
        elif command.lower() == 'add':
            add(employee_list)
        elif command.lower() == 'del':
            delete(employee_list)
        elif command.lower() == 'exit':
            break
        else:
            print('That is not a valid command. Please try again. \n')

if __name__ == '__main__':
    main()