from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load model
model = pickle.load(open("rain_XGBnew_model.pkl", "rb"))

app = Flask(__name__, template_folder="template")

# Location mapping
location_map = {
    'Adelaide': 0, 'Albany': 1, 'Albury': 2, 'AliceSprings': 3, 'BadgerysCreek': 4, 'Ballarat': 5,
    'Bendigo': 6, 'Brisbane': 7, 'Cairns': 8, 'Canberra': 9, 'Cobar': 10, 'CoffsHarbour': 11,
    'Dartmoor': 12, 'Darwin': 13, 'GoldCoast': 14, 'Hobart': 15, 'Katherine': 16, 'Launceston': 17,
    'Melbourne': 18, 'MelbourneAirport': 19, 'Mildura': 20, 'Moree': 21, 'MountGinini': 22,
    'MountGambier': 23, 'Newcastle': 24, 'Nhil': 25, 'NorahHead': 26, 'NorfolkIsland': 27,
    'Nuriootpa': 28, 'PearceRAAF': 29, 'Penrith': 30, 'Perth': 31, 'PerthAirport': 32,
    'Portland': 33, 'Richmond': 34, 'Sale': 35, 'SalmonGums': 36, 'Sydney': 37,
    'SydneyAirport': 38, 'Tuggeranong': 39, 'Townsville': 40, 'Uluru': 41, 'WaggaWagga': 42,
    'Walpole': 43, 'Watsonia': 44, 'Williamtown': 45, 'Witchcliffe': 46, 'Wollongong': 47,
    'Woomera': 48
}

# Wind direction mapping 
wind_dir_map = {
    'N': 0, 'NNE': 1, 'NE': 2, 'ENE': 3, 'E': 4, 'ESE': 5, 'SE': 6, 'SSE': 7,
    'S': 8, 'SSW': 9, 'SW': 10, 'WSW': 11, 'W': 12, 'WNW': 13, 'NW': 14, 'NNW': 15
}

# RainToday mapping
rain_today_map = {'No': 0, 'Yes': 1}

@app.route("/", methods=['GET'])
def home():
    return render_template(
        "index.html",
        locations=location_map.keys(),
        wind_dirs=wind_dir_map.keys()
    )

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":
        try:
            # Extract and process form values
            date = request.form['date']
            day = float(pd.to_datetime(date).day)
            month = float(pd.to_datetime(date).month)

            # Continuous variables
            minTemp = float(request.form['mintemp'])
            maxTemp = float(request.form['maxtemp'])
            rainfall = float(request.form['rainfall'])
            evaporation = float(request.form['evaporation'])
            sunshine = float(request.form['sunshine'])
            windGustSpeed = float(request.form['windgustspeed'])
            windSpeed9am = float(request.form['windspeed9am'])
            windSpeed3pm = float(request.form['windspeed3pm'])
            humidity9am = float(request.form['humidity9am'])
            humidity3pm = float(request.form['humidity3pm'])
            pressure9am = float(request.form['pressure9am'])
            pressure3pm = float(request.form['pressure3pm'])
            cloud9am = float(request.form['cloud9am'])
            cloud3pm = float(request.form['cloud3pm'])
            temp9am = float(request.form['temp9am'])
            temp3pm = float(request.form['temp3pm'])

            # Categorical variables
            location = location_map.get(request.form['location'], -1)
            windGustDir = wind_dir_map.get(request.form['windgustdir'], -1)
            windDir9am = wind_dir_map.get(request.form['winddir9am'], -1)
            windDir3pm = wind_dir_map.get(request.form['winddir3pm'], -1)
            rainToday = rain_today_map.get(request.form['raintoday'], -1)

            # Model input
            input_lst = [[
                location, minTemp, maxTemp, rainfall, evaporation, sunshine,
                windGustDir, windGustSpeed, windDir9am, windDir3pm, windSpeed9am,
                windSpeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm,
                cloud9am, cloud3pm, temp9am, temp3pm, rainToday, month, day
            ]]

            # Predict
            pred = model.predict(input_lst)[0]

            if pred == 0:
                return render_template("after_sunny3.html")
            else:
                return render_template("after_rainy3.html")

        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
