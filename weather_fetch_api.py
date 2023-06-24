import requests
import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import math
import os

def fetch_data_from_api(api_key, location):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={start_date}&end_dt={end_date}"
    response = requests.get(url)
    data = response.json()
    return data

def convert_to_csv(data, filename):
    fields = ['date', 'temperature', 'windspeed']
    
    # Get the directory path where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Concatenate the script directory with the provided filename
    file_path = os.path.join(script_directory, filename)
    print(file_path)

    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for entry in data['forecast']['forecastday']:
            date = entry['date']
            formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
            temperature = entry['day']['avgtemp_c']
            windspeed = entry['day']['maxwind_kph']

            writer.writerow({'date': formatted_date, 'temperature': temperature, 'windspeed': windspeed})

    return file_path

def handle_generate_csv():
    api_key = '1228be45880d463b8f853053231606'
    location = city_dropdown.get()
    api_data = fetch_data_from_api(api_key, location)
    filename = 'weather_data.csv'
    file_path = convert_to_csv(api_data, filename)
    result_label.config(text=f"Data saved successfully to {file_path}.")
    

    api_key = '1228be45880d463b8f853053231606'
    location = city_dropdown.get()
    api_data = fetch_data_from_api(api_key, location)
    filename = 'weather_data.csv'
    convert_to_csv(api_data, filename)
    result_label.config(text=f"Data saved successfully to {filename}.")
    
def locadata():
    loca_data=city_dropdown.get()
    loca_label.config(text=f"The City You Have Selected Is {loca_data}")
    #print(loca_data)
    
    
    
def handle_exit():
    window.destroy()
    


cities = ['Chennai', 'Mumbai', 'Delhi', 'Kolkata', 'Bengaluru', 'Hyderabad', 'Ahmedabad', 'Pune', 'Jaipur']

# Create Tkinter window
window = tk.Tk()
window.title("Weather Data")
window.configure(bg="light blue")

# Calculate the position to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 700
window_height = 500
x_position = math.ceil((screen_width - window_width) / 2)
y_position = math.ceil((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Main label
main_label = ttk.Label(window, text="Weather Prediction Application", font=("Arial", 30, "bold"), background="light blue")
main_label.pack(pady=20)

# City dropdown label
city_label = ttk.Label(window, text="Select City:", font=("Arial", 20, "bold"), background="light blue")
city_label.pack()

# City dropdown menu
city_dropdown = ttk.Combobox(window, values=cities)
city_dropdown.pack(pady=10)

# Create a custom style for buttons
button_style = ttk.Style()
button_style.configure('Custom.TButton', font=("Arial", 14), background="light blue", relief="groove",
                       activebackground="red", activeforeground="red")

# Generate CSV button
generate_button = ttk.Button(window, text="Generate CSV", command=lambda:(handle_generate_csv(),locadata()), 
                             style='Custom.TButton', width=20)
generate_button.pack(pady=20)

loca_label=ttk.Label(window,text="", font=("Arial", 14,"bold"), background="light blue")
loca_label.pack(pady=10)

exit_button = ttk.Button(window, text="Exit", command=handle_exit, style='Custom.TButton', width=10)
exit_button.pack(pady=5)

# Result label
result_label = ttk.Label(window, text="", font=("Arial", 14), background="light blue")
result_label.pack()

window.mainloop()




