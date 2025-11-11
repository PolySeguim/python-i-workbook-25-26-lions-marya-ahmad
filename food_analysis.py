
import tkinter as tk
from tkinter import filedialog
import csv

# Define the lists to store data
restaurants = []
items = []
types = []
serving_sizes = []
calories = []
fats = []
sodiums = []
sugars = []

# Read the CSV file and store the data into lists

def choose_file():
    root = tk.Tk()
    root.withdraw()  #Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    #print(file_path)
    return file_path

def read_csv(file_name):
    with open(file_name, newline='', mode='r', encoding='utf=8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurants.append(row['restaurant'])
            items.append(row['item'])
            types.append(row['type'])
            serving_sizes.append(float(row['serving_size']))
            calories.append(int(row['calories']))
            fats.append(float(row['fat']))
            sodiums.append(float(row['sodium']))
            sugars.append(float(row['sugars']))

def calculateAverages(list_of_values):
    average = sum(list_of_values)/len(list_of_values)
    return average

def countItems(list_of_values):
    return len(list_of_values)

def max_value(list_of_values):
    return max(list_of_values)

def min_value(list_of_values):
    return min(list_of_values)

def sugars_per_restaurant(sugars, restaurant_name):
    sugars_per = {}
    for i in range(len(restaurants)):
        if (restaurants[i] == restaurant_name):
            sugars_per.append(sugars)
    return sum(sugars_per)


def main():
    #Read and load data from a CSV file
    file_path = choose_file()
    #read_file (file_path)
    read_csv(file_path)

    #Calculate Averages
    #Average Calories
    average_calories = calculateAverages(calories)
    print("Average calories", average_calories)

    #Calculate the number of items per list
    count_calories = countItems(calories)
    print("Calorie count is", count_calories)

    #Calculate the highest value per list 
    max_calories = max_value(calories)
    print("Max calories is: ", max_calories)

    #Calculate Averages
    #Average Sugars
    average_sugars = calculateAverages(sugars)
    print("Average sugars", average_sugars)

    #Calculate the number of items per list
    count_sugars = countItems(sugars)
    print("Sugar count is", count_sugars)

    #Calculate the highest value per list 
    max_sugars = max_value(sugars)
    print("Max sugars is: ", max_sugars)

    #Calculate the lowest value per list
    min_sugars = max_value(sugars)
    print("Max sugars value: ", min_sugars)

    #Calculate the lowest value per list
    min_calories = max_value(calories)
    print("Max Calorie value: ", min_calories)

    print("Sugars for Burger King:", sugars_per_restaurant(sugars, "Burger King"))
    



if __name__ == '__main__':
    main()

