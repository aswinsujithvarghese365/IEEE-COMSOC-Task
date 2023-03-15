import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

df = pd.read_csv("winequality-red.csv")
print(df.head(20))
#Dataset information
print(df.info())
print()
# Converting the column values to array
fixed_acidity = np.array(df["fixed acidity"])
volatile_acidity = np.array(df["volatile acidity"])
density = np.array(df["density"])
pH = np.array(df["pH"])
sulphates = np.array(df["sulphates"])
alcohol = np.array(df["alcohol"])
quality = np.array(df["quality"])

# 10 NumPy module functions

# Size of the dataset
dataset_size = np.size(fixed_acidity)+1
print("Size of the dataset is",dataset_size)
print()
print("Sorted density = ", np.sort(density))
# Rounding to 5 decimal places
print("Minimum density = ", np.min(density).round(5))
print("Maximum density = ",np.max(density).round(5))
print("Average alcohol content = ",np.mean(alcohol).round(5))
print("The quality of Red Wine will be mostly",st.mode(quality))
print("Average pH value = ",np.mean(pH).round(5))
# Finding the average using sum() function
print("Average sulphate rate = ",(np.sum(sulphates)/dataset_size).round(5))
print("Average of fixed acidity of red wine is",np.mean(fixed_acidity).round(5))

#Graphs
values = np.array(df["alcohol"]).tolist()
alc_cont=[8,9,10,11,12,13,14]
plt.hist(values,bins=alc_cont,color="magenta",edgecolor="black",histtype="bar",rwidth=0.6)
plt.title("Histogram of Alcohol content")
plt.xlabel("Alcohol Content ->")
plt.ylabel("No. of Red Wines ->")
plt.show()

plt.boxplot(alcohol)
plt.title("Boxplot of Alcohol content")
plt.show()

plt.boxplot(pH)
plt.title("Boxplot of pH value")
plt.show()

plt.scatter(np.arange(0,1599,1), fixed_acidity, c ="pink",edgecolors="black")
plt.title("Scatter plot of Fixed Acidity")
plt.ylabel("Fixed Acidity ->")
plt.show()
