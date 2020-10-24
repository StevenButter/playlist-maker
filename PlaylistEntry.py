class PlaylistEntry(object):

    def __init__(self, artist, trackName):
        self._artist = artist
        self._trackName = trackName

    def Artist(self):
        return self._artist

    def TrackName(self):
        return self._trackName

    def __eq__(self, other):
        return self._artist == other._artist and self._trackName == other._trackName
