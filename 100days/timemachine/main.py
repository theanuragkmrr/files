import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date=input("Which year do you want tp travel to? Type the date in this format yyy-mm-dd:")
response=requests.get("https://www.billboard.com/charts/hot-100/"+date)
soup=BeautifulSoup(response.text,"html.parser")
name=soup.find_all(name="h3",  class_="a-no-trucate")
titlesongs=[song.getText().strip() for song in name]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="cf058b56094a4644a4c55f9e5ba60c3e",
                                                           client_secret="4bb7689e3069495391f6c1b341cf0232",
                                               redirect_uri="http://localhost:8888/callback ",
                                               scope="playlist-modify-private",
                                               show_dialog=True,

                                               ))
user_id = sp.current_user()["id"]
year=date.split("-"[0])
song_uris=[]

for song in titlesongs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")