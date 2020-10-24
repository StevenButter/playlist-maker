class PlaylistEntry(object):

    def __init__(self, artist, trackName):
        self._artist = artist
        self._trackName = trackName

    def __str__(self):
        return 'Artist: ' + self._artist + ', Track: ' + self._trackName
