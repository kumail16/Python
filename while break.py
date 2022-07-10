while True:
    print('Who are you?')
    name = input()
    if name != 'Kumail':
        continue
    print('Hello Kumail, What is the password?')
    password = input()
    if password == 'cisco':
        break
print('''Access Granted''')
