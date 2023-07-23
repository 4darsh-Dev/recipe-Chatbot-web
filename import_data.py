# Created by Admin

import os
import django

# Replace 'your_project_name' with the actual name of your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recpieChatbot.settings')

# Ensure Django is configured before accessing any Django components
django.setup()

# Takes datasets from csv and import it into the database

import csv

from home.models import Recipe

def import_recipes(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            recipe = Recipe(
                # srNo = row['Srno'],
                title = row['RecipeName'],
                
                ingredients=row['Ingredients'],
                instructions=row['Instructions'],
                prepTimeInMins = row['PrepTimeInMins'],
                cookTimeInMins = row['CookTimeInMins'],
                totalTimeInMins = row['TotalTimeInMins'],
            )

            recipe.save()


if __name__ == "__main__":
    csv_file_path = "indian_recipes.csv"  #Actual path of your CSV file
    import_recipes(csv_file_path)
