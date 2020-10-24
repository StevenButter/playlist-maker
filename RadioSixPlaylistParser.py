import requests
from bs4 import BeautifulSoup

RadioSixPlaylistUrl = 'https://www.bbc.co.uk/programmes/articles/5JDPyPdDGs3yCLdtPhGgWM7/bbc-radio-6-music-playlist'


def GetPlaylist():
    return _GetPlaylistFromWebsite(RadioSixPlaylistUrl)


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


if __name__ == '__main__':
    playlist = GetPlaylist()
    print(playlist)
