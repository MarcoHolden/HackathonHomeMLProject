"""This code will be for connecting information to FrontEnd"""
import pandas as pd

apartment_data = pd.read_csv('apartment_data.csv')

def recomender(predicted_apartment_ids):
     x=int(predicted_apartment_ids[0])

     lst=[apartment_data['apartmentId'][x-1],
          apartment_data['location'][x-1],
          apartment_data['price'][x-1],
          apartment_data['year'][x-1],
          apartment_data['qualityOfEducation'][x-1],
          apartment_data['age'][x-1],
          apartment_data['typeOfCommunity'][x-1],
          apartment_data['laundryRoom'][x-1],
          apartment_data['Hospital'][x-1],
          apartment_data['Walk-able'][x-1],
          apartment_data['Bike-able'][x-1],
          apartment_data['EnergyEfficient'][x-1],
          apartment_data['DrinkableWaterIndex'][x-1],
          apartment_data['careAboutTidyNeighborhoods'][x-1],
          apartment_data['MunicipalTransport'][x-1],
     ]
     return lst
     #List 2 is the respective catagory to number

     # lst2=[f"Home Number: {apartment_data['apartmentId'][x-1]}",
     #      f"Area code: {apartment_data['location'][x-1]}",
     #      f"Price: {apartment_data['price'][x-1]}",
     #      f"Year Built: {int(apartment_data['year'][x-1])}",
     #      f"Rating of Education: {apartment_data['qualityOfEducation'][x-1]}",
     #      f"Type of Community: {apartment_data['typeOfCommunity'][x-1]}",
     #      f"LaundryRoom(1:Has, 0:Doesn't Have): {apartment_data['laundryRoom'][x-1]}",
     #      f"Hospital within 20minutes(1:Has, 0:Doesn't Have): {apartment_data['Hospital'][x-1]}",
     #      f"Walkability Score(0-5): {apartment_data['Walk-able'][x-1]}",
     #      f"Bikeability Score(0-5): {apartment_data['Bike-able'][x-1]}",
     #      f"Energy Efficient Ranking(0-10): {apartment_data['EnergyEfficient'][x-1]}",
     #      f"Water drinkability ratings(0-5): {apartment_data['DrinkableWaterIndex'][x-1]}",
     #      f"Clean Community: {apartment_data['careAboutTidyNeighborhoods'][x-1]}",
     #      f"Local Transportation options: {apartment_data['MunicipalTransport'][x-1]}",
     #      f"Ranking of past owners: {apartment_data['pastAverageOwnerExperience'][x-1]}"
     # ]
     # print("You may love Apartment", int(predicted_apartment_ids[0]))
     # print()
     # print("Here is the info:", lst2 )

