# rolling dice
    
import random, time

def roll(sides):
    num_rolled = random.randint(1,6)
    return num_rolled

def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling = False
            
    print("Thanks for playing.")

main()    
    
          
          
    
    
    
    

    
