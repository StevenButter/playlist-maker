class Spotify(object):
    def __init__(self, spotifyClient):
        self._sp = spotifyClient

    def CreatePlaylist(self, playlistName):
        userId = self._sp.me()['id']
        return self._sp.user_playlist_create(userId, playlistName)

    def AddToPlaylist(self, spPlaylist, playlist):
        for entry in playlist:
            try:
                track = self._SearchForTrack(entry)
                self._AddToPlaylist(spPlaylist, track)
            except:
                print ('{} {}'.format(
                entry.Artist(), entry.TrackName()))

    def _SearchForTrack(self, playlistEntry):
        search = self._sp.search(
            '{} {}'.format(
                playlistEntry.Artist(), playlistEntry.TrackName()))
        return search['tracks']['items'][0]


    def _AddToPlaylist(self, playlist, track):
        self._sp.playlist_add_items(playlist['id'], [track['id']])
