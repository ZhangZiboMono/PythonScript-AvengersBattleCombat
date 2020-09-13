import random # Import random module to create the random generator.

# Define combat function to calculate whether the computer wins or the player wins. It uses 2 parameters, which are computer_Move and player_Move.
def combat(computer_move,player_move):
   if computer_move == player_move:
      print("--Tie! No Winner.--")
      combat_result = 0 # Create a new variable that will be used to judge the outcome.
   elif (computer_move == 1 and player_move in [2,3,6]) or (computer_move == 2 and player_move in [3,4,6]) or (computer_move == 3 and player_move in [4,5]) or (computer_move == 4 and player_move in [1,5]) or (computer_move == 5 and player_move in [1,2,6]) or (computer_move == 6 and player_move in [3,4]):
      print("--Sorry, you lost.--")
      combat_result = 1 # Create a new variable that will be used to judge the outcome.
   else:
      print("--Congratulations, you won.--")
      combat_result = 2 # Create a new variable that will be used to judge the outcome.
   return combat_result # Return the outcome value.

# Define computerMove function to print the move of computer. It uses 1 parameters, which is computer_Choice.
def computerMove(computer_choice):
   if computer_choice == 1:
      print("Computer chose Attack 1: Iron Man's Attack.")
   elif computer_choice == 2:
      print("Computer chose Attack 2: Thor's Hammer.")
   elif computer_choice == 3:
      print("Computer chose Attack 3: Hulk's Howl.")
   elif computer_choice == 4:
      print("Computer chose Attack 4: Captain America's Shield.")
   elif computer_choice == 5:
      print("Computer chose Attack 5: Hawkeye's Arrow.")
   else:
      print("Computer chose Attack 6: Black Widow's Gun.")
   return computer_choice

# Define playerMove function to print the move of player. It uses 1 parameters, which is player_Choice.
def playerMove(player_choice):
   if player_choice == 1:
      print("\n********************\nYou chose Attack 1: Iron Man's Attack.")
   elif player_choice == 2:
      print("\n********************\nYou chose Attack 2: Thor's Hammer.")
   elif player_choice == 3:
      print("\n********************\nYou chose Attack 3: Hulk's Howl.")
   elif player_choice == 4:
      print("\n********************\nYou chose Attack 4: Captain America's Shield.")
   elif player_choice == 5:
      print("\n********************\nYou chose Attack 5: Hawkeye's Arrow.")
   else:
      print("\n********************\nYou chose Attack 6: Black Widow's Gun.")
   return player_choice

# Define checkRestart function to check if the player inputs right number when they want to play again or go back to the menu.
def checkRestart():
   restart = input("\nWould you like to try again or go back to the menu?\n[1]: Play again.\n[2]: Go back to the menu.") # I didn't use intger function because player may input letters or symbols, which will cause the program to report an error and force the program to quit.
   while not (restart == '1' or restart == '2'):
      print("\nI did not understand that response. Please choose 1 or 2.")
      restart = input("\nWould you like to try again or go back to the menu?\n[1]: Play again.\n[2]: Go back to the menu.")
   return restart # Variable restart gets its value only when the player input 1 or 2.

# Define ensureBetIsNum function to make sure that the player enter a positive integer which will be used for mathematical calculation (mod).
def ensureBetIsNum():
   player_bet = input("\nHow nuch do you want to bet for this round? (The bet amount must be in multiples of 5)") # I didn't use intger function because player may input letters or symbols, which will cause the program to report an error and force the program to quit.
   while not player_bet.isdigit() == True: # The player_Bat goes out of the while loop only when the player inputs full of digits. 
      print("\nThat is not a valid amount.\nYou can't input letters, sumbols, negative number or decimal, which means your bet must be a positive integer.")
      player_bet = input("Please re-enter your bet.\n\nHow nuch do you want to bet for this round? (The bet amount must be in multiples of 5)")
   return int(player_bet) # Convert this variable to an integer, in order to do the mathematical calculation (mod).

# Define calCurrentMoney function to calculate new balance after every round. It uses 3 parameters, which are combat_Result, _balance and player_Bet.
def calCurrentBalance(combat_result, _balance, player_bet):
   if combat_result == 0:
      pass
   elif combat_result == 1:
      _balance = _balance - player_bet
   else:
      _balance = _balance + player_bet
   return _balance

