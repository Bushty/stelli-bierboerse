import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

# Initiale Preise für die Getränke festlegen
prices = {
    "Wasser": 1.00,
    "Cola": 2.00,
    "Bier": 3.00,
    "Wein": 5.00,
    "Whiskey": 10.00
}

# Speichert die Preisgeschichte jedes Getränks für die Grafik
price_history = {drink: deque([price], maxlen=50) for drink, price in prices.items()}

# Funktion, die den Preis nach einem Kauf erhöht und andere senkt
def buy_drink(drink_name):
    if drink_name in prices:
        # Preis des gekauften Getränks erhöhen
        prices[drink_name] = round(prices[drink_name] * 1.05, 2)
        # Andere Getränke im Preis leicht senken
        for other_drink in prices:
            if other_drink != drink_name:
                prices[other_drink] = round(prices[other_drink] * 0.98, 2)
        # Preis zur Historie hinzufügen
        for drink in prices:
            price_history[drink].append(prices[drink])
        # Grafik aktualisieren
        update_plot()

# Aktualisierung der Grafik
def update_plot():
    ax.clear()
    ax.set_title("Preisverlauf der Getränke")
    ax.set_xlabel("Käufe")
    ax.set_ylabel("Preis in €")
    # Preise der letzten 50 Schritte für jedes Getränk plotten
    for drink, history in price_history.items():
        ax.plot(list(history), label=drink)
    ax.legend()
    canvas.draw()

# GUI einrichten
root = tk.Tk()
root.title("Getränke-Börse Simulation")
root.geometry("800x600")

# Matplotlib-Figur für den Plot
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Buttons für jedes Getränk erstellen
frame = ttk.Frame(root)
frame.pack(pady=20)
for drink in prices.keys():
    button = ttk.Button(frame, text=f"Kaufe {drink}", command=lambda d=drink: buy_drink(d))
    button.pack(side=tk.LEFT, padx=10)

# Initiale Grafik anzeigen
update_plot()

# GUI-Schleife starten
root.mainloop()