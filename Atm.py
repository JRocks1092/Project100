class Atm:
    def __init__(self, atmCardNumber, pinNumber) -> None:
        self.cardNumber = atmCardNumber
        self.pinNumber = pinNumber
        self.depositAmount = 0
        self.logs = []

    def credit(self):
        amount = int(input("Amount : "))
        self.depositAmount += amount
        self.log("Credit "+str(amount)+" Successfull")

    def debit(self):
        amount = int(input("Amount : "))
        if self.depositAmount - amount > 0:
            self.depositAmount -= amount
            self.log("Debit "+str(amount)+" Successfull")
            return True
        else:
            self.log("Debit "+str(amount)+" Unsuccessfull")
            return False

    def getBalance(self):
        print(str(self.depositAmount))

    def getLog(self):
        for i in self.logs:
            print(i)

    def log(self, log):
        self.logs.append(log)


cards = []
currentCard = Atm(int(input("Enter Card No : ")),
                  int(input("Enter Pin No : ")))
cards.append(currentCard)
apprun = True


def addCard():
    cardNo = int(input("Enter Card No : "))
    pin = int(input("Enter Pin No : "))
    cards.append(Atm(cardNo, pin))


def changeCard():
    card = None
    run = True
    while run:
        cardNo = int(input("Enter Card No : "))
        pin = int(input("Enter Pin No : "))
        for i in cards:
            if i.cardNumber == cardNo:
                if i.pinNumber == pin:
                    card = i
                    run = False
                else:
                    print("Pin Wrong")
            else:
                print("No Card")
    print("Changed Card!")
    global currentCard
    currentCard = card


print("Enter c to credit")
print("Enter d to dedit")
print("Enter l to view logs")
print("Enter b to check balance")
print("Enter a to add card")
print("Enter cg to change Card")
print("Enter e to Exit")


def run():
    print("")
    command = input("Enter Command : ")
    if command == "c":
        currentCard.credit()
    elif command == "d":
        a = currentCard.debit()
        if not a:
            print("Debit Unsuccessful! Low Balance in card")
    elif command == "l":
        currentCard.getLog()
    elif command == "b":
        currentCard.getBalance()
    elif command == "a":
        addCard()
    elif command == "cg":
        changeCard()
    elif command == "e":
        global apprun
        apprun = False

while apprun:
    run()

print("exiting...")