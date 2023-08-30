import requests
from bs4 import BeautifulSoup

response=requests.get("https://web.archive.org/web/20200518073855/https:"
                      "//www.empireonline.com/movies/features/best-movies-2/")

data=response.text

soup=BeautifulSoup(data,"html.parser")
all_movies=soup.findAll(name="h3",class_="title")
movie_title=[movie.getText() for movie in all_movies]
movies=movie_title[::-1]

with open("100movies.txt","w", encoding="utf-8") as f:
    for movie in movies:
        f.write(f"{movie}\n")
