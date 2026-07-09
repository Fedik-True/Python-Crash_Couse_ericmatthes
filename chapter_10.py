# ============
# Chapter 10
# ============
from pathlib import Path

### file_reader
# from pathlib import Path

# path = Path("text_file/pi_million_digits.txt")
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.lstrip()

# pi_birthday

# birthday = input("Enter your birthday (dd:mm:yy): ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# Try it yourself
# 10.1
# study = Path("learning_python.txt")
# learned = study.read_text()

# print(learned)

# rows = learned.splitlines()
# for study in rows:
#     print(study)

# # 10.2
# for study in rows:
#     print(study.replace("python", "C"))

# # 10.3
# for lines in learned.splitlines():
#     print(lines.replace("python", "C++"))


# # write_message
# contentss = "I love programming.\n"
# contentss += "I love creating new games.\n"
# contentss += "I also love working with data.\n"

# paath = Path("text_file/programming.txt")
# paath.write_text(contentss)


# try it yourself
# 10.4 Guest
# name = input("Enter your name: ")
# name_path = Path("text_file/guest_book.txt")
# name_path.write_text(name)

# 10.5 Guest_book
names_path = Path("text_file/guest_book.txt")
names = []
while True:
    namee = input("Enter a name ('q' to quit): ").lower()
    if namee == "q":
        break
    names.append(namee)

# print(type(names))
# print(names)
names_path.write_text("\n".join(names))


# EXCEPTIONS
# division_calculator
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No no no no")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# alice, word_count


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contentsss = filename.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contentsss.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = [
    "text_file/alice.txt",
    "text_file/siddharthas.txt",
    "text_file/moby_dick.txt",
    "text_file/little_women.txt",
]
for filename in filenames:
    path = Path(filename)
    count_words(path)


# try it yourself
# 10.6, 10.7
print("Enter 'q' to quit.")
while True:
    try:
        number1 = int(input("First nuumber: "))
        if number1 == "q":
            break
        number2 = int(input("Second number: "))
        if number2 == "q":
            break
        result = number1 + number2
        print(result)
    except ValueError:
        print("You have to enter a number!")
        pass

# 10.8, 10.9
animal_files = ["text_file/dogs.txt", "text_file/cats.txt"]
try:
    for files in animal_files:
        path = Path(files)
        animals = path.read_text(encoding="utf-8")
        print(animals)
except FileNotFoundError:
    pass

# 10.10
counter_tester = Path("text_file/moby_dick.txt")
counter = counter_tester.read_text(encoding="utf-8")
print(counter.lower().count(" the "))
