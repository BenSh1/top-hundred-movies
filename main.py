import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Inspect the page to find the movie titles – they're in <h3> tags with class 'title'
#print(soup.prettify())

movie_title_elements  = soup.find_all('h3', class_='title')

movie_titles = [movie.getText() for movie in movie_title_elements ]
movies = movie_titles[::-1]

with open("movies.txt",mode="w" , encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


