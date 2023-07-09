import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

def count_people_above_40_with_high_cholesterol(data):
    count = len(data[(data['age'] > 40) & (data['chol'] > 200)])
    return count

def calculate_percentage_above_40_with_high_cholesterol(data):
    total_above_40 = len(data[data['age'] > 40])
    above_40_high_cholesterol_sugar = len(data[(data['age'] > 40) & (data['chol'] > 200) & (data['fbs'] > 0)])
    percentage = (above_40_high_cholesterol_sugar / total_above_40) * 100
    return percentage

def create_chart_high_cholesterol_sugar_restecg(data):
    filtered_df = data[(data['chol'] > 200) & (data['fbs'] > 0) & (data['restecg'] == 2)]
    cholesterol = filtered_df['chol']
    blood_sugar = filtered_df['fbs']
    plt.scatter(cholesterol, blood_sugar, cmap='RdYlBu')
    plt.xlabel('Cholesterol')
    plt.ylabel('Blood Sugar')
    plt.title('Comparison of High Cholesterol and High Blood Sugar (restecg = 2)')
    plt.show()

# People above 40 with high cholesterol
people_above_40_high_cholesterol = count_people_above_40_with_high_cholesterol(data)
print("People above 40 with high cholesterol:", people_above_40_high_cholesterol)

# Percentage of people above 40 with high cholesterol and high blood sugar
percentage = calculate_percentage_above_40_with_high_cholesterol(data)
print("Percentage of people above 40 with high cholesterol and high blood sugar:", percentage, "%")

# Chart showing the relationship between high cholesterol, high blood sugar, and left ventricular hypertrophy
create_chart_high_cholesterol_sugar_restecg(data)
