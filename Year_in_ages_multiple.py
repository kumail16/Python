while True:
    add_year = input('Enter your year of birth (or "q" to quit): ')
    if add_year.lower() == 'q':
        break

    age = 2023 - int(add_year)
    print(f'You are {age} year/s old')

    repeat = input('Do you want to do another calculation? (yes/no): ')
    if repeat.lower() != 'yes':
        break