from PlaylistEntry import PlaylistEntry


def ConvertToPlaylist(websitePlaylist):
    return [_ConvertToPlaylistItem(x) for x in websitePlaylist]


def _ConvertToPlaylistItem(websitePlaylistItem):
    HyphenSep = ' - '
    DashSep = ' – '
    FeatArtistSep = ' ft. '

    separated = websitePlaylistItem.split(
        HyphenSep if HyphenSep in websitePlaylistItem else DashSep, 2)
    artists = separated[0].split(FeatArtistSep, 2)
    trackName = separated[1]

    mainArtist = artists[0]
    featArtist = artists[1] if len(artists) == 2 else None

    return PlaylistEntry(mainArtist, trackName, featuredArtists=featArtist)
