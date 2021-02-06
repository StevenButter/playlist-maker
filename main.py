import RadioSixPlaylist
import spotipy
import Spotify
from datetime import datetime


def _GetDate():
    return datetime.today().strftime('%Y-%m-%d')


if __name__ == "__main__":
    playlist = RadioSixPlaylist.GetPlaylist()

    spotifyClient = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            redirect_uri='https://example.com',
            scope='playlist-modify-private'))

    spotify = Spotify.Spotify(spotifyClient)
    clientPlaylist = spotify.CreatePlaylist('{} - {}'.format('r6', _GetDate()))
    spotify.AddToPlaylist(clientPlaylist, playlist)
