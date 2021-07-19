class Atm (object):
    def __init__(self,cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def check_balance(self):
        print('Your balance is 50000')

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print('Your have withdrawn amount '+str(amount) + '. Your remaining balance is '+str(new_amount))

def infoReceiver():
    cardNumber = input('Enter your card number: ')
    pinNumber = input('Enter your pin number: ')
    newUser = Atm(cardNumber, pinNumber)
    print('Choose what you want to do: ')
    print('1.Balance Enquiry      2.Cash Withdrawl')
    activity = int(input('Enter activity number: '))
    if(activity==1):
        newUser.check_balance()

    elif(activity==2):
        amount = int(input('Enter the amount you wish to withdraw: '))
        newUser.withdrawl(amount)

    else:
        print('Enter a valid number: ')

infoReceiver()
