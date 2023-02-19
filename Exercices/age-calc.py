from datetime import date

birth_year = int(input('Birth year: '))
today = date.today()
actual_year = int(today.strftime("%Y"))

age = actual_year - birth_year

print("Age: ", age)