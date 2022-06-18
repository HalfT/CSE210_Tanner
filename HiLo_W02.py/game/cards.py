import random

class Cards:

    def __init__(self):
        self.new_card = ""
        self.old_card = ""

    def draw(self):

        """
        Starts with a simple random to start the game.
        Second part is the make sure the same card isn't used twice causeing a potental error.
        prints the card number 
        """
        
        if self.new_card == "":
            self.new_card = random.randint(1,13)
            print (f"The card is: {self.new_card}")
        else:
            self.old_card = self.new_card
            self.new_card = random.randint(1,13)
            
            while self.old_card == self.new_card:
                self.new_card = random.randint(1,13)
            
            print (f"The card is: {self.new_card}")

