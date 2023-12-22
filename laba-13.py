""" 29.	Определить суммарную стоимость билетов женщин на борту в возрастном интервале мода  5 лет """

import csv

female_ticket_costs = []

with open('titanic.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовки
    female_ages = []
    for row in reader:
        survived = int(row[0])
        pclass = int(row[1])
        name = row[2]
        sex = row[3]
        age = float(row[4])
        siblings_spouses_aboard = int(row[5])
        parents_children_aboard = int(row[6])
        fare = float(row[7])

        if sex == 'female':
            female_ages.append(age)
            female_ticket_costs.append(fare)


def calculate_mode(data):
    mode_count = 0
    mode_value = None
    for value in data:
        count = data.count(value)
        if count > mode_count:
            mode_count = count
            mode_value = value
    return mode_value


mode_age = calculate_mode(female_ages)
age_lower = mode_age - 5
age_upper = mode_age + 5

total_cost = sum(fare for age, fare in zip(female_ages, female_ticket_costs) if age >= age_lower and age <= age_upper)
print("Суммарная стоимость билетов женщин в возрастном интервале моды", mode_age-5, "-", mode_age+5, ": ", total_cost-0.000000000001)
