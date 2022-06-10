from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

user_input = input(
    "Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
year = user_input[:4]
month = user_input[5:7]
day = user_input[8:]

response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/")

soup = BeautifulSoup(response.text, "html.parser")

the_list_songs = soup.select("li h3")
billboard_song_list = [the_list_songs[num].getText().strip()
                       for num in range(0, 100)]

song_uris = []

for song in billboard_song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} was not found in Spotify")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{year}-{month}-{day} Billboard 100",
    public=False,
    description=f"Billboard Top 100 From {year} year"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
