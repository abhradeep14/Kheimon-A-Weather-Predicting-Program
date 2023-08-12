# Kheimon: A Weather Prediction Program

Kheimon is a Python-based Weather Prediction App that employs the Linear Regression Algorithm to predict weather with an accuracy nearest to 1. This relatively simpler machine learning algorithm utilizes linear relationships to extrapolate further data. The program integrates a dynamic Weather API to gather recent weather data (default: 15 days) and stores it in a CSV (Comma-Separated Value) file format. This data is then processed by the Python program for graphical display, facilitating weather forecasting for N days. Additionally, Kheimon has the capability to function across 9 major Indian cities.

## Features

- **Simple Python GUI:** The program features a user-friendly interface based on the Tkinter library.
  
- **Streamlined API Integration:** Kheimon employs an API-based approach to dynamically collect weather data from the past 15 days, dependent on the current date. This data is saved as a CSV file on the local device.
  
- **Data Retrieval:** Historical weather data for linear regression analysis is retrieved from WeatherApi.com, offering free access for simplified data parsing.
  
- **Multi-City Compatibility:** The model currently functions successfully in 9 Indian cities, providing accurate weather data.
  
- **Data Manipulation and Visualization:** Kheimon leverages crucial libraries like Numpy, Pandas, and Matplotlib for dataset manipulation and data visualization. It employs scatter plots to visually represent temperature and windspeed data, the core parameters for the linear regression model's prediction.
  
- **Temperature and Windspeed Prediction:** Utilizing the linear regression model and Weather-API data, the program predicts temperature and windspeed. The outcomes are presented through tables and graphical representations.
  
## Setup

To ensure proper functionality, Kheimon requires Python 3.11.2. Follow these steps to set up the program:

1. Navigate to the project directory using the command line:
   
   ```bash
   cd Kheimon
2. Install dependencies by running:
    ```python
    python dependencies.py


3. Launch the program by executing:
   ```python
   python complete_project.py

## Tkinter Windows:

![Python ScreenShot1](https://github.com/abhradeep14/Kheimon-A-Weather-Predicting-Program/assets/77497523/70438fea-0ccd-42aa-bb9a-07afcdcf92bd)


**Cities Currently Available For Analysis:**

![Python Screenshot 3](https://github.com/abhradeep14/Kheimon-A-Weather-Predicting-Program/assets/77497523/3b349541-18b6-4a09-a6eb-3dc392e7fb22)




![Python Screenshot 2](https://github.com/abhradeep14/Kheimon-A-Weather-Predicting-Program/assets/77497523/be0472be-960e-4664-9a52-23df3d6c7703)




![Python Screenshot 4](https://github.com/abhradeep14/Kheimon-A-Weather-Predicting-Program/assets/77497523/13017b2e-bf64-40cc-94a4-c3545f89307d)





