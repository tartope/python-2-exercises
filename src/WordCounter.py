class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        

    def count_words(self):
        # count = self.sentence.count(" ") + 1
        count = len(self.sentence.split())
        return count
    
    def get_word_count(self):
        return self.count_words()
    
    def get_shortest_word(self):
        words = self.sentence.split()
        if words:
            return min(len(word) for word in words)
        
    def get_longest_word(self):
        words = self.sentence.split()
        if words:
            return max(len(word) for word in words)
    