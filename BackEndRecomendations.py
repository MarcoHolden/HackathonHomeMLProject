"""This code will be for connecting information to FrontEnd"""
from BackEndModel import predicted_apartment_ids, apartment_data
x=int(predicted_apartment_ids[0])

#List one is raw numbers

lst=[apartment_data['apartmentId'][x-1],
     apartment_data['location'][x-1],
     apartment_data['price'][x-1],
     apartment_data['year'][x-1],
     apartment_data['qualityOfEducation'][x-1],
     apartment_data['age'][x-1],
     apartment_data['typeOfCommunity'][x-1],
     apartment_data['careAfrican'][x-1],
     apartment_data['careMexican'][x-1],
     apartment_data['careWhite'][x-1],
     apartment_data['careOther'][x-1],
     apartment_data['careNA'][x-1],
     apartment_data['laundryRoom'][x-1],
     apartment_data['Hospital'][x-1],
     apartment_data['Insurance'][x-1],
     apartment_data['Walk-able'][x-1],
     apartment_data['Bike-able'][x-1],
     apartment_data['EnergyEfficient'][x-1],
     apartment_data['DrinkableWaterIndex'][x-1],
     apartment_data['careAboutTidyNeighborhoods'][x-1],
     apartment_data['MunicipalTransport'][x-1],
     apartment_data['pastAverageOwnerExperience'][x-1]
]

#List 2 is the respective catagory to number

lst2=[f"Home Number: {apartment_data['apartmentId'][x-1]}",
     f"Area code: {apartment_data['location'][x-1]}",
     f"Price: {apartment_data['price'][x-1]}",
     f"Year Built: {int(apartment_data['year'][x-1])}",
     f"Rating of Education: {apartment_data['qualityOfEducation'][x-1]}",
     f"Type of Community: {apartment_data['typeOfCommunity'][x-1]}",
     f"African demographic > 10% (1:Y, 0:N): {apartment_data['careAfrican'][x-1]}",
     f"Hispanic demographic > 10% (1:Y, 0:N): {apartment_data['careMexican'][x-1]}",
     f"European(White) demographic > 10% (1:Y, 0:N): {apartment_data['careWhite'][x-1]}",
     f"LaundryRoom(1:Has, 0:Doesn't Have): {apartment_data['laundryRoom'][x-1]}",
     f"Hospital within 20minutes(1:Has, 0:Doesn't Have): {apartment_data['Hospital'][x-1]}",
     f"Insurance covers 1st year(1:Does, 0:Doesn't): {apartment_data['Insurance'][x-1]}",
     f"Walkability Score(0-5): {apartment_data['Walk-able'][x-1]}",
     f"Bikeability Score(0-5): {apartment_data['Bike-able'][x-1]}",
     f"Energy Efficient Ranking(0-10): {apartment_data['EnergyEfficient'][x-1]}",
     f"Water drinkability ratings(0-5): {apartment_data['DrinkableWaterIndex'][x-1]}",
     f"Clean Community: {apartment_data['careAboutTidyNeighborhoods'][x-1]}",
     f"Local Transportation options: {apartment_data['MunicipalTransport'][x-1]}",
     f"Ranking of past owners: {apartment_data['pastAverageOwnerExperience'][x-1]}"
]
print("You may love Apartment", int(predicted_apartment_ids[0]))
print()
print("Here is the info:", lst2 )

