# 🌧️ Rainfall Prediction Web App

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

Multiple machine learning models were evaluated throughout the process. Ultimately, **XGBoost** was selected for its superior accuracy and reliability. The final model was serialized using `pickle` and embedded into the Flask application.

Performance was validated using accuracy scores and a confusion matrix.

---

## 🌐 Flask App & AWS Deployment

The core of this project is the **Flask web application**, designed with modular, readable code and clear routing logic. It serves a user-friendly HTML form, captures input data, makes predictions using the trained ML model, and dynamically renders result pages.

Deployment to **AWS EC2** involved the following steps:

- Launching and configuring a Ubuntu EC2 instance
- Installing Python, virtualenv, Flask, and dependencies
- Transferring project files via Git
- Running the Flask app with `--host=0.0.0.0` to expose it to the web
- Updating EC2 security groups to allow traffic on the desired port (e.g., 5000 or 5001)
- Ensuring reliable public access without exposing sensitive IP information

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

### 📋 Input Page  
![Input Form](images/form_page.png)

### 🌧️ Rain Prediction  
![Rain Result](images/result_rain.png)

### ☀️ Sunny Prediction  
![Sunny Result](images/result_sunny.png)
