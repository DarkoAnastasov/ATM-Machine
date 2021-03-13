import time

print('Please insert your CARD')

time.sleep(5)

password = 1234

pin = int(input('Enter your pin'))

balance = 5000

if pin == password:

    while True:

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

            print('=============================================')
            print('=============================================')

        if option == 2:
            withdraw_amount = int(input('Please enter how much you want to withdraw?'))

            print('=============================================')
            print('=============================================')
            if withdraw_amount > balance:
                print("You don't have that much money on your balance")
            else:
                balance = balance - withdraw_amount

                print(f'{withdraw_amount} is withdrawn from your balance')

                print('=============================================')
                print('=============================================')

                print(f'Your current balance is {balance}')

                print('=============================================')
                print('=============================================')

        if option == 3:
            deposit_amount = int(input('Please enter how much you want to deposit?'))
            balance = balance + deposit_amount

            print('=============================================')
            print('=============================================')

            print(f'{deposit_amount} is deposited to your balance')

            print('=============================================')
            print('=============================================')

            print(f'Your current balance is {balance}')

            print('=============================================')
            print('=============================================')


        if option == 4:
            break


else:
    print('Wrong pin. Please try again')