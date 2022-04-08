#Name: Min Jung
#Due Date:12/05/2021
#Final Project: Lab 3

#part 1
#output the roster from smallest  to largest jersey
def roster(player_dictionary):
    jersey_list = list(player_dictionary.keys())
    jersey_list.sort()
    
    print("\nROSTER")
    for i in jersey_list:
        print(f'Jersey number: {i}, Rating:{player_dictionary[i]}')

def menu():
    print("\nMENU")
    print("a-Add player")
    print("d-Remove player")
    print("u-Update player rating")
    print("r-Output players above a rating")
    print("o-Output roster")
    print("q-Quit")
    user_char=input("Choose an option:")
    return user_char

def add_player(player_dictionary):
    jersey = int(input("Enter a new player's jersey number:\n"))
    if jersey < 0 or jersey > 99:
            print("ERROR:Jersey number must be in between 0 and 99!")
            exit()
    rating = int(input("Enter the player's rating:\n"))
    if rating < 1 or rating > 9:
            print("ERROR:Rating number must be in between 1 and 9!")
            exit()
    player_dictionary[jersey] = rating
    return player_dictionary
    
def remove_player(player_dictionary):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey < 0 or jersey > 99:
            print("ERROR:Jersey number must be in between 0 and 99!")
            exit()
    player_dictionary.pop(jersey)
    return player_dictionary
    
def update_rating(player_dictionary):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey < 0 or jersey > 99:
            print("ERROR:Jersey number must be in between 0 and 99!")
            exit()
    rating = int(input("Enter a new rating for player:\n"))
    if rating < 1 or rating > 9:
            print("ERROR:Rating number must be in between 1 and 9!")
            exit()
    player_dictionary[jersey] =rating
    return player_dictionary   
 
def above_rating(player_dictionary):
    rating = int(input("Enter a rating:\n"))
    if rating < 1 or rating > 9:
            print("ERROR:Rating number must be in between 1 and 9!")
            exit()
    print("\nABOVE", rating )
    jersey_list = list(player_dictionary.keys())
    jersey_list.sort()
    for i in jersey_list:
        if player_dictionary[i] > 5:
            print(f'Jersey number:{i}, Rating:{player_dictionary[i]}')
def main():
    player_dictionary = {}
    for i in range(5):
        jersey = int(input(f"Enter player {i+1}'s jersey number:\n"))
        if jersey < 0 or jersey > 99:
            print("ERROR:Jersey number must be in between 0 and 99!")
            break
        rating = int(input(f"Enter player {i+1}'s rating:\n"))
        if rating < 1 or rating > 9:
            print("ERROR:Rating number must be in between 1 and 9!")
            break
        player_dictionary[jersey] = rating
    roster(player_dictionary)
    
    user_char = ''

    while user_char != "q":
        user_char = menu()
        if user_char.lower() == "a":
            player_dictionary = add_player(player_dictionary)
        elif user_char.lower() == "d":
            player_dictionary = remove_player(player_dictionary)
        elif user_char.lower() == "u":
            player_dictionary = update_rating(player_dictionary)
        elif user_char.lower() == "r":
            player_dictionary = above_rating(player_dictionary)
        elif user_char.lower() == "o":
            player_dictionary == roster(player_dictionary)
    
        
main()

