import unittest
from unittest.mock import Mock, patch
import RadioSixPlaylistParser
from PlaylistEntry import PlaylistEntry
import encodings

PlaylistEntries = [PlaylistEntry('A artist', 'track name'), PlaylistEntry('A artist ft. feat artist', 'track name'), PlaylistEntry('B artist', 'track name'), PlaylistEntry(
    'B artist ft. feat artist', 'track name'), PlaylistEntry('C artist', 'track name'), PlaylistEntry('C artist ft. feat artist', 'track name'), ]


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
    pTagContents = []
    for entry in entries:
        pTagContents.append('{0} {1} {2}'.format(
            entry.Artist(), sep, entry.TrackName()))

    with open('RadioSixTestPage.html', 'r') as webPage:
        return webPage.read().format(*pTagContents)


if __name__ == "__main__":
    unittest.main()
