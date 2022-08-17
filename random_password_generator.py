import random
from unicodedata import name

characters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", ",", "|", ":", ";", "<", ">", ".", "?",
              "/")
print(characters[52])
users_permission = input(
    "\nYou need a random password generated for you: yes or no: ")


def generate_random_password():
    pass_count = 0
    random_char = ""
    while pass_count < 10:
        random_num = random.randint(0, 51)
        random_char += characters[random_num]
        # print(pass_count)
        pass_count += 1
    pass_count = 0
    while pass_count < 5:
        random_num = random.randint(52, len(characters) - 1)
        random_char += characters[random_num]
        pass_count += 1

    return random_char


if users_permission.lower() == "yes":
    print("Your new password is => ", generate_random_password())


class Person():
    account = 2000000

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def Speak(self, msg):
        return msg


class Voter(Person):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def Vote(self, candidate):
        return f"I voted {candidate}"


person1 = Person("John", "Developer")
person2 = Person("Manny", "Software Engineer")
person3 = Person("Daniel", "Graphics designer")
person4 = Person("Jesse", "Data Analyst")

# voter = Voter("Emmanuel", "Citizen")
# print(voter.Speak("I can speak"))

print(person1.Speak("I can speak"))
print(person1.name, "has ", person1.account)
print(person2.name, "has ", person2.account)
print(person3.name, "has ", person3.account)
print(person4.name, "has ", person4.account)

voter = Voter("Manny", "Akute")
print(voter.Vote("Peter Obi"))
print(voter.Speak("This voter can speak"))
print(person1.Vote("Peter Obi"))
