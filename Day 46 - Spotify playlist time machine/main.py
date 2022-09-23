import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "client id"
CLIENT_SECRET = "client secret"

date = input("What year you want to travel to?Type the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100"

#response = requests.get(f"{URL}/{date}")
response = requests.get("https://www.billboard.com/charts/hot-100/2002-06-28/")

datos = response.text


soup = BeautifulSoup(datos, "html.parser")
songs = soup.select(selector="li h3", class_="c-title")
songs_names = [song.getText().strip("\n\t") for song in songs]
print(songs_names)

year = date.split("-")[0]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )
user_id = sp.current_user()["id"]

songs_uris = []
for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, public=True, name=f"{date} Billboard 100")
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
print(playlist["id"])