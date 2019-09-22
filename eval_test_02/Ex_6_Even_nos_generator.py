def generate_even(n):
    # returns even numbers from 0 and less than n
    for i in range(n):
        if i % 2 == 0:
            yield i


num = int(input('Enter the last number - '))
for even_number in generate_even(num):
    print(even_number)
