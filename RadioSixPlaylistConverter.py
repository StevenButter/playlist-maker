from PlaylistEntry import PlaylistEntry


def ConvertToPlaylist(websitePlaylist):
    return [_ConvertToPlaylistItem(x) for x in websitePlaylist if x.strip()]


def _ConvertToPlaylistItem(websitePlaylistItem):
    splitItem = _SplitItem(websitePlaylistItem)
    artists = _SplitArtists(splitItem[0])
    trackName = splitItem[1]

    return PlaylistEntry(
        _GetMainArtist(artists),
        trackName,
        featuredArtists=_GetFeatArtists(artists))


def _SplitItem(item):
    HyphenSep = ' - '
    DashSep = ' – '

    return item.split(HyphenSep if HyphenSep in item else DashSep, 2)


def _SplitArtists(item):
    FeatArtistSep = ' ft. '
    otherFeatArtistsep = [' w/ ', ' & ']

    for sep in otherFeatArtistsep:
        item = item.replace(sep, FeatArtistSep)

    return item.split(FeatArtistSep, 2)


def _GetMainArtist(artists):
    return artists[0]


def _GetFeatArtists(artists):
    return artists[1] if len(artists) == 2 else None
