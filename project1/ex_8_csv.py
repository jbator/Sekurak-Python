import random
import csv

fruits = ["apple", "banana", "cherry", "orange", "blueberry", "plum", "strawberry", "lemon", "peach", "pear"]

CSV_FILE = 'test.csv'

with open(CSV_FILE, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i in range (0,30):
        fruit = random.choice(fruits)
        price = round(random.uniform(1,20), 2)
        row = (fruit, price)
        print(row)
        csv_writer.writerow(row)