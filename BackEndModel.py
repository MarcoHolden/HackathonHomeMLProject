#This needs to give the 10 most likely appartments
#Right now it gives purchase

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error, r2_score


apartment_data = pd.read_csv('apartment_data.csv')
X = apartment_data[['location', 'price', 'year', 'qualityOfEducation', 'age', 'typeOfCommunity', 'careAfrican', 'careAsian', 'careWhite', 'careOther', 'careMexican', 'careNA', 'laundryRoom','Hospital','Insurance','Walk-able','Bike-able','EnergyEfficient','DrinkableWaterIndex', 'careAboutTidyNeighborhoods', 'MunicipalTransport','pastAverageOwnerExperience']]
y = apartment_data['apartmentId']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

p = input("Are you ready for your prediction? ")

# Predict the apartment IDs for new data
# Replace 'new_data' with the features of the new data you want to predict
new_data = pd.DataFrame({
    'location': [23476],
    'price': [395000],
    'year': [2000],
    'qualityOfEducation': [5],
    'age': [33],
    'typeOfCommunity': [4],
    'careAfrican': [0],
    'careAsian': [1],
    'careWhite': [1],
    'careOther': [0],
    'careMexican': [0],
    'careNA': [0],
    'laundryRoom': [0],
    'Hospital': [1],
    'Insurance': [1],
    'Walk-able': [1],
    'Bike-able': [1],
    'EnergyEfficient': [2],
    'DrinkableWaterIndex': [3],
    'careAboutTidyNeighborhoods': [0],
    'MunicipalTransport': [0],
    'pastAverageOwnerExperience': [4]
})
# Predict apartment IDs for the new data
predicted_apartment_ids = model.predict(new_data)
print("You may love Apartment", round(predicted_apartment_ids[0]))
