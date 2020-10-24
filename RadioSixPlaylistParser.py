import requests
from bs4 import BeautifulSoup
from PlaylistEntry import PlaylistEntry

RadioSixPlaylistUrl = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'


def GetPlaylist():
    websitePlaylist = _GetPlaylistFromWebsite(RadioSixPlaylistUrl)
    return _ConvertToPlaylist(websitePlaylist)


def _GetPlaylistFromWebsite(website):
    rsp = requests.get(website)
    if not rsp.ok:
        raise
    return _ExtractEntriesFromHtml(rsp.content)


def _ExtractEntriesFromHtml(rspContent):
    soup = BeautifulSoup(rspContent, "html.parser")
    allProseTags = soup.find_all(class_='text--prose')[1:4]

    searches = []
    for proseTag in allProseTags:
        pTags = proseTag.find_all('p')
        for pTag in pTags:
            searches.append(pTag.get_text())
    return searches


def _ConvertToPlaylist(websitePlaylist):
    return [_ConvertToPlaylistItem(x) for x in websitePlaylist]


def _ConvertToPlaylistItem(websitePlaylistItem):
    HyphenSep = ' - '
    DashSep = ' – '

    sep = HyphenSep if HyphenSep in websitePlaylistItem else DashSep
    separated = websitePlaylistItem.split(sep, 2)

    return PlaylistEntry(separated[0], separated[1])
