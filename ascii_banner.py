import pyfiglet
import random


FONTS = ["slant", "3-d", "5lineoblique", "alligator", "bubble", "digital"]

def generate_banner(text):
    font = random.choice(FONTS)
    banner = pyfiglet.figlet_format(text, font=font)
    return banner

if __name__ == "__main__":
    user_text = input("Enter text for your banner: ")
    print(generate_banner(user_text))