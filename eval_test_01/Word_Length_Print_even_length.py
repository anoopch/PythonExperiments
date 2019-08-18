# Program to print even length words in a paragraph
def is_word_length_even(word):
    return len(word) % 2 == 0


menu_choice = str(input('Enter the Words(Press <Enter>) to stop input : '))
print('The even words are as follows ')

for m_word in menu_choice.split(' '):
    if is_word_length_even(m_word):
        print(m_word)

