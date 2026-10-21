import string


user_input = input("Enter a string: ")
first, last = user_input.split("-")

start = string.ascii_letters.index(first[0])
end = string.ascii_letters.index(last[-1])

print(string.ascii_letters[start:end])