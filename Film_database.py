import random
from datetime import date

import datetime

today_date = datetime.date.today()
new_today_date = today_date.strftime("%d.%m.%Y")


class Movie:
     def __init__(self, name, year, genre, plays):
       self.name = name
       self.year = year
       self.genre = genre
       self.plays = plays
     def __str__(self):
         return f'{self.name} ({self.year})'
     def play(self, plays):
         plays = plays + 1
     def __eq__(self, other):
         return (
             self.name == other.name)

class Series(Movie):
     def __init__(self,episode_number, season_number, *args, **kwargs):
         self.episode_number = episode_number
         self.season_number = season_number
         super().__init__(*args, **kwargs)
     def __str__(self):
         if self.season_number > 9 and self.episode_number > 9:
            return f'{self.name} S{self.season_number}E{self.episode_number}'
         elif self.season_number < 10 and self.episode_number > 9:
            return f'{self.name} S0{self.season_number}E{self.episode_number}'  
         elif self.season_number < 10 and self.episode_number < 10:
            return f'{self.name} S0{self.season_number}E0{self.episode_number}' 
         elif self.season_number > 9 and self.episode_number < 10:
            return f'{self.name} S{self.season_number}E0{self.episode_number}'   
     def play(self, plays):
         plays = plays + 1

def get_movies(list):
     movie_list = []
     for item in list:
         if type(item) == Movie:
             movie_list.append(item)
     return sorted(movie_list, key=lambda c: c.name)
     
def get_series(list):
     series_list = []
     for item in list:
         if type(item) == Series:
             series_list.append(item)
     return sorted(series_list, key=lambda c: c.name)
     
def search(title, list):
         for item in list:
            if item.name == title:
             return item

def generate_views(list):
    random_item = random.choice(list)
    random_item.plays = random_item.plays + random.randint(0, 100)
    return list

def generate_views_ten_times(list):
    for a in range (0,10):
        generate_views(list)
    return list
        
def top_titles(content_type, list, how_many):
    if content_type == "M":
        list = get_movies(list)
    elif content_type == "S":
        list = get_series(list)
    return sorted(list, key=lambda c: c.plays)[-(how_many):]
     
def add_season(list, title, year, genre, season_number, how_many_episodes):
    for number in range (1, how_many_episodes + 1):
        episode = Series(name=title, year=year, genre=genre, episode_number=number, season_number=season_number, plays=0)
        list.append(episode)
    return list

def how_many_episodes(name,list):
    how_many = 0
    for item in list:
        if item.name == name:
            how_many = how_many +1
        else:
            pass
    return how_many


# Run
print("Biblioteka filmów")

movie1 = Movie(name="Pulp Fiction", year=1986, genre="action", plays=0)
movie2 = Movie(name="Hulk", year=1999, genre="sci-fi", plays=0)
movie3 = Movie(name="Orange", year=1988, genre="drama", plays=0)
movie4 = Movie(name="Shrek", year=2002, genre="animated", plays=0)
series1 = Series(name="Friends", year=2002, genre="comedy", episode_number=1, season_number=3, plays=0)
all_list = [movie1, movie2, movie3, movie4, series1]  

add_season(all_list, "HIMYM", 2021, "comedy", 4, 9)
add_season(all_list, "Scrubs", 2009, "comedy", 2, 8)

generate_views_ten_times(all_list)

print(f"\nNajpopularniejsze filmy dnia {new_today_date}")

for a in (top_titles("M",all_list,3)):
    print(a)

print(f"\nNajpopularniejsze seriale dnia {new_today_date}")
for a in (top_titles("S",all_list,3)):
    print(a)

