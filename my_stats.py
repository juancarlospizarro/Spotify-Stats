import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET


# Configura tus credenciales
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    redirect_uri="http://localhost:8888/callback",
    scope="user-top-read user-read-recently-played"
))

# Obtener canciones más escuchadas
top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')
print("Mis 50 canciones más escuchadas de siempre año:")
for idx, track in enumerate(top_tracks['items']):
    print(f"{idx + 1}: {track['name']} - {track['artists'][0]['name']}")

print("---------------------------------------------------------")

top_artistas = sp.current_user_top_artists(limit=50, time_range='long_term')
print("Mis 50 artistas más escuchados de siempre: ")
for número, artistas in enumerate(top_artistas['items']):
    print(f"{número + 1}: {artistas['name']}")



