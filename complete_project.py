import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import dependencies  
import weather_fetch_api



# Read the data from the CSV file
data = pd.read_csv("weather_data.csv")
date = data['date']
meantemp = data['temperature']
windspeed = data['windspeed']

meantemp_norm = (meantemp - meantemp.min()) / (meantemp.max() - meantemp.min())
windspeed_norm = (windspeed - windspeed.min()) / (windspeed.max() - windspeed.min())

# Create a Tkinter window
root = tk.Tk()
root.title("Graph Display")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a frame for the graphs
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create the first figure and scatter plot
fig1 = Figure(figsize=(screen_width / 200, screen_height / 200), dpi=100)
ax1 = fig1.add_subplot(111)
ax1.plot(date, meantemp, color='red', alpha=0.6)
ax1.scatter(date, meantemp, color='red', s=meantemp_norm * 150)
ax1.set_xlabel('Date')
ax1.set_ylabel('Mean Temperature')
ax1.grid(alpha=0.6)
num_ticks = 16  # Number of desired ticks on the x-axis
tick_indices = np.linspace(0, len(date) - 1, num_ticks, dtype=int)
tick_labels = date[tick_indices]
ax1.set_xticks(tick_indices)
ax1.set_xticklabels(tick_labels, rotation=26)

# Create a FigureCanvasTkAgg for the first graph
canvas1 = FigureCanvasTkAgg(fig1, master=frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10)

# Create the second figure and scatter plot
fig2 = Figure(figsize=(screen_width / 200, screen_height / 200), dpi=100)
ax2 = fig2.add_subplot(111)
ax2.plot(date, windspeed, color='blue', alpha=0.5)
ax2.scatter(date, windspeed, color='blue', s=windspeed_norm * 100)
ax2.set_xlabel('Date')
ax2.set_ylabel('Wind Speed')
ax2.grid(alpha=0.6)
ax2.set_xticks(tick_indices)
ax2.set_xticklabels(tick_labels, rotation=26)

# Create a FigureCanvasTkAgg for the second graph
canvas2 = FigureCanvasTkAgg(fig2, master=frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10)

def start_prediction(event=None):
    n_days = int(days_entry.get())
    predict_weather(n_days)



def predict_weather():
    # Perform weather prediction using scikit-learn
    date_numeric = pd.to_datetime(data['date'], format='%d/%m/%Y').apply(lambda x: int(x.timestamp()))

    # Fit the linear regression model for temperature
    regression_model = LinearRegression()
    regression_model.fit(date_numeric.values.reshape(-1, 1), meantemp)

    # Fit the linear regression model for windspeed
    regression_model_windspeed = LinearRegression()
    regression_model_windspeed.fit(date_numeric.values.reshape(-1, 1), windspeed)

    # Get the number of days from the entry widget
    n_days = int(days_entry.get())

    # Create a new window for displaying predictions
    window = tk.Toplevel(root)
    window.title("Weather Predictions")
    window.attributes('-fullscreen', True)
    window.bind('<Escape>', lambda event: window.attributes('-fullscreen', False))
    root.bind('<Escape>',lambda event: window.attributes('-fullscreen',False))

    # Calculate the window size and position for center alignment
    window_width = int(screen_width * 0.6)
    window_height = int(screen_height * 0.6)
    window_x = int((screen_width - window_width) / 2)
    window_y = int((screen_height - window_height) / 2)

    # Set the window size and position
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Create a frame for the predictions
    prediction_frame = tk.Frame(window)
    prediction_frame.pack(pady=10)

    # Create the third figure and scatter plot for predicted temperature
    fig3 = Figure(figsize=(window_width / 100, window_height / 100), dpi=100)
    ax3 = fig3.add_subplot(111)
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Mean Temperature')
    ax3.grid(alpha=0.6)
    ax3.set_xticks(tick_indices)
    ax3.set_xticklabels(tick_labels, rotation=30)
    ax3.xaxis.set_tick_params(labelsize=8)

    # Create the fourth figure and scatter plot for predicted windspeed
    fig4 = Figure(figsize=(window_width / 100, window_height / 100), dpi=100)
    ax4 = fig4.add_subplot(111)
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Wind Speed')
    ax4.grid(alpha=0.6)
    ax4.set_xticks(tick_indices)
    ax4.set_xticklabels(tick_labels, rotation=30)
    
    # Create a label for the weather prediction
    prediction_label = tk.Label(window, text=f"The Weather Prediction for {n_days} days is:", font=("Arial", 16), pady=10)
    prediction_label.pack()
        
     # Create a frame for the exit button
    exit_frame = tk.Frame(window)
    exit_frame.pack(pady=10)

# Create an exit button to close the weather predictions window
    exit_button = ttk.Button(exit_frame, text="Exit", command=window.destroy, style='Custom.TButton')
    exit_button.pack()

