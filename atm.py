class Atm (object):
    def __init__(self,cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def check_balance(self):
        print('Your balance is 50000')

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print('Your have withdrawn amount'+str(amount) + '. Your remaining balance is '+str(new_amount))

def infoReceiver():
    cardNumber = input('Enter your card number: ')
    pinNumber = input('Enter your pin number: ')
