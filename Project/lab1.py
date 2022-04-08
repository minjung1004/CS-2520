#Name: Min Jung
#Due Date: October 31, 2021
#Project 1: Lab 1

#1
user_String = input("Enter a sample text:\n")
print("\nYou entered:", user_String)

#2
def print_menu():
    command_menu = "\nMENU\nc-Number of non-whitespace characters\nw-Number of words\nf-Fix capitalization\nr-Replace punctuation\ns-Shorten spaces\nq-Quit\n"
    print(command_menu)

#3
def execute_menu(user_character, user_text):
    while True:
        if user_character == 'c':
            print("Number of non-whitespace characters:",get_num_of_non_WS_characters(user_text))
            break
        elif user_character == 'w':
            print("Number of words:",get_num_of_words(user_text))
            break
        elif user_character == 'f':
            count,text = fix_capitalization(user_text)
            print("Number of letters capitalized: {}\nEdited text: {} ".format(count, text))
            break
        elif user_character == 'r':
            text, exclamation_count, semicolon_count = replace_punction(user_text)
            print("Punction replaced\nexclamation_count: {}\nsemicolon_count: {}\nEdited text: {}".format(exclamation_count, semicolon_count, text))
            break
        elif user_character == 's':
            print("Edited text:", shorten_space(user_text))
            break
        elif user_character == 'q':
            break
        else:
            print_menu()
            user_choice =input("Choose an option:\n")
            execute_menu(user_choice, user_String)
            break
        
#5 
def get_num_of_non_WS_characters(user_text):
    character_count = 0
    for characters in user_text:
        if characters != ' ' and characters !='\t':
            character_count += 1   
    return character_count
    

#6
def get_num_of_words(user_text):
   word_count= len(user_text.split( ))
   #print(str(word_count))
   return word_count
   
#7
def fix_capitalization(user_text):
    word_cap_count = 0
    start = True
    fixed_text=''
    for word in user_text:
        if start and word.isalpha():
            if word.islower():
                word = word.upper()
                word_cap_count += 1
                fixed_text += word
                start = False
        elif word in '.?!':
            start = True
            fixed_text += word
        else:
            fixed_text += word
    return (word_cap_count, fixed_text)

#8
def replace_punction(user_text, exclamation_count = 0, semicolon_count = 0):
    fixed_text=''
    for character in user_text:
        if character == '!':
            fixed_text += '.'
            exclamation_count += 1
        elif character == ';':
            fixed_text += ','
            semicolon_count += 1
        else:
            fixed_text += character
    return (fixed_text,exclamation_count,semicolon_count)

#9
def shorten_space(user_text):
    if user_text.isspace() == False:
        while '  ' in user_text:
            user_text = user_text.replace('  ', ' ')
        return user_text
            
       
#4 
def main():
    print_menu()
    user_choice =input("Choose an option:\n")
    execute_menu(user_choice, user_String)
    
main()