#Name: Min Jung
#Due Date:12/05/2021
#Final Project: Lab 1

import csv
filename = "movies.csv"

def read_movies():
    movies=[]
    with open(filename, newline="")as file:
        reader=csv.reader(file)
        for row in reader:
            movies.append(row)
    for i in range(len(movies)):
        showtime = movies[i][0]
        title = movies[i][1][:44] #limit to 44 char
        rating = movies[i][2]
        print(f'{title:<44}|{rating:>5}|{showtime}')
    return ""
def main():
    movieList = read_movies()
    print(movieList)
main()