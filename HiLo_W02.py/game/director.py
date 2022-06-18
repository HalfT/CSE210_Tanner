from game.cards import Cards

class Director:

    def __init__(self):
        self.playing = True
        self.p_guess = ""

    def start_game(self):
        """
        Begin Game
        """
        
        score = 300
        cards = Cards()
        p_guess = ""
        print ("Welcome to HiLo. Select if you think your card will be higher or lower. If you guess correctly you get 100 points, if not you loose 75 points. Good Luck!")      

        while self.playing:
            print ()
            cards.draw()
            p_guess = self.guess()
            cards.draw()
            new_card = cards.new_card
            old_card = cards.old_card
            points = self.check_guess(new_card, old_card, p_guess)
            score += points
            self.print_score(score)
            self.check_play(score)

    def guess(self):
        """
        Ask the user for h/l
        """

        return input("Higher or Lower? [h/l] ")

    def check_guess(self, old_card, new_card, p_guess):
        """ 
        Check the guess with the cards
        """

        if p_guess == "h":
            if old_card > new_card:
                points = 100
                print ("\n*** Correct! ***")
            if old_card < new_card:
                points = -75
                print ("\n *** Incorrect, sorry loose 75 points ***")                
        elif p_guess == "l":
            if old_card < new_card:
                points = 100
                print ("\n *** Correct! ***")
            if old_card > new_card:
                points = -75
                print ("\n *** Incorrect, sorry loose 75 points ***")
        return points   

    def print_score(self, score):
        """
        simple print option
        """

        print(f"\nYour score is: {score} ")

    def check_play(self, score):
        """ 
        Check to see if the player still has points to play or wants to opt out. 
        """


        if score < 0:
            print ("Thanks for playing, better luck next time. ")
            self.playing = False
        else:
            play = input ("Play again? [y/n] ")
            if play == "n":
                self.playing = False
            else:
                print()

            
        
