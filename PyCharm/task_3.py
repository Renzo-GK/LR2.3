input_text = input("Enter anything text\n")

letter_to_remove = ["c", "с", "C", "С"]

result = input_text

for letter in letter_to_remove:
    result = result.replace(letter, "")

print(result)