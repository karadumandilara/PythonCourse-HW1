import random
import math

#portfolio
class Portfolio:

    def __init__(self):
        #initial three portfolio props

        self.cash = 0.0
        self.stock = {}
        self.mutualFunds={}
        self.propToUse = None

        self.history = "\n\nportfolio's ledger\n \n"

    #adding cash to the portfolio
    def deposit(self, cash):
        amount= cash
        self.cash +=amount
        self.history +="Deposited : $"+str(amount)+" \n\n"

    #draw cash from the portfolio
    def withdraw(self, cash):
        #check if there is balance
        if self.cash<cash :
            print("you can't withdraw, insufficient balance")
        else:
            self.cash -= int(cash)
            self.history +="Withdrew :$" + str(cash)+" \n\n "

##########################################################################

    def buyProp(self, quantity, prop):

        neededAmount=( quantity * prop.price)

        if self.cash < neededAmount:

            print("insufficient balance. you can't buy that now")
            return
        #if you have money go on with buying

        #get the prop type
        propT=prop.getPropName()



        if(propT=='stock'):
            self.propToUse=self.stock
            pass

        elif(propT=='mutual fund'):
            self.propToUse = self.mutualFunds
        else:
            self.propToUse = None

        if self.propToUse == None:
            return

        if prop in self.propToUse:
            self.propToUse[prop] += quantity
        else:
            self.propToUse[prop] = quantity
        self.history += "\nBought %d of %s ---  %s\n" % (quantity, prop.getPropName(), prop.symbol)

        #withdraw the money for the transaction

        self.withdraw(neededAmount)

    def buyStock(self, quantity, prop):
        self.buyProp(int(quantity), prop)

    def buyMutualFund(self, quantity, prop):
        self.buyProp(quantity, prop)

    def buyBond(self, quantity, prop):
        self.buyProp(quantity, prop)


    #selling

    def sellProp(self, prop, quantity):

        # make sure to use objects rather than prop names
        # get the prop type
        propT = prop.getPropName()

        if (propT == 'stock'):
            self.propToUse = self.stock
            pass

        elif (propT == 'mutual fund'):
            self.propToUse = self.mutualFunds
        else:
            self.propToUse = None

        if self.propToUse==None:
            return


        if prop in self.propToUse:

            if self.propToUse[prop] < quantity:
                print("insufficient %s from %s" % (prop.symbol, prop.getPropName()))
            else:
                self.propToUse[prop] -= quantity

                if self.propToUse[prop] == 0:
                    del self.propToUse[prop]


                self.history +="sold %d of %s ---- %s\n" % (quantity, prop.getPropName(), prop.symbol)
                self.deposit(quantity * prop.getPrice())
        else:
            print("no %s with name %s found " % (prop.getPropName(), prop.symbol))

    def sellStock(self, prop, quantity):
        self.sellProp( prop,int(quantity))

    def sellMutualFund(self, prop, quantity):
        self.sellProp( prop, quantity)

    def sellBond(self, prop, quantity):
        self.sellProp(prop,quantity)



##################################

    def __str__(self):
        message ="\n\n------------------\n"

        message += "Total Balance: $" + str(self.cash) + "\n"
        self.propToUse=self.stock
        message += "\nStock\n"

        if not self.propToUse:
            message += "\t => nothing in this class \n"
        for prop in self.propToUse:
            message += "\t => "+ str(prop.symbol)+"  "+str(self.propToUse[prop])+" \n"


        self.propToUse = self.mutualFunds
        message += "Mutual Funds\n"

        if not self.propToUse:
            message += "\t => nothing in this class \n"

        for prop in self.propToUse:
            message += "\t => "+ str(prop.symbol)+" \n"


        #finally display the balance
        message+="-------------------\n\n"

        return message

    def showHistory(self):
        print(self.history)

#property superclass for ...
class Property:

    def __init__(self,price,symbol):
        self.price=price
        self.symbol=symbol

    def getPropName(self):
        return ""
    def getPrice(self):
        return 0.0

#stock:property
class Stock(Property):
    def __init__(self, price, symbol):
        super().__init__( price, symbol)

    # override the get class and get price methods
    def getPropName(self):
        return "stock"

    def getPrice(self):
        return int(random.uniform(.5 * self.price, 1.5 * self.price)) / 100.0

#Mutual fund:property
class MutualFund(Property):
    def __init__(self, symbol):
        super().__init__( 1.0, symbol)

    def getPropName(self):
        return "mutual funds"

    def getPrice(self):
        return int(100 * random.uniform(.9 * self.price,1.2 * self.price)) / 100.0

#bond:property #bonus
class Bonds(Property):
    def __init__(self, symbol):
        super().__init__(1.0, symbol)

    def getPropName(self):
        return "bonds"
    def getPrice(self):
        return 0.0;



#Main function
def main():

    portfolio = Portfolio()  # Creates a new portfolio

    portfolio.deposit(300.50)  # Adds cash to the portfolio

    s = Stock(20, "HFH")  # Create Stock with price 20 and symbol "HFH"
    portfolio.buyProp(5, s)  # Buys 5 shares of stock s

    mf1 = MutualFund("BRT")  # Create MF with symbol "BRT"
    mf2 = MutualFund("GHT")  # Create MF with symbol "GHT"

    portfolio.buyMutualFund(10.3, mf1)  # Buys 10.3 shares of "BRT"
    portfolio.buyMutualFund(2, mf2)  # Buys 2 shares of "GHT"

    print(portfolio)  # Prints portfolio

    # cash: $140.50
    # stock: 5 HFH
    # mutual funds: 10.33 BRT
    # 2 GHT

    portfolio.sellMutualFund(mf1, 3)  # Sells 3 shares of BRT
    portfolio.sellMutualFund(mf2, 3)  # Sells 3 shares of BRT
    portfolio.sellMutualFund(s, 3)  # Sells 3 shares of BRT


    portfolio.sellProp(s, 1)  # Sells 1 share of HFH

    portfolio.withdraw(50)  # Removes $50

    portfolio.showHistory()  # Prints a list of all transactions
    # ordered by time

    print(portfolio)  # Prints portfolio

main()