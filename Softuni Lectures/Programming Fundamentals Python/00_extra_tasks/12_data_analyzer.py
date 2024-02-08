# import requests

# def get_user_info(username):
#     url = f'https://www.googleapis.com/fitness/v1/users/me/dataSources'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = data.json()
#         return data
#     else:
#         print('Error 404')
#         return None

from datetime import datetime   

def add_stats(name, weight, height, bmi, current_date):
    with open('data.txt', 'a') as f:
        f.write(str(name) + "|" + str(weight) + "|" + str(height) + "|" + str(bmi) + "|" + str(current_date) + "\n")   

def view_stats():
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            info = line.rstrip()
            name, weight, height, current_date = info.split("|")
            print("Name:", name, "Weight:", weight, "Height:", height, "BMI:", bmi, "Date:", current_date)

def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    calories_burned = duration * 5
    return calories_burned


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people

# Main program
people_data = []
overweight_people = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter person's name: ").strip()
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    current_date = datetime.now()
    people_data.append(person)
    another_person = input("Would you like to add another person? Type 'Yes' or 'no'" ).lower() #Still a bit janky
    if another_person == 'yes':
        continue
    else:
        break


print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")
    add_stats_question = input("Would you like to save the stats for later use? ").lower()
    if add_stats_question == "yes":
        add_stats(name, weight, height, round(bmi), current_date)
    else:
        read_file = input("Would you like to read saved previous calculations? ").lower() 
        if read_file == "yes":
            view_stats()


overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")

