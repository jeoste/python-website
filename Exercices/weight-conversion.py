choice = input('Choose your weight (L)bs or (K)g: ')

if choice == 'L' or choice == 'l':
    weight_lbs = float(input('Weight (L)bs: '))
    weight_kg = weight_lbs * 0.45
    print(weight_kg)
elif choice == 'K' or choice == 'k':
    weight_kg = float(input('Weight (K)g: '))
    weight_lbs = weight_kg / 0.45
    print(weight_lbs)

