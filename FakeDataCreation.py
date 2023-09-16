import pandas as pd
import random

# Create an empty DataFrame
data = pd.DataFrame(columns=[
    'apartmentId',
    'location',
    'price',
    'qualityOfEducation',
    'age',
    'typeOfCommunity',
    'careAfrican',
    'careAsian',
    'careWhite',
    'careMexican',
    'careOther',
    'careNA',
    'laundryRoom',
    'Hospital',
    'Insurance',
    'Walk-able',
    'Bike-able',
    'EnergyEfficient',
    'DrinkableWaterIndex',
    'careAboutTidyNeighborhoods',
    'MunicipalTransport',
    'pastAverageOwnerExperience'
])

# Generate fake data for 1000 rows
for i in range(1, 1001):
    if i<50:
        x=random.randint(100000, 120000)
    elif i<100:
        x=random.randint(120000, 150000)
    elif i<150:
        x=random.randint(15000, 170000)
    elif i<200:
        x=random.randint(170000, 190000)
    elif i<250:
        x=random.randint(190000, 210000)
    elif i<300:
        x=random.randint(210000, 240000)
    elif i<350:
        x=random.randint(240000, 270000)
    elif i<400:
        x=random.randint(270000, 290000)
    elif i<450:
        x=random.randint(290000, 330000)
    elif i<500:
        x=random.randint(330000, 360000)
    elif i<550:
        x=random.randint(360000, 420000)
    elif i<600:
        x=random.randint(420000, 500000)
    elif i<750:
        x=random.randint(500000, 660000)
    elif i<800:
        x=random.randint(660000, 720000)
    elif i<950:
        x=random.randint(720000, 810000)
    elif i<1001:
        x=random.randint(810000, 1000000)

    new_row = {
        'apartmentId': f'{i:04}',
        'location': f'{(random.randint(0, 99999)):05}',
        'price': x,
        'year': random.randint(1700, 2023),
        'qualityOfEducation': random.randint(0, 10),
        'age': random.randint(18, 100),
        'typeOfCommunity': random.randint(0, 7),
        'careAfrican': random.randint(0, 1),
        'careAsian': random.randint(0, 1),
        'careWhite': random.randint(0, 1),
        'careMexican': random.randint(0, 1),
        'careOther': random.randint(0, 1),
        'careNA': random.randint(0, 1),
        'laundryRoom': random.randint(0, 1),
        'Hospital': random.randint(0, 1),
        'Insurance': random.randint(0, 1),
        'Walk-able': random.randint(0, 5),
        'Bike-able': random.randint(0, 5),
        'EnergyEfficient': random.randint(0, 10),
        'DrinkableWaterIndex': random.randint(0, 5),
        'careAboutTidyNeighborhoods': random.randint(0, 1),
        'MunicipalTransport': random.randint(0, 1),
        'pastAverageOwnerExperience': random.randint(0, 100),
    }
    data = pd.concat([data, pd.DataFrame(new_row, index=[0])], ignore_index=True)

# Save the DataFrame to a CSV file (optional)
data.to_csv('apartment_data.csv', index=False)

# Display the DataFrame
print(data)
