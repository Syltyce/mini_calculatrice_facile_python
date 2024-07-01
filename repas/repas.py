import os
import random

if os.path.exists("meals.txt"):
    with open("meals.txt", "r+") as file:
        meals_list = file.readlines()
        meal_random_choice = random.choice(meals_list)
        print(f"Je vous propose aujourd'hui : {meal_random_choice}")
        file.close()

else: 
    print("le document n'existe pas")