import random

print("Welcome to AJ's Band Name Generator")

while True:
    choice = input("How do you want your band name: 1) Random 2) Personal?\n")

    if choice == '1':
        word1 = ['Rusty', 'Gnarled', 'Rotten', 'Chrome']
        word2 = ['Hearts', 'Love', 'Serpents', 'Chains']
        print("The name of your band should be", random.choice(word1), random.choice(word2))
    
    if choice == '2':
        city = input("What is the name of the city you grew up in?\n")
        pet_name = input("What is your pet's name?\n")
        print("The name of your band should be", city, pet_name)
    
    next_name = input("Want another name? (yes/no): ")
    if next_name == 'yes':
        continue
    if next_name == 'no':
        print("Goodbye!")
        break