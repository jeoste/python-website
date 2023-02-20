askPhoneNumber = input('Phone: ')
phone_number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"

}

output = ""
for number in askPhoneNumber:
    output += phone_number.get(number, "!") + " "
    #if askPhoneNumber in phone_number:
     #   askPhoneNumber = phone_number.get[number]

print(output)
