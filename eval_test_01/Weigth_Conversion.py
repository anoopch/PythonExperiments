# Program converts weight between pounds and kilograms
def kg_to_lbs(kilogram_value):
    return kilogram_value / 0.45359237


def lbs_to_kg(pound_value):
    return pound_value * 0.45359237


print('------------------MENU------------------')
print('\t\t1. Kilogram(Kg) to Pounds(lbs)')
print('\t\t2. Pounds(lbs) to Kilogram(Kg)')
print('----------------------------------------')
menu_choice = int(input('\nEnter the Menu choice : '))

if menu_choice == 1:
    weight = float(input('Enter the Weight (Kilograms): '))
    print('Weight in Pounds is - {0}'.format(kg_to_lbs(weight)))
elif menu_choice == 2:
    weight = float(input('Enter the Weight (Pounds): '))
    print('Weight in Kilograms is -  {0}'.format(lbs_to_kg(weight)))
else:
    print('Invalid menu choice.')
