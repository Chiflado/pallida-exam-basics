# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys

class FavouriteAnimals:

    def __init__(self):
        self.commands()

    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def commands(self):
        self.arg = self.get_arguments()
        if self.arg == None:
            self.print_usage()
        if self.arg == 'add':
            if self.check_animals(sys.argv[2]) == True:
                self.add_animal(sys.argv[2])
            else:
                print('Animal already in list')

    def print_usage(self):
        print( 'fav_animals [animal] [animal]')

    def add_animal(self, animal):
        with open('favourites.txt', 'a') as text_file:
            text_file.write(animal + '\n')
            text_file.close

    def check_animals(self, animal):
        with open('favourites.txt', 'r') as text_file:
            self.list = list(text_file)
            for i in range(len(self.list)):
                if self.list[i] != animal:
                    return True


fav_anmimals = FavouriteAnimals()