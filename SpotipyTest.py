import unittest
import spotipy

ValidTrackId = '045sp2JToyTaaKyXkGejPy'


class SpotipyUnauthorisedTest(unittest.TestCase):
    def test_ShouldRaiseIfNoCreds(self):
        with self.assertRaises(spotipy.oauth2.SpotifyOauthError):
            spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(
                client_id='invalid', client_secret='invalid'))


class SpotipyTest(unittest.TestCase):

    def setUp(self):
        self._sp = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(redirect_uri='https://example.com', scope='playlist-modify-private'))

    def test_ShouldGetAllPlaylists(self):
        playlists = self._sp.current_user_playlists()

        self.assertGreater(len(playlists), 0)

    def test_SearchForTracks(self):
        search = self._SearchForValidTrack()

        trackId = search[0]['id']

        self.assertEqual(trackId, ValidTrackId)

    def test_ShouldCreatePlaylist(self):
        playlistName = 'testplaylist'

        playlist = self._CreatePrivatePlaylist(playlistName)

        self.assertEqual(playlistName, playlist['name'])

        # tear down
        self._DeletePlaylist(playlist)

    def test_ShouldAddToPlaylist(self):
        tracks = self._SearchForValidTrack()
        playlist = self._CreatePrivatePlaylist('testplaylist')

        self._sp.user_playlist_add_tracks(
            self._GetUserId(), playlist['id'], [tracks[0]['id']])

        playlistTracks = self._sp.user_playlist_tracks(
            self._GetUserId(), playlist['id'])

        self.assertIs(1, len(playlistTracks['items']))

        # tear down
        self._DeletePlaylist(playlist)

    def _GetUserId(self):
        return self._sp.me()['id']

    def _CreatePrivatePlaylist(self, name):
        return self._sp.user_playlist_create(self._GetUserId(), name, public=False)

    def _DeletePlaylist(self, playlist):
        self._sp.user_playlist_unfollow(self._GetUserId(), playlist['id'])

    def _SearchForValidTrack(self):
        search = self._sp.search('fake plastic trees', limit=1, type='track')
        return search['tracks']['items']


if __name__ == "__main__":
    unittest.main()
