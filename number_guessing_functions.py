logo = ''' _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
                                                                                    '''

# def game(difficulty, pc_num):
#     if difficulty == 'easy':
#         attempts = 10
#         user_guess = 'down'
#         while attempts != 0:
#             print(f"You have {attempts} remaining to guess the number.")
#             user_guess = int(input("Make a guess: "))
#             if pc_num != user_guess:
#                 if pc_num > user_guess:
#                     print("Too low.")
#                     attempts -= 1
#                 else:
#                     print("Too high.")
#                     attempts -= 1
#             else:
#                 return f"You got it! The answer was {pc_num}"
#     elif difficulty == 'hard':
#         attempts = 5
#         user_guess = 'down'
#         while attempts != 0:
#             print(f"You have {attempts} remaining to guess the number.")
#             user_guess = int(input("Make a guess: "))
#             if pc_num != user_guess:
#                 if pc_num > user_guess:
#                     print("Too low.")
#                     attempts -= 1
#                 else:
#                     print("Too high.")
#                     attempts -= 1
#             else:
#                 return f"You got it! The answer was {pc_num}"
#     else:
#         return "Not a difficulty!"

def easy_mode(pc_num):
    attempts = 10
    user_guess = 'down'
    while attempts != 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if pc_num != user_guess:
            if pc_num > user_guess:
                print("Too low.")
                attempts -= 1
            else:
                print("Too high.")
                attempts -= 1
        else:
            
            return print(f"You got it! The answer was {pc_num}")
    return print("Sorry! You lose.")

def hard_mode(pc_num):
    attempts = 5
    user_guess = 'down'
    while attempts != 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if pc_num != user_guess:
            if pc_num > user_guess:
                print("Too low.")
                attempts -= 1
            else:
                print("Too high.")
                attempts -= 1
        else:
            return print(f"You got it! The answer was {pc_num}")
    return print("Sorry! You lose.")