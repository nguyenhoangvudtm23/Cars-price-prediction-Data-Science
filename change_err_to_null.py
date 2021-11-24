import pandas as pd
import numpy as np
import matplotlib.pyplot as ply
import seaborn as sns

# emissionsCO2, engineCapacity, fuelCapacity, fuelConsumption, fuelType, height

name_in = input("Input csv name:")
name_out = input("Output csv name:")

data = pd.read_csv(name_in)

# emissionsCO2
print("EmissionCO2 null data before: {}".format(data["emissionsCO2"].isnull().sum()))
error_data = dict()
for value in data["emissionsCO2"]:
    number = value.split(" ")[0]
    try:
        int(number)
    except:
        if number not in error_data:
            error_data[number] = 1
        else:
            error_data[number] += 1
print("EmissionCO2 error data: {}".format(error_data))
# Erase g/km
data["emissionsCO2"] = pd.Series(map(lambda x: x.split(" ")[0],data["emissionsCO2"].to_list()))
# Change error data to nan
for err in error_data.keys():
    data["emissionsCO2"] = data["emissionsCO2"].replace(err, np.nan)
print("EmissionCO2 null data after: {}".format(data["emissionsCO2"].isnull().sum()))

# engineCapacity
print("engineCapacity null data before: {}".format(data["engineCapacity"].isnull().sum()))
error_data = dict()
for value in data["engineCapacity"]:
    try:
        number = value.split(" ")[0]
    except:
        continue
    try:
        int(number)
    except:
        if number not in error_data:
            error_data[number] = 1
        else:
            error_data[number] += 1
print("engineCapacity error data: {}".format(error_data))
for err in error_data.keys():
    data["engineCapacity"] = data["engineCapacity"].replace(err, np.nan)
print("engineCapacity null data after: {}".format(data["engineCapacity"].isnull().sum()))
# Remove cc
repair = []
for value in data["engineCapacity"]:
    try:
        number = value.split(" ")[0]
    except:
        repair.append(value)
        continue
    repair.append(number)
data["engineCapacity"] = pd.Series(repair)

# fuelCapacity
print("fuelCapacity null data before: {}".format(data["fuelCapacity"].isnull().sum()))
error_data = dict()
for value in data["fuelCapacity"]:
    try:
        number = value.split(" ")[0]
    except:
        continue
    try:
        int(number)
    except:
        if value not in error_data:
            error_data[value] = 1
        else:
            error_data[value] += 1
print("fuelCapacity error data: {}".format(error_data))
for err in error_data.keys():
    data["fuelCapacity"] = data["fuelCapacity"].replace(err, np.nan)
print("fuelCapacity null data after: {}".format(data["fuelCapacity"].isnull().sum()))
# Delete l
repair = []
for value in data["fuelCapacity"]:
    try:
        number = value.split(" ")[0]
    except:
        repair.append(value)
        continue
    repair.append(number)
data["fuelCapacity"] = pd.Series(repair)

# fuelConsumption
print("fuelConsumption null data before: {}".format(data["fuelConsumption"].isnull().sum()))
# Delete the unit
repair = []
for value in data["fuelConsumption"]:
    try:
        number = value.split(" ")[0]
    except:
        repair.append(value)
        continue
    repair.append(number)
data["fuelConsumption"] = pd.Series(repair)
# Create float number
repair = []
for value in data["fuelConsumption"]:
    try:
        number = int(value.split(",")[0]) + (int(value.split(",")[1])/10)
    except:
        repair.append(value)
        continue
    repair.append(number)
data["fuelConsumption"] = pd.Series(repair)
# Find some error in fuelConsumption
error_data = dict()
for value in data["fuelConsumption"]:
    try:
        number = value.split(" ")[0]
    except:
        continue
    try:
        int(number)
    except:
        if number not in error_data:
            error_data[number] = 1
        else:
            error_data[number] += 1
print("fuelConsumption error data: {}".format(error_data))
for err in error_data.keys():
    data["fuelConsumption"] = data["fuelConsumption"].replace(err, np.nan)
print("fuelConsumption null data after: {}".format(data["fuelConsumption"].isnull().sum()))

# fuelType
print("fuelType null data before: {}".format(data["fuelType"].isnull().sum()))
print("Nothing to be change")
# height
print("height null data before: {}".format(data["height"].isnull().sum()))
# Find some error in height
d = dict()
for number in data['height']:
    try:
        int(number)
    except:
        if number not in d:
            d[number] = 1
        else:
            d[number] += 1
print("fuelConsumption error data: {}".format(d))
for err in d.keys():
    data["height"] = data["height"].replace(err, np.nan)
print("height null data after: {}".format(data["height"].isnull().sum()))

# Save
data.to_csv(name_out)