# Create a frame for the predictions
    prediction_frame = tk.Frame(window)
    prediction_frame.pack(pady=10)

    last_temp = meantemp.iloc[-1]
    last_windspeed = windspeed.iloc[-1]

    predicted_dates = []
    predicted_temperatures = []
    predicted_windspeeds = []

    for i in range(n_days):
        last_date = pd.to_datetime(date.iloc[-1], format='%d/%m/%Y')
        future_date = last_date + pd.DateOffset(days=i + 1)

        # Predict the future date
        future_date_numeric = pd.Timestamp(future_date).timestamp()

        # Predict the future weather
        future_weather_temp = regression_model.predict([[future_date_numeric]])
        future_weather_windspeed = regression_model_windspeed.predict([[future_date_numeric]])

        # Append the predicted values to the lists
        predicted_dates.append(future_date)
        predicted_temperatures.append(future_weather_temp)
        predicted_windspeeds.append(future_weather_windspeed)

        # Plot the predicted temperature and windspeed
        ax3.plot([last_date, future_date], [last_temp, future_weather_temp], color='green', linestyle='-')
        ax3.scatter(future_date, future_weather_temp, color='green', marker='o')
        last_temp = future_weather_temp

        ax4.plot([last_date, future_date], [last_windspeed, future_weather_windspeed], color='maroon', linestyle='-')
        ax4.scatter(future_date, future_weather_windspeed, color='maroon', marker='o')
        last_windspeed = future_weather_windspeed

        ax3.annotate(f"{future_date.strftime('%d/%m/%Y')}\n{future_weather_temp[0]:.2f}", (future_date, future_weather_temp[0]),
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7,fontweight='bold')
        ax3.annotate(f"{future_weather_temp[0]:.2f}",(future_date, future_weather_temp[0]),textcoords="offset points", xytext=(0, 10),ha='center', fontsize=7)
        ax4.annotate(f"{future_date.strftime('%d/%m/%Y')}\n{future_weather_windspeed[0]:.2f}", (future_date, future_weather_windspeed[0]),
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7,fontweight='bold')
        

    # Create a FigureCanvasTkAgg for the third graph
        canvas3 = FigureCanvasTkAgg(fig3, master=prediction_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a FigureCanvasTkAgg for the fourth graph
        canvas4 = FigureCanvasTkAgg(fig4, master=prediction_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create a DataFrame for the predicted weather
    predicted_data = pd.DataFrame({'date': predicted_dates,
                                   'temperature': predicted_temperatures,
                                   'windspeed': predicted_windspeeds})

    # Create a treeview to display the predicted weather
    tree = ttk.Treeview(window)
    tree["columns"] = ("date", "temperature", "windspeed")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("date", anchor=tk.CENTER, width=100)
    tree.column("temperature", anchor=tk.CENTER, width=100)
    tree.column("windspeed", anchor=tk.CENTER, width=100)
    tree.heading("date", text="Date")
    tree.heading("temperature", text="Temperature(C)")
    tree.heading("windspeed", text="Wind Speed")
    tree.pack(pady=10)
    
    style = ttk.Style()
    style.theme_use("clam")  # Choose a desired theme ("clam" is just an example)
    style.configure("Treeview",
                background="white",
                foreground="black",
                fieldbackground="white")

    style.configure("Treeview.Heading",
                font=("Arial", 12, "bold"),
                background="light blue",
                foreground="black")

    style.map("Treeview",
          background=[("selected", "light blue")],
          foreground=[("selected", "black")])

    # Insert the predicted weather data into the treeview
    for _, row in predicted_data.iterrows():
     date_str = row["date"].strftime("%d/%m/%Y")
     temperature_str = f"{row['temperature'][0]:.2f}"  # Format temperature with two decimal places
     windspeed_str = f"{row['windspeed'][0]:.2f}"  # Format windspeed with two decimal places
     tree.insert("", tk.END, values=(date_str, temperature_str, windspeed_str))

    def exit_window():
        window.destroy()
        root.destroy()


# Create a frame for the input
def exit_window1():
    root.destroy()

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

days_entry = tk.Entry(input_frame)
days_entry.pack(side=tk.LEFT)
days_entry.bind('<Return>', start_prediction)

# Create a label and entry for the number of days to predict
days_label = tk.Label(input_frame, text="Enter number of days to predict:", font=("Arial", 16), background="light blue")
days_label.pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(input_frame)
button_frame.pack(side=tk.LEFT, padx=10)

button_style = ttk.Style()
# Create a button to initiate the prediction
predict_button = ttk.Button(button_frame, text="Predict Weather", command=predict_weather, style='Custom.TButton')
predict_button.pack(side=tk.LEFT,padx=5)

# Create a custom style for the button
button_style.configure('Custom.TButton', font=("Arial", 14), background="light blue", relief="raised",
                       activebackground="light gray", activeforeground="black")

exit_button = ttk.Button(button_frame, text="Exit Program", command=exit_window1, style='Custom.TButton')
exit_button.pack(side=tk.LEFT, pady=10)

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda event: root.destroy())

# Run the Tkinter event loop
root.mainloop()
