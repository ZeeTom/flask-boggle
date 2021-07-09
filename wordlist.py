class WordList:
    """Searchable list of words from a file.

    This isn't Boggle-specific (you could use it for Scrabble or other word
    games), so there's no Boggle-specific logic in it.
    """

    def __init__(self, dict_path="dictionary.txt"):
        """Create a word list from a dictionary file on disk.

            >>> wl = WordList("test_dictionary.txt")
            >>> wl.words == {'CAT', 'DOG'}
            True
        """

        self.words = self._read_dict(dict_path)

    def __repr__(self):
        return f"<WordList len={len(self.words)}>"

    def _read_dict(self, dict_path):
        """Read dictionary file at dict_path and return set of words."""

        dict_file = open(dict_path)
        words = {w.strip().upper() for w in dict_file}
        dict_file.close()
        return words

    def check_word(self, word):
        """Is word in word list?

            Searches to find if a word in the list exists, returns a boolean

            >>> wl = WordList("test_dictionary.txt")

            CAT exists in word list, should return True

            >>> wl.check_word('CAT')
            True

            HORSE does not exist in word list, should return False
            
            >>> wl.check_word('HORSE')
            False
        """

        return word in self.words


english_words = WordList("dictionary.txt")
