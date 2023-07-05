years_of_birth = []
add_year = input('Enter your year of birth: ')
years_of_birth.append(add_year)
ages = []
for year in years_of_birth:
    ages.append(2023 - int(year))
    print(f'you are {ages} year/s old')
