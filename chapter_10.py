# ============
# Chapter 10
# ============

### file_reader
from pathlib import Path

path = Path("text_file/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

# pi_birthday

# birthday = input("Enter your birthday (dd:mm:yy): ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# Try it yourself
# 10.1
study = Path("learning_python.txt")
learned = study.read_text()

print(learned)

rows = learned.splitlines()
for study in rows:
    print(study)

# 10.2
for study in rows:
    print(study.replace("python", "C"))

# 10.3
for lines in learned.splitlines():
    print(lines.replace("python", "C++"))
