#author Sparsh Khanna
#@SparshKhanna0001        ->Github

import time
from os import system

def move_validater(move:str,valid_moves:list):
   return True if move in valid_moves else False


def move_generator(valid_moves:list):

    import random
    return random.choice(valid_moves)

def move_comparer_rps(player1,move1,player2,move2):

    #rps: rock paper 
    
    if move1=='p':
        if move2 =='s':
            return player2
        if move2 =='s':
            return player1
        
    if move1=='s':
        if move2 =='r':
            return player2
        if move2 =='p':
            return player1

    if move1=='r':
        if move2 =='s':
            return player2
        if move2 =='p':
            return player1


level_msg="Select :-\n(s) start\n(q) quit"

turns = 3
valid_moves= ['r','p','s']

ai_wins = 0
player_wins = 0
waiting_time = 1

game_code = {
        'r':'rock',
        'p':'paper',
        's':'scissors'
        }

while True:
    print(level_msg)
    option_selectd = input(">")

    system('clear')

    if option_selectd.lower() == 'q':
        break

    elif option_selectd.lower() =='s':

        print("r: rock\np: paper\ns: scissors\n")

        for turn in range(turns):

            ai_move = move_generator(valid_moves)
            player_move = input(">")
           
            if move_validater(player_move,valid_moves) == False:
                print("You have entered wrong move\nAI will be rewarded for your mistake.")
                ai_wins += 1
                time.sleep(0.3)

                system('clear')
                continue


            for i in range(2):
                for j in range(1,4):
                    print("AI deciding move  "+"."*j+"  " ,end="\r")
                    time.sleep(0.3)

            print("\n")

            for i in ['rock','paper','scissors']:
                print(i+"     " ,end="\r")
                time.sleep(0.3)

            print("AI choosed :- "+game_code[ai_move])


            print("\n")

            if move_comparer_rps('player', player_move,'ai',ai_move) == None: 
                print("Draw!")

            elif move_comparer_rps('player', player_move,'ai',ai_move) == 'player':
                print("You won ! ")
                player_wins += 1

            elif move_comparer_rps('player', player_move,'ai',ai_move) == 'ai':
                print("AI won")
                ai_wins += 1

            time.sleep(0.4)
            system('clear')

        print('Score:- \n')
        print("Your score: "+str(player_wins))
        print("AI scored: "+str(ai_wins))
        print('\n')
 
        if ai_wins == player_wins:
            print("It's a draw!")
            print("You may try a rematch.")
 
        if ai_wins > player_wins:
            print("AI won")

        if ai_wins < player_wins:
            print("You won")

        print('\n')

        i = input("Press ENTER to continue ")
        system('clear')

    else: 
        print("Invalid option please try again")
        print('\n')

        i = input("Press EBTER to continue ")
        system('clear')
