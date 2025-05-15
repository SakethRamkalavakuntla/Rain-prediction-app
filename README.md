# 🌧️ Rainfall Prediction Flask App & AWS Deployment

A Flask-based web application that predicts whether it will rain tomorrow using a machine learning model trained on historical weather data.

---

## 📌 Overview

This project brings together machine learning, web development, and cloud deployment to deliver a seamless rainfall prediction tool. The backend runs on a robust **XGBoost** model, integrated into a lightweight **Flask** server that delivers predictions through a clean, intuitive user interface.

The app is deployed on a live **AWS EC2 Ubuntu instance**, providing real-time inference capabilities. Special care was taken to configure networking, ports, security groups, and environment setup on EC2 to make the app publicly accessible and secure.

---

## 🚀 Features

- Predicts rainfall likelihood based on user input  
- Trained using **XGBoost** for high accuracy  
- Flask app with custom routing and template rendering  
- Simple and responsive frontend with Jinja-powered HTML  
- Hosted and served from an **AWS EC2 instance**  
- Dynamic result views for rainy and sunny predictions  

---

## 🧠 Machine Learning Model

We began with **Exploratory Data Analysis (EDA)** to uncover insights and clean the dataset for modeling. This was followed by **feature engineering** to enhance model input quality and improve performance.

A variety of machine learning models were tested during experimentation. Ultimately, **XGBoost** was selected due to its superior accuracy and consistency. The final model was serialized using `pickle` and integrated into the Flask application for real-time predictions.

Model performance was validated through accuracy metrics and confusion matrix evaluations.

---

## 🌐 Flask App & AWS Deployment

The heart of the project lies in the **Flask web application**, which handles:

- Displaying a user-friendly HTML form for inputs  
- Capturing and preprocessing form data  
- Making predictions using the trained model  
- Dynamically rendering result pages based on the prediction outcome  

### ✅ Deployed on AWS EC2

Deployment steps included:

- Launching an Ubuntu-based EC2 instance  
- Installing Python, virtual environment, Flask, and required packages  
- Uploading project files using Git/GitHub  
- Running the app using `flask run --host=0.0.0.0` to expose it externally  
- Configuring EC2 **security group inbound rules** to allow traffic on the app’s port (e.g., 5000 or 5001)  

This setup ensures scalable and secure cloud deployment for real-time inference.

---

## 🧰 Tech Stack

| Layer       | Tools/Tech                          |
|-------------|-------------------------------------|
| Language     | Python 3.10                         |
| ML Model     | XGBoost                             |
| Framework    | Flask                               |
| Hosting      | AWS EC2 (Ubuntu)                    |
| Frontend     | HTML, CSS (Jinja templating)        |
| Deployment   | Git, GitHub                         |

---

## 🖼️ Web App Screenshots

> You can find the screenshots inside the `images/` folder of the repository:

- [Input Form Page](images/index.png)  
- [Rainy Result Page](images/rain.png)  
- [Sunny Result Page](images/no_rain.png)  
