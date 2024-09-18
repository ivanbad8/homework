class WordsFinder:
    def __init__(self, name):
        self.file_names = []
        self.name = name
        file = open(name, 'a+', encoding='utf-8')
        file.close()
        self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        for text in self.file_names:
            with open(text, 'r', encoding='utf-8') as textfile:
                text_file = textfile.read()
                text_file = text_file.lower()
                text_file = text_file.translate({ord(i): None for i in ',,.=!?;:-'})
                text_file = text_file.split()
                all_words[self.name] = text_file
                return all_words

    def find(self, word: str):
        dict1 = {}
        word = word.lower()
        list1 = [*self.get_all_words().values()]
        index1 = list1[0]
        index2 = index1.index(word)
        dict1[self.name] = index2 + 1
        return dict1


    def count(self, word: str):
        dict2 = {}
        word = word.lower()
        list1 = [*self.get_all_words().values()]
        list1 = list1[0]
        num_ = 0
        for skore in list1:
            if skore == word:
                num_ += 1
        dict2[self.name] = num_
        return dict2






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
#print(finder1.get_all_words())
#print(finder1.find('captain'))
#print(finder1.count('captain'))
