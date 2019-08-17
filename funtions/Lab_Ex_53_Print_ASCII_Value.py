# Program to convert entered string/character to ASCII value
def string_to_ascii(string_value):
    return ord(string_value)


choice = input('Enter a Character or Text to convert - ')

print("Char\tASCII = ")
for char in choice:
    print("{0}\t{1}".format(char, string_to_ascii(char)))
