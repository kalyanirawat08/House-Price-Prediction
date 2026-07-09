import tkinter as tk
from sklearn.linear_model import LinearRegression
import numpy as np

# -----------------------------
# Step 1: Train Model
# -----------------------------
# Features: [Area, Age, Rooms] 
X = np.array([
    [1000, 5, 2],
    [1500, 10, 3],
    [2000, 3, 4],
    [2500, 1, 4],
    [1200, 7, 2],
    [1800, 4, 3]
])

# Prices (in lakhs)
y = np.array([20, 25, 40, 55, 22, 35])

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Step 2: Prediction Function
# -----------------------------
def predict_price():
    try:
        area = float(entry_area.get())
        age = float(entry_age.get())
        rooms = int(entry_rooms.get())

        prediction = model.predict([[area, age, rooms]])

        result_label.config(
            text=f"Estimated Price: {prediction[0]:.2f} Lakhs",
            fg="green"
        )
    except:
        result_label.config(
            text="Please enter valid values!",
            fg="red"
        )

# -----------------------------
# Step 3: GUI Design
# -----------------------------
root = tk.Tk()
root.title("🏠 House Price Predictor")
root.geometry("350x300")

tk.Label(root, text="House Price Prediction", font=("Arial", 14, "bold")).pack(pady=10)

# Area
tk.Label(root, text="Area (sq ft)").pack()
entry_area = tk.Entry(root)
entry_area.pack()

# Age
tk.Label(root, text="Age (years)").pack()
entry_age = tk.Entry(root)
entry_age.pack()

# Rooms
tk.Label(root, text="Number of Rooms").pack()
entry_rooms = tk.Entry(root)
entry_rooms.pack()

# Button
tk.Button(root, text="Predict Price", command=predict_price, bg="blue", fg="white").pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()