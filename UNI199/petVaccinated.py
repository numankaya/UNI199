def add_animals():
    pet_list = []
    ans = 'y'
    while ans.lower() == 'y':
        name = input('Enter the name of the pet:  ')
        yn = input('Pet vaccinated before? (y/n) ')
        is_vaccinated = yn.lower()=='y'
        pet = {'name':name, 'is_vaccinated':is_vaccinated}
        pet_list.append(pet)
        ans = input('Add more pets? (y/Y to continue):  ')
    return pet_list
pets = add_animals()
print('Initial state')
print(pets)

pets_to_vaccinate = []
for pet in pets:
    if not pet['is_vaccinated']:
        pets_to_vaccinate.append(pet)

print('Pets to be vaccinated:')
print(pets_to_vaccinate)

for pet in pets_to_vaccinate:
    pet['is_vaccinated'] = True
print('Final state')
print(pets)