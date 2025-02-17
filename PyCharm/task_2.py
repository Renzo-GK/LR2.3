#Part 1
count = 0

word_1 = input("Enter word 1:\n")
word_2 = input("Enter word 2 (does not match with word 1):\n")

for char1, char2 in zip(word_1, word_2):
#С помощью функции zip проходит по парам символов из обоих слов.
    if char1 == char2:
        count += 1
    else:
        break

print(count)