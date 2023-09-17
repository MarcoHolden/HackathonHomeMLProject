from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error, r2_score
from BackEndRecommendations import recomender
#This initializes what we need for ML
apartment_data = pd.read_csv('apartment_data.csv')
X = apartment_data[['location', 'price', 'year', 'qualityOfEducation', 'age', 'typeOfCommunity', 'laundryRoom','Hospital','Walk-able','Bike-able','EnergyEfficient','DrinkableWaterIndex', 'careAboutTidyNeighborhoods', 'MunicipalTransport']]
y = apartment_data['apartmentId']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
###

app = Flask("__name__")

def filesToList(result):
    stringResult = str(result)
    #removes unnecessary text in begining and end
    stringResult = stringResult[20:-3]
    print("StringResult after slicing:", stringResult)
    lstResult = stringResult.split("),")
    print("lstResult:", lstResult)
    for i in range(len(lstResult)):
        x = lstResult[i].replace("(\'state\'", "")
        x = x.replace("(\'city\'", "")
        x = x.replace("(\'state\'", "")
        x = x.replace("(\'neighborhood\'", "")
        x = x.replace("(\'zip-code\'", "")
        x = x.replace("(\'price_range\'", "")
        x = x.replace("(\'year\'", "")
        x = x.replace("(\'age\'", "")
        x = x.replace("(\'year\'", "")
        x = x.replace("(\'energy-efficiency\'", "")
        x = x.replace("(\'public-transport\'", "")
        x = x.replace("(\'walk-friendly\'", "")
        x = x.replace("(\'community\'", "")
        x = x.replace("(\'laundry-room\'", "")
        x = x.replace("(\'hospital\'", "")
        x = x.replace("(\'bike-friendly\'", "")
        x = x.replace("(\'water-drinkability\'", "")
        x = x.replace("(\'tidy-neighborhood\'", "")
        x = x.replace("(\'rating1\'", "")
        x = x.replace("(\'rating2\'", "")
        x = x.replace(", \'", "")
        x = x.replace("\'", "")
        x = x.replace(" ", "")
        lstResult[i] = x
    print("lstResult before removal:", lstResult)
    lstResult = lstResult[3:len(lstResult)]
    print("lstResult after cutting 3 values")
    print("lstResult after removal:", lstResult)
    return lstResult

def MLDataConversion(lst):
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = lst
    new_data = pd.DataFrame({
        'location': [int(x1)],
        'price': [int(x2)],
        'year': [int(x3)],
        'qualityOfEducation': [int(x14)],
        'age': [int(x4)],
        'typeOfCommunity': [int(x13)],
        'laundryRoom': [int(x6)],
        'Hospital': [int(x7)],
        'Walk-able': [int(x12)],
        'Bike-able': [int(x8)],
        'EnergyEfficient': [int(x5)],
        'DrinkableWaterIndex': [int(x9)],
        'careAboutTidyNeighborhoods': [int(x10)],
        'MunicipalTransport': [int(x11)],
    })
    return new_data
     
#Landing page
@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/infoForm")
def form():
        return render_template("main.html")

@app.route("/resultForm", methods = ["POST", "GET"])
def resultForm():
        if request.method == "POST":
            results = request.form
            print(results)
            print("After converting")
            lst=filesToList(results)
            dataForML = MLDataConversion(lst)
            predicted_apartment_ids = model.predict(dataForML)
            HomeQualities=recomender(predicted_apartment_ids)
            print("list", HomeQualities, "type of variable:", type(HomeQualities))
            price = HomeQualities[2]
            price = str(price)[::-1]
            price = price[0:3] + "," + price [3:6]
            price = price[::-1]
            print("price:", price)
            zipcode = HomeQualities[1]
            year_built = HomeQualities[3]
            rating = HomeQualities[4]
            print("This apartment is good :", int(predicted_apartment_ids[0]))
            return render_template("result_page.html", price = price, zip_code = zipcode, 
                                   year_built = year_built, rating = rating)
        else:
              "error in result form"

if __name__ == "__main__":
    #app.run(host = '192.168.8.180', port = 5051, debug = True)
    app.run(debug = True)