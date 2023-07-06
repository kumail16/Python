your_year_birth = []
add_year = input('Enter your year of birth: ')
your_year_birth.append(add_year)
ages = []
for year in your_year_birth:
    ages.append(2023 - int(year))
    print(f'you are {ages} year/s old')
