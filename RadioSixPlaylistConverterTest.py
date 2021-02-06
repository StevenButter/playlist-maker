import unittest
import RadioSixPlaylistConverter


class RadioSixPlaylistConverterTest(unittest.TestCase):
    def test_ShouldSplitArtistIntoMainAndFeatured(self):
        websitePlaylist = ['Deap Vally w/ jennylee - Look Away']

        playlist = RadioSixPlaylistConverter.ConvertToPlaylist(websitePlaylist)

        self.assertEqual('Deap Vally', playlist[0].Artist())


if __name__ == "__main__":
    unittest.main()
