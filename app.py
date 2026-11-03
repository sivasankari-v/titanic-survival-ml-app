import pandas as pd

# Load dataset
data = pd.read_csv('titanic.csv')

# Simple prediction rule: female = survived
data['Prediction'] = data['Sex'].apply(lambda x: 1 if x == 'female' else 0)

# Calculate accuracy
correct = (data['Survived'] == data['Prediction']).sum()
total = len(data)
accuracy = (correct / total) * 100

print(f"Total passengers: {total}")
print(f"Correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
print("Project executed successfully!")