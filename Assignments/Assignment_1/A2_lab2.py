#Name: Min Jung
#Due Date: September 13, 2021 till 10pm

red_input = int(input())
green_input= int(input())
blue_input = int(input())

red = red_input - min(red_input, green_input ,blue_input)
green = green_input - min(red_input, green_input ,blue_input)
blue = blue_input - min(red_input, green_input ,blue_input)

    
print(red, green, blue)


