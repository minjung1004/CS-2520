#Name: Min Jung
#Due Date: 11/30/2021
#Homework Assignment on Classes and Objects: Lab 1


class Artist:
    def __init__(self, name = "None", birth_year = 0, death_year = 0):
        #initialize consturctors
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
    def print_info(self):
        if self.death_year == -1:
            print(f'Artist: {self.name}, born {self.birth_year}')
        else:
            print(f'Artist: {self.name} ({self.birth_year}-{self.death_year})')

class Artwork:
    def __init__(self,title="None",year_created=0):
        self.title = title
        self.year_created = year_created
    def print_info(self):
        print(f'Title: {self.title}, {self.year_created}')

def main():
    user_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())
    
    user_artist = Artist(user_name, user_birth_year, user_death_year)
    user_artwork = Artwork(user_title, user_year_created)
    user_artist.print_info()
    user_artwork.print_info()
main()

        
        
    
