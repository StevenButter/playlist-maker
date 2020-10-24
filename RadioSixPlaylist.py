from RadioSixPlaylistRetriever import GetPlaylistFromWebsite
from RadioSixPlaylistConverter import ConvertToPlaylist

RadioSixPlaylistUrl = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'


def GetPlaylist():
    websitePlaylist = GetPlaylistFromWebsite(RadioSixPlaylistUrl)
    return ConvertToPlaylist(websitePlaylist)
