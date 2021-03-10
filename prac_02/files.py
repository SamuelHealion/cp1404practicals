# Asks for name and writes to a file called name.txt
out_file = open("name.txt", 'w')
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

# Opens name.txt and then reads name
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print("Your name is ", name)

# Reads the first two numbers in numbers.txt and then adds them together
in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# Reads the numbers in a text file and then adds all the numbers together
total = 0
in_file = open("numbers.txt", 'r')
for line in in_file:
    number = int(line)
    total += number

in_file.close()
print("Your total is: ", total)
