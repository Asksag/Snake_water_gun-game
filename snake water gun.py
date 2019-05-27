import random
lst=['snake','water','gun']
computer_point= 0
player_point = 0
player_name= input("Enter your name:\t")
number_of_turn=10
number_of_chances = 0

print("\t \t \t \t \tSnake , Water , Gun Game by Abhishek... \n \n ")

# implementing while loop for 10 chances..

while(number_of_chances <= 10):
    enter_choice = input("enter any one of the following snake,water,gun")
    comp_choice = random.choice(lst)
    #if statement for exit . when chances is 10 or more than 10...


        # if user enter snake and computer also chooses snake
    if (comp_choice == enter_choice):
            print(f"both computer and {player_name} both entered{comp_choice}."
                  f"therefore match has tie and both get zero points.")
            number_of_turn =number_of_turn -1
            number_of_chances = number_of_chances + 1

# when comp_choice is snake and player_point is water.
    elif ( comp_choice== 'snake' and  enter_choice == 'water'):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 1 point and {player_name} gets 0.")
            number_of_turn = number_of_turn - 1
            number_of_chances = number_of_chances + 1
            player_point  = player_point
            computer_point = computer_point + 1


# when comp_choice is water and player_point is snake

    elif ( comp_choice == 'water' and enter_choice == 'snake'):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 0 point and {player_name} gets 1.")
            number_of_turn = number_of_turn-1
            number_of_chances = number_of_chances + 1
            player_point = player_point + 1
            computer_point = computer_point

# when computer chooses gun and user choose snake
    elif ( comp_choice == 'gun' and enter_choice == 'snake'):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 1 point and {player_name} gets 0.")
            number_of_turn = number_of_turn - 1
            number_of_chances = number_of_chances + 1
            player_point = player_point
            computer_point = computer_point + 1

# when computer chooses snake and user chooses gun
    elif (comp_choice == 'snake' and enter_choice == 'gun' ):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 0 point and {player_name} gets 1.")
            number_of_turn = number_of_turn - 1
            number_of_chances = number_of_chances + 1
            player_point = player_point + 1
            computer_point = computer_point

# when computer choose water and user chooses gun
    elif (comp_choice == 'water' and enter_choice == 'gun'):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 1 point and {player_name} gets 0.")
            number_of_turn = number_of_turn - 1
            number_of_chances = number_of_chances + 1
            player_point = player_point
            computer_point = computer_point + 1


# when computer chooses gun and user chooses water..
    elif (comp_choice == 'gun' and enter_choice == 'water'):
            print(f"computer chooses {comp_choice} and player chooses {enter_choice}."
                  f"therefore computer gets 0 point and {player_name} gets 1.")
            number_of_turn = number_of_turn - 1
            number_of_chances = number_of_chances + 1
            player_point = player_point + 1
            computer_point = computer_point


    else:
            print("wrong choice !!!")




if( computer_point == player_point):
    print(f"computer sore{computer_point} and  player {player_name} score {player_point}"
          f"therefore match has been tied...")

elif (computer_point<player_point):
    print(f"computer sore{computer_point} and  player {player_name} score {player_point}"
          f"therefor player {player_name} has won the game..")

else:
    print(f"computer sore{computer_point} and  player {player_name} score {player_point}"
          f"therefore computer has won the match..")











