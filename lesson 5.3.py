import string

def generate_hashtag(phrase):
    clean_phrase = ""
    for char in phrase:
        if char not in string.punctuation:
            clean_phrase += char

    words = clean_phrase.split()

    hashtag = "#"
    for word in words:
        hashtag += word.capitalize()

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


phrase = input("Введите строку для создания хэштега: ")
result = generate_hashtag(phrase)
print("Результат:", result)
