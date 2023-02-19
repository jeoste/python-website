print('''This is a numerology program. Type the number you notice, and I''ll give you the signification
Type 'quit' to exit the program''')

userEntry = ""
flag = 0
while userEntry != 'quit':
    userEntry = input('Type your command: ').lower()
    commands = ["111", "1111", "222", "333", "444", "555", "quit"]
    if userEntry not in commands:
        print('I don''t understand, try again')
    elif userEntry == commands[0]:
        print('''The ones signify new beginnings. Whether you’re about to embark on a brand-new passage or you’re already on the right path, seeing 1111 coincides with that. And when you see it, experts say you should focus and use it as an indicator that you're on the right track.''')