# Define checkAttackChoice function to check if the player inputs the right number of the attack choice.   
def checkAttackChoice():
   attack_choice = input("\nPlease choose an attack.\n[1]: Iron Man's Attack.\n[2]: Thor's Hammer.\n[3]: Hulk's Howl.\n[4]: Captain America's Shield.\n[5]: Hawkeye's Arrow.\n[6]: Black Widow's Gun.") # Player choose their move. I didn't use intger function because player may input letters or symbols, which will cause the program to report an error and force the program to quit.
   while not (attack_choice == '1' or attack_choice == '2' or attack_choice == '3' or attack_choice == '4' or attack_choice == '5' or attack_choice == '6'): # Ensure the variable attackChoice that the player inputs must be "1", "2", "3", "4", "5" or "6".
      print("\nI did not understand that response. Please choose 1, 2, 3, 4, 5 or 6.")
      attack_choice = input("\nPlease choose an attack.\n[1]: Iron Man's Attack.\n[2]: Thor's Hammer.\n[3]: Hulk's Howl.\n[4]: Captain America's Shield.\n[5]: Hawkeye's Arrow.\n[6]: Black Widow's Gun.")
   return attack_choice

# Define main function.
def main():
   name = input("Hello player, what's your name?")
   print("\nDear "+name+":\nWelcome to The Avengers Battle Combat.\nWe offer you $100 to begin this game.")
   choice = input("\nPlease choose from the menu.\n[I]: Instructions\n[P]: Play game\n[Q]: Quit game")
   balance = 100 # Create a constants to set the initial balance.
   balanceHistory = [] # Create a list to store the balance history.
   while not (choice == "Q" or choice == "q" or balance == 0): # The game ends only when the variable choice is "Q" or "q" or the variable balance is 0.
      if choice == "I" or choice == "i":
         print("\nWelcome to The Avengers Battle Combat. You will be fighting against the computer, and the winner gets bragging rights. You are allowed to make a bet to win the money and you will lose money when you lose the game, of course. You will also be forced to quit when your balance is $0. \nFor each turn you will be asked to use one of these 6 attacks below:\n\n1: Iron Man's Attack.\n2: Thor's Hammer.\n3: Hulk's Howl.\n4: Captain America's Shield.\n5: Hawkeye's Arrow.\n6: Black Widow's Gun.\nP.S. Choose wisely.\n")
         choice = input("Please choose from the menu.\n(I): Instructions\n(P): Play game\n(Q): Quit game")
      elif choice == "P" or choice == "p":
         playerBetInt = ensureBetIsNum()
         while not (playerBetInt%5 == 0 and playerBetInt <= balance): # Ensure the varialbe playerBet that the player inputs is not bigger than his current balance and must be a multiple of 5.
            if playerBetInt > balance:
               if playerBetInt%5 == 0:
                  print("\nThat is not a valid amount.\nYour bet can't be bigger than your current balance ($"+str(balance)+").")
               else:
                  print("\nThat is not a valid amount.\nYour bet must be a multiple of 5 and no bigger than your current balance ($"+str(balance)+") at the same time.")
            else:
               print("\nThat is not a valid amount.\nYour bet must be a multiple of 5.")
            print("Please re-enter your bet.")
            playerBetInt = ensureBetIsNum()
         playerBet = playerBetInt
         print("\nYou chose to bet $"+str(playerBet)+".")
         attackChoice = checkAttackChoice() # Use checkAttackChoice to get the correct value of player's choice.
         playerChoice = playerMove(int(attackChoice)) # Print the move of player and assign the value produced by playerMove function to playerChoice which will be used to combat function later.
         computerChoice = random.randint(1,6) # Use random to generate a random number for computerChoice.
         computerMove(computerChoice) # Print the move of computer.
         combatResult = combat(playerChoice, computerChoice)
         balance = calCurrentBalance(combatResult, balance, playerBet)
         balanceHistory.append(balance) # Add every balance after every round to the balanceHistory list.
         print("Your current balance is $"+str(balance)+".") # Print the current balance after every round.
         print("********************")
         if balance != 0: # Check if the balance is 0.
            restartChoice = checkRestart()
            if restartChoice == '1':
               pass
            else:
               choice = input("\nPlease choose from the menu.\n(I): Instructions\n(P): Play game\n(Q): Quit game")
         else:
            print("\nSorry, you can't play next round since you have lost all your money.")   
      else:
         print("\nI did not understand that response. Please choose either I, P or Q.")
         choice = input("\nPlease choose from the menu.\n(I): Instructions\n(P): Play game\n(Q): Quit game")
   print("\nThank you for playing Avengers Battle Combat!\nYour final balance is $"+str(balance)+".\n\nYour balance history is:\nStarting balance: $100")
   for i in range(len(balanceHistory)): # Use the for loop to print the history of balance.
      print("After round "+str(i+1)+": "+str(balanceHistory[i]))
   print("\nGood bye "+name+", have a nice day.")

# Call the main function.
main()

