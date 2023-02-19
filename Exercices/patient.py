name = str(input("What is your name: "))
age = int(input("What is your age: "))
isNewPatient = str(input("New patient? Y or N "))

if isNewPatient == 'Y' or isNewPatient == 'y':
    isNewPatient = True
elif isNewPatient == 'N' or isNewPatient == 'n':
    isNewPatient = False

print(name, age, isNewPatient)
