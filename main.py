import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Variables for the graph (you can replace this with actual data)
variables = [random.randint(1, 10) for _ in range(6)]

# Function to update the graph in the secondary window
def update_graph():
    # Clear the current plot
    ax.clear()
    # Update the variables with new random values for demonstration
    global variables
    variables = [random.randint(1, 10) for _ in range(6)]
    # Plot the updated data
    ax.bar(range(1, 7), variables, tick_label=["Var1", "Var2", "Var3", "Var4", "Var5", "Var6"])
    ax.set_ylim(0, 10)
    ax.set_title("Variable Values")
    # Redraw the canvas
    canvas.draw()
    # Schedule the next update after 30 seconds
    root.after(30000, update_graph)

# Function to handle button clicks
def button_click(button_id):
    print(f"Button {button_id} clicked")

# Create the main window for buttons
root = tk.Tk()
root.title("Main Window - Buttons")
root.geometry("300x200")

# Create and pack six buttons
for i in range(1, 7):
    button = ttk.Button(root, text=f"Button {i}", command=lambda i=i: button_click(i))
    button.pack(pady=5)

# Create the secondary window for the graph
toplevel = tk.Toplevel(root)
toplevel.title("Secondary Window - Graph")
toplevel.geometry("400x300")

# Set up the matplotlib figure and axes for the bar graph
fig, ax = plt.subplots()
ax.bar(range(1, 7), variables, tick_label=["Var1", "Var2", "Var3", "Var4", "Var5", "Var6"])
ax.set_ylim(0, 10)
ax.set_title("Variable Values")

# Create a FigureCanvasTkAgg widget to display the plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=toplevel)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the graph update loop
update_graph()

# Run the main loop
root.mainloop()
