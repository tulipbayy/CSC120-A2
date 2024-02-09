from computer import *
from typing import Optional
class ResaleShop:

    # What attributes will it need?
    inventory = []


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory
 


    # What methods will you need?
    def buy(self, computer):
        #1. call Computer(...) constructor
        # to create a new computer instance
        c = Computer(computer)
        #2. call inventory.append(...) to add the
        # new Computer instance to the inventory
        self.inventory.append(c)


    def sell(self, computer):
        if (computer in self.inventory):
            self.inventory.remove(computer)
        else:
            print("It's not in inventory")

    def print_inventory(self):
        print(self.inventory)

    def refurbish(self, computer: Computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", computer, "not found. Please select another item to refurbish.")

