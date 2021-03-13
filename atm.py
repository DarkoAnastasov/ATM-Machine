import time

print('Please insert your CARD')

time.sleep(5)

password = 1234

pin = int(input('Enter your pin'))

balance = 5000

if pin == password:

    print("""
        1 == balance
        2 == withdraw balance  
        3 == deposit balance
        4 == exit
        """
    )
    try:
        option = int(input('Please choose an option'))
    except:
        print('Please enter valid option')

    if option == 1:
        print(f'Your current balance is {balance}')

    if option == 2:
        withdraw_amount = int(input('Please enter how much you want to withdraw?'))
        balance = balance - withdraw_amount
        print(f'{withdraw_amount} is withdrawn from your balance')
        print(f'Your current balance is {balance}')

    if option == 3:
        deposit_amount = int(input('Please enter how much you want to deposit?'))
        balance = balance + deposit_amount
        print(f'{deposit_amount} is deposited to your balance')
        print(f'Your current balance is {balance}')

    if option == 4:
        break

else:
    print('Wrong pin. Please try again')