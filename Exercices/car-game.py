print('''Here's the commands you can type
- help
- start
- stop
- quit
''')

userEntry = ""
flag = 0
while userEntry != 'quit':
    userEntry = input('Type your command: ').lower()
    commands = ["help", "start", "stop", "quit"]
    if userEntry not in commands:
        print('I don''t understand, try again')
    elif userEntry == commands[0]:
        print('''start: start the car
        stop: stop the car
        quit: quit the program''')
    elif userEntry == commands[1] and flag == 0:
        print('Car started')
        flag = 1
    elif userEntry == commands[1] and flag == 1:
        print('Car already started')
    elif userEntry == commands[2] and flag == 1:
        print('Car has stopped')
        flag = 0
    elif userEntry == commands[2] and flag == 0:
        print('Car has already stopped')
    elif userEntry == commands[3]:
        print('Game will quit')
        break
