"""Generate a silly name by randomly selecting a first and last name from 2 tuples"""
import sys
import random


def main():
    """Choose names at random from 2 tuples and print"""
    print("Welcome to the random name generator. Use it for gags, insults, maybe even usernames?!"
          "The possibilities are endless")


first = ("Baby Oil", "Bad News", "Big Burps", "Bill '/Beenie Weenie/'", "Bob Stinkbug",
         "Bowel Noises", "Lunch Money", "Bud Lite", "Butterbean", "Buttermilk", "Chad")
last = ("Appleyard", "Bigmeat", "Bloominshine", "Boogerbottom", "Breedslovetrout", "Butterbaugh",
        "Clovenhoof", "Clutterbuck", "Guster", "Poopoo", "Beans", "Johnson", "Fewhairs", "Jenkins")

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("\n")
    print(f"A new {firstName} {lastName} has joined the chat", file=sys.stderr)
    print("\n")
    more_names = input("Press enter to continue, n to exit")
    if more_names.lower() == "n":
        break
input("Press enter to exit")

if __name__ == "__main__":
    main()
