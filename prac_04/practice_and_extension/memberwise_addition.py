"""
Add together two lists on each element and displays the new list of added values
"""


def main():
    """Display two lists of numbers added together memberwise"""
    numbers1 = [1, 2, 3]
    numbers2 = [1, 2, 3, 4]

    numbers_total = add_memberwise(numbers1, numbers2)
    print(numbers_total)


def add_memberwise(numbers1, numbers2):
    """Adds two lists together for each element"""
    numbers_total = []
    if len(numbers1) >= len(numbers2):
        for index, number in enumerate(numbers2):
            numbers_total.append(number + numbers1[index])
        numbers_total += numbers1[len(numbers2):]
    elif len(numbers1) < len(numbers2):
        for index, number in enumerate(numbers1):
            numbers_total.append(number + numbers2[index])
        numbers_total += numbers2[len(numbers1):]
    return numbers_total


main()
