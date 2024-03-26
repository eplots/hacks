#!/usr/bin/env python3
import glob
from sklearn.model_selection import train_test_split

data = glob.glob("../raw_data/*.png")

print(data)

dataset = []
labels = []

for item in data:
    label = item.split('/')[1].replace(".png","") #dataset/32154.png
    labels.append(label)
    dataset.append(item)

train_X, validate_X, train_y, validate_y = train_test_split(dataset, labels, test_size=0.2)

f = open('training.txt', 'w')

count = 0

for count in range(len(train_X)):
    f.write(train_X[count] + " " + train_y[count] + "\n")

f.close()

count = 0

f = open('testing.txt', 'w')

for count in range(len(validate_X)):
    f.write(validate_X[count] + " " + validate_y[count] + "\n")

f.close()
