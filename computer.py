class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, desc, type, capacity, memory, os, year, price):
        self.description = desc
        self.processor_type = type
        self.hard_drive_capacity = capacity
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = price
    
    def update_price(self, new_price):
        self.price = new_price
    def update_os(self, os):
        self.operating_system = os



