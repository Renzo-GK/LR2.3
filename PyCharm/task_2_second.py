count = 0

word_1 = input("Enter word 1:\n")
word_2 = input("Enter word 2:\n")

min_length = min(len(word_1), len(word_2))

for char in range(min_length):
    if word_1[char] == word_2[char]:
        count += 1
    else:
        break

print(count)