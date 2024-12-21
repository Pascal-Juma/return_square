numbers = [3, 4, 10, 12, 5, 4, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)