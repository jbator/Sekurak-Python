import random
import csv

fruits = ("apple", "banana", "cherry", "orange", "blueberry", "plum", "strawberry", "lemon", "peach", "pear", "mandarin")

def generate_fruits_list():
    list_fruits = []
    for i in range(0, 30):
        fruit = random.choice(fruits)
        price = round(random.uniform(1, 20), 2)
        row = (fruit, price)
        list_fruits.append(row)
    return list_fruits

CSV_FILE = 'test.csv'

def generate_fruits_csv():
    with open(CSV_FILE, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        price_list = generate_fruits_list()
        for price_row in price_list:
            csv_writer.writerow(price_row)

generate_fruits_csv()