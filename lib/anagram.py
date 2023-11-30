# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        # Check if two words are anagrams by comparing sorted lists of their letters
        return sorted(self.word) == sorted(other_word.lower())

# Example usage:
if __name__ == "__main__":
    listen = Anagram("listen")
    result = listen.match(['enlists', 'google', 'inlets', 'banana'])
    print(result)
