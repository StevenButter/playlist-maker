import unittest
from unittest.mock import Mock, patch
import RadioSixPlaylistParser
from PlaylistEntry import PlaylistEntry
import encodings

PlaylistEntries = [
    PlaylistEntry('A artist', 'track name'),
    PlaylistEntry('A artist', 'track name', featuredArtists='feat artist'),
    PlaylistEntry('B artist', 'track name'),
    PlaylistEntry('B artist', 'track name', featuredArtists='feat artist'),
    PlaylistEntry('C artist', 'track name'),
    PlaylistEntry('C artist', 'track name', featuredArtists='feat artist')]


class RadioSixPlaylistParserTest(unittest.TestCase):
    @patch('requests.get')
    def test_ShouldRaiseExceptionIfRspNotOk(self, mockGet):
        mockGet.return_value.ok = False

        with self.assertRaises(Exception):
            RadioSixPlaylistParser.GetPlaylist()

    @patch('requests.get')
    def test_ShouldRaiseExceptionIfRspContentEmpty(self, mockGet):
        mockGet.return_value.ok = True
        mockGet.return_value.content = ""
        playlist = RadioSixPlaylistParser.GetPlaylist()

        self.assertListEqual(playlist, [])

    @patch('requests.get')
    def test_ShouldReadPlaylistWithHypenSep(self, mockGet):
        mockGet.return_value.ok = True
        mockGet.return_value.content = LoadTestWebPage(PlaylistEntries, '-')

        playlist = RadioSixPlaylistParser.GetPlaylist()

        self.assertListEqual(playlist, PlaylistEntries)

    @patch('requests.get')
    def test_ShouldReadPlaylistWithDashSep(self, mockGet):
        mockGet.return_value.ok = True
        mockGet.return_value.content = LoadTestWebPage(PlaylistEntries, '–')

        playlist = RadioSixPlaylistParser.GetPlaylist()

        self.assertListEqual(playlist, PlaylistEntries)


def LoadTestWebPage(entries, sep):
    with open('RadioSixTestPage.html', 'r') as webPage:
        pTagContents = [MakeString(entry, sep) for entry in entries]
        return webPage.read().format(*pTagContents)


def MakeString(playlistEntry, sep):
    featuredArtistsStr = ' ft. ' + \
        playlistEntry.FeaturedArtists() if playlistEntry.FeaturedArtists() else ''

    return '{0}{1} {2} {3}'.format(playlistEntry.Artist(), featuredArtistsStr, sep, playlistEntry.TrackName())


if __name__ == "__main__":
    unittest.main()
