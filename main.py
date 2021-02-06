import RadioSixPlaylist
import spotipy
import Spotify

if __name__ == "__main__":
    playlist = RadioSixPlaylist.GetPlaylist()

    spotifyClient = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            redirect_uri='https://example.com', 
            scope='playlist-modify-private'))

    spotify = Spotify.Spotify(spotifyClient)
    clientPlaylist = spotify.CreatePlaylist("r6")
    spotify.AddToPlaylist(clientPlaylist, playlist)
    