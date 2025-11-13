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

list_data = []
unique_restaurants = set()

# Read the CSV file and store the data into lists
def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def read_csv(file_name):
    with open(file_name, newline='', mode='r', encoding='utf-8') as file:  # fixed encoding typo
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
            list_data.append(row)
            unique_restaurants.add(row['restaurant'])

def calculateAverages(list_of_values):
    return sum(list_of_values) / len(list_of_values)

def countItems(list_of_values):
    return len(list_of_values)

def max_value(list_of_values):
    return max(list_of_values)

def min_value(list_of_values):
    return min(list_of_values)

def sugars_per_restaurant(sugars, restaurant_name):
    sugars_per = []  
    for i in range(len(restaurants)):
        if (restaurants[i] == restaurant_name):
            sugars_per.append(sugars[i]) 
    return sum(sugars_per)

def restaurants_sugars_report():
    report = {} #dictionary to hold restaurant: sugar total pairs
    for restaurant in unique_restaurants:
        total_sugars = 0
        for i in range(len(restaurants)):
            if restaurants[i] == restaurant:
                total_sugars += sugars[i]
        report[restaurant] = total_sugars

    return report




def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    read_csv(file_path)

    # Calories stats
    print("Average calories:", calculateAverages(calories))
    print("Calorie count is:", countItems(calories))
    print("Max calories is:", max_value(calories))
    print("Min calories is:", min_value(calories))  

    # Sugars stats
    print("Average sugars:", calculateAverages(sugars))
    print("Sugar count is:", countItems(sugars))
    print("Max sugars is:", max_value(sugars))
    print("Min sugars is:", min_value(sugars)) 

    # Sugars for Burger King
    print("Sugars for Burger King:", sugars_per_restaurant(sugars, "Burger King"))

    #print a report of all restaurants and the sum of their sugars
    print("\nList of restaurants and their total sugars: \n")
    report = restaurants_sugars_report()
    for result in report:
        print(result, ":", report[result])
    print("\n")



if __name__ == '__main__':
    main()