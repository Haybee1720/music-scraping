import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth


Client_ID = "d47XXXXXXXXXX....2c273f"
Client_Secret = "342f4XXXXX.......8a5"



sp = spotipy.Spotify(auth="BQAS9LYNDGGDXTlra-0zvk7UXX-UXzGghowbTADMMlei7CvydLG1AzYFyLbHrO11Sev1OhamjTi9Lo7_XHM9m62ZbaNuY-dhrTzk6Evejukco4dM6DJmSrTNqUp6v3-p9pJp6oOpy5011ZYC4nnC1yIxiHRL4bCDwETUtlwzZac2r5gTDDZppJs2-b2ZprZLvRZb0vxpGDU8TBi4W-guJvOpJO-2-uVwvPJ1YQ")

user_id = sp.current_user()["id"]

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")

stuff = response.text

soup = BeautifulSoup(stuff, "html.parser")

songs = soup.find_all(name="h3", class_="title-of-a-story")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

song_names = [song.getText().strip()  for song in soup.select(selector="ul li ul li h3")]

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="private")
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


