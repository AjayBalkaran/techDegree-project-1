"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
Going for Exceeds Expectations rejected if project 1 does not meet all Exceeds Expectations Requirements Thank You.
"""
import random


def start_game():
    # intro Message to the player 
    print("""
    --------------------------------------------------------
                The Great Number Guessing Game
    --------------------------------------------------------
    """)
    
    high_score = 0
    high_score_name = 0 
    
    play_game = True
    
    while play_game:
      random_int = random.randint(1,10)   # store a random number as the answer/solution 
      player_guess = 0
      player_tries = 0
      
      player_name = input("What is your name?  ")
      
      # Shows player what is the current high score so they know what they have to beat
      if high_score == 0:
        print("{} their currently is no High score".format(player_name))
      else:
        print("The current High Score is held by {} and is {} tries ".format(high_score_name,high_score))
      
      while player_guess != random_int:
        player_guess = input("{} please enter a number between 1 - 10.  ".format(player_name))
        player_tries += 1  
      
      # handeling errors in a user friendly manner
        try:
          player_guess = int(player_guess)
          if player_guess < 1 or player_guess > 10:
            raise ValueError
        
        except ValueError:
          print("Please enter a whole number greater or equal to 1 or lower than or equal to 10")
        
        else:      
          if player_guess > random_int:
            print("It's lower")
                  
          elif player_guess < random_int:
            print("It's higher")
          else:
            print("Got it")
            break
      if high_score > player_tries or high_score == 0:
        high_score = player_tries
        high_score_name = player_name
        print("Wow!!!!! You hold the honour of a new High Score!!!!!!!")
      
      # leting the player know the game is over 
      print("""
                                *****************************
                                        Game Over
                                *****************************
      
    Congradulations {}. You guessed correctly that the number was {}, and it only took you {} tries.
    """.format(player_name, random_int, player_tries))
      
      #prompt the player if they would like to play again
      play_again = input("Would you like to play again? y for yes n for no  ").lower()
      
      # handeling errors in a user friendly manner
      while play_again != "y" and play_again != "n":
        play_again = input("Please enter y if you wish to play again or n if you wish to quit. ").lower() 
      if play_again == "y":
        play_game = True
        continue
      else:
        print("Goodbye {}, Thank you for playing".format(player_name))
        break
        
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()