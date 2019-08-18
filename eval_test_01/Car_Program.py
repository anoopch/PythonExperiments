# A program to mimic the car functions as below
# Start - to start the car
# Stop  – to stop the car
# Quit  – to exit


def start_car():
    print('car started....... ready to go')


def stop_car():
    print('car stopped')


def invalid_operation():
    print('I don’t understand')


def stop_program():
    print('program terminated')


def print_help():
    print('\nStart - to start the car\nStop  – to stop the car\nQuit  – to exit\n')


print_help()
while True:
    input_choice = str(input('> ')).lower()
    if input_choice == 'start':
        start_car()
    elif input_choice == 'stop':
        stop_car()
    elif input_choice == 'help':
        print_help()
    elif input_choice == 'quit':
        stop_program()
        break
    else:
        invalid_operation()
