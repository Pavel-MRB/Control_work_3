def is_it_palindrome(word):
    word_backwards=word[::-1]
    if word==word_backwards:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

is_it_palindrome(input('Input the word:\n'))