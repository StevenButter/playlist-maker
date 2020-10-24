import requests
from bs4 import BeautifulSoup


def GetPlaylistFromWebsite(url):
    rsp = requests.get(url)
    if not rsp.ok:
        raise
    return _ExtractEntriesFromHtml(rsp.content)


def _ExtractEntriesFromHtml(rspContent):
    soup = BeautifulSoup(rspContent, "html.parser")
    allProseDivs = soup.find_all(class_='text--prose')[1:4]

    return [pTag.get_text() for proseDiv in allProseDivs for pTag in proseDiv.find_all('p')]
