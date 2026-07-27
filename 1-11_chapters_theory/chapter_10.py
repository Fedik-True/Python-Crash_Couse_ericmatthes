# # # ============
# # # Chapter 10
# # # ============
# # from pathlib import Path

# # ### file_reader
# # # from pathlib import Path

# # # path = Path("text_file/pi_million_digits.txt")
# # # contents = path.read_text()

# # # lines = contents.splitlines()
# # # pi_string = ""
# # # for line in lines:
# # #     pi_string += line.lstrip()

# # # pi_birthday

# # # birthday = input("Enter your birthday (dd:mm:yy): ")
# # # if birthday in pi_string:
# # #     print("Your birthday appears in the first million digits of pi!")
# # # else:
# # #     print("Your birthday does not appear in the first million digits of pi.")


# # # Try it yourself
# # # 10.1
# # # study = Path("learning_python.txt")
# # # learned = study.read_text()

# # # print(learned)

# # # rows = learned.splitlines()
# # # for study in rows:
# # #     print(study)

# # # # 10.2
# # # for study in rows:
# # #     print(study.replace("python", "C"))

# # # # 10.3
# # # for lines in learned.splitlines():
# # #     print(lines.replace("python", "C++"))


# # # # write_message
# # # contentss = "I love programming.\n"
# # # contentss += "I love creating new games.\n"
# # # contentss += "I also love working with data.\n"

# # # paath = Path("text_file/programming.txt")
# # # paath.write_text(contentss)


# # # try it yourself
# # # 10.4 Guest
# # # name = input("Enter your name: ")
# # # name_path = Path("text_file/guest_book.txt")
# # # name_path.write_text(name)

# # # 10.5 Guest_book
# # names_path = Path("text_file/guest_book.txt")
# # names = []
# # while True:
# #     namee = input("Enter a name ('q' to quit): ").lower()
# #     if namee == "q":
# #         break
# #     names.append(namee)

# # # print(type(names))
# # # print(names)
# # names_path.write_text("\n".join(names))


# # # EXCEPTIONS
# # # division_calculator
# # try:
# #     print(5 / 0)
# # except ZeroDivisionError:
# #     print("No no no no")

# # print("Give me two numbers, and I'll divide them.")
# # print("Enter 'q' to quit.")

# # while True:
# #     first_number = input("\nFirst number: ")
# #     if first_number == "q":
# #         break
# #     second_number = input("Second number: ")
# #     if second_number == "q":
# #         break
# #     try:
# #         answer = int(first_number) / int(second_number)
# #     except ZeroDivisionError:
# #         print("You can't divide by 0!")
# #     else:
# #         print(answer)


# # # alice, word_count


# # def count_words(filename):
# #     """Count the approximate number of words in a file."""
# #     try:
# #         contentsss = filename.read_text(encoding="utf-8")
# #     except FileNotFoundError:
# #         pass
# #     else:
# #         # Count the approximate number of words in the file:
# #         words = contentsss.split()
# #         num_words = len(words)
# #         print(f"The file {filename} has about {num_words} words.")


# # filenames = [
# #     "text_file/alice.txt",
# #     "text_file/siddharthas.txt",
# #     "text_file/moby_dick.txt",
# #     "text_file/little_women.txt",
# # ]
# # for filename in filenames:
# #     path = Path(filename)
# #     count_words(path)


# # # try it yourself
# # # 10.6, 10.7
# # print("Enter 'q' to quit.")
# # while True:
# #     try:
# #         number1 = int(input("First nuumber: "))
# #         if number1 == "q":
# #             break
# #         number2 = int(input("Second number: "))
# #         if number2 == "q":
# #             break
# #         result = number1 + number2
# #         print(result)
# #     except ValueError:
# #         print("You have to enter a number!")
# #         pass

# # # 10.8, 10.9
# # animal_files = ["text_file/dogs.txt", "text_file/cats.txt"]
# # try:
# #     for files in animal_files:
# #         path = Path(files)
# #         animals = path.read_text(encoding="utf-8")
# #         print(animals)
# # except FileNotFoundError:
# #     pass

# # # 10.10
# # counter_tester = Path("text_file/moby_dick.txt")
# # counter = counter_tester.read_text(encoding="utf-8")
# # print(counter.lower().count(" puss "))

# import json
# from pathlib import Path

# # number_writer

# # numbers = [2, 3, 5, 7, 11, 13]

# # path = Path("text_file/numbers.json")
# # contents = json.dumps(numbers)
# # path.write_text(contents)

# # number_reader
# # path = Path("text_file/numbers.json")
# # contents = path.read_text()
# # numbers = json.loads(contents)
# # print(numbers)

# # username = input("What is your name? ").title()

# # path = Path("text_file/username.json")
# # contents = json.dumps(username)
# # path.write_text(contents)

# # print(f"We'll remember you when you come back, {username}!")

# # path = Path("text_file/username.json").read_text()
# # username = json.loads(path)
# # print(f"Welcome back, {username}!")


# def get_stored_username(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None


# def get_new_username(path):
#     """Prompt for a new username."""
#     username = input("What is your name! ").title()
#     contents = json.dumps(username)
#     path.write_text(contents)
#     return username


# def greet_user():
#     """Greet the user by name."""
#     path = Path("text_file/username.json")
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = get_new_username(path)
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()


# Try it yourself
# 10.11, 10.12
import json
from pathlib import Path

# def store_number(number):
#     path = Path("text_file/fav_number.json")
#     path.write_text(json.dumps(number))


# def get_number():
#     path = Path("text_file/fav_number.json")
#     return json.loads(path.read_text())


# def initial_program():
#     path = Path("text_file/fav_number.json")

#     if path.exists():
#         print(f"Your favorite number is {get_number()}")
#     else:
#         number = int(input("What is your favorite number? "))
#         store_number(number)
#         print(f"The number {number} was stored as your favorite!")


# initial_program()


# 10.13

FILE = Path("text_file/username.json")


def store_user_data(name, age, city):
    """Stores user's information."""
    data = {"name": name, "age": age, "city": city}
    FILE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def get_user_data():
    """Get user's information."""
    return json.loads(FILE.read_text(encoding="utf-8"))


def store_data():
    """Stores the information"""
    name = input("Enter your name: ").title()
    age = int(input("Enter your age: "))
    city = input("Enter city you live in: ").title()
    store_user_data(name, age, city)
    print("Your data has been stored!")


def initial_program():
    """Start of the program."""
    check_name = input("What is your name? ").title()
    if FILE.exists():
        data = get_user_data()
        if check_name == data["name"]:
            print(
                f"Welcome back, {data['name']} from {data['city']}. Age: {data['age']}."
            )
        else:
            store_data()
    else:
        store_data()


initial_program()
