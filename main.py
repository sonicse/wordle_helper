import requests
import wordle

def write_russian_txt():
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    with open('data/russian.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))

exclude = 'налспишуме'
include = 'огр'

if __name__ == '__main__':
    words = wordle.words_gen("data/russian_nouns.txt")
    for word in wordle.filter_words(words, exclude=exclude, include=include, chars=['в']):
        print(f"\"{word}\"")
