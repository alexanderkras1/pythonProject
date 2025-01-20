from collections import Counter

def popular_words (text, words):
    text = text.lower()
    word_list = text.split()
    word_count = Counter(word_list)

    return {word: word_count.get(word, 0 ) for word in words}


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'

print('OK')


