class PlaylistEntry(object):

    def __init__(self, artist, trackName, featuredArtists=None):
        self._artist = artist
        self._trackName = trackName
        self._featuredArtists = featuredArtists

    def Artist(self):
        return self._artist

    def TrackName(self):
        return self._trackName

    def FeaturedArtists(self):
        return self._featuredArtists

    def __eq__(self, other):
        return self._artist == other._artist and self._trackName == other._trackName and self._featuredArtists == other._featuredArtists
