while True:
    print('Who are you?')
    
    name = input()
    
    if name != 'Kumail':
        print('Only Kumail is allowed')
        continue
    
    print('Hello Kumail, What is the password?')
    
    password = input()
    
    if password == 'cisco':
        break
    elif password !='cisco':
        print('Wrong Password')
        
print('''Access Granted''')