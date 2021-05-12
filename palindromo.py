def pali(word):
    word = "".join(word.split()).lower()
    invert_word = word.replace(" ","").lower()[::-1]
    if word == invert_word:
        print('The word introduced is Palindromo')
    else:
        print('The word introduced is NOT Palindromo')

# Principal function
def run():
    word = input('Write a word: ')
    return pali(word)


#Entry point "The program starts from here"
if __name__ == '__main__':
    run()