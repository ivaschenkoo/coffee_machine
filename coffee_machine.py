class CoffeeMachine():
    """A class describing a coffee machine"""

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.status = True
        
    # get the necessary action from the user
    def get_status(self):
        status = input('Write action (buy, fill, take, remaining, exit):\n')
        if status == 'buy':
            buy_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            self.buy(buy_type)
        elif status == 'fill':
            self.fill()
        elif status == 'take':
            self.take()
        elif status == 'remaining':
            self.available_resources()
        elif status == 'exit':
            self.status = False
        else:
            print('Enter correct status')
    
    # show the user the available resources
    def available_resources(self):
        print("The coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
    
    # determine what resources are not enough to make coffee
    def not_enough_res(self, amount_water, amount_milk, amount_beans):
        if self.water < amount_water:
            return 'water'
        elif self.milk < amount_milk:
            return 'milk'
        elif self.beans < amount_beans:
            return 'beans'
        else:
            return 'cups'
    
    # offer the user a choice of available purchases
    def buy(self, buy_type):
        if buy_type == 'back':
            self.get_status()
        elif buy_type == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                print(f'Sorry, not enough {self.not_enough_res(250, 0, 16)}!')
        elif buy_type == '2':
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                print(f'Sorry, not enough {self.not_enough_res(350, 75, 20)}!')
        elif buy_type == '3':
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                print(f'Sorry, not enough {self.not_enough_res(200, 100, 12)}!')
        else:
            print('Enter correct action')
    
    # Add the necessary resources   
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    
    # Give out money
    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

first_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    if first_machine.status == False:
        break
    first_machine.get_status()