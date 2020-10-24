import requests
from bs4 import BeautifulSoup

RadioSixPlaylistUrl = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'


def GetPlaylist():
    return _GetPlaylistFromWebsite(RadioSixPlaylistUrl)


def _GetPlaylistFromWebsite(website):
    rsp = requests.get(website)
    if not rsp.ok:
        raise
    return rsp.content


if __name__ == '__main__':
    playlist = GetPlaylist()
    print(playlist)
