import tkinter as tk

# Define a function to calculate the PERT estimate
def calculate_pert():
    # Get the values from the text entry boxes and convert them to floats
    optimistic = float(optimistic_entry.get())
    most_likely = float(most_likely_entry.get())
    pessimistic = float(pessimistic_entry.get())
    
    # Calculate the PERT estimate using the formula: (optimistic + 4 * most_likely + pessimistic) / 6
    pert = (optimistic + 4 * most_likely + pessimistic) / 6
    
    # Update the label to display the PERT estimate with two decimal places
    pert_label.config(text=f"PERT Estimate: {pert:.2f}")

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("PERT Calculator")

# Create a label for the optimistic estimate
optimistic_label = tk.Label(root, text="Optimistic Estimate:")
optimistic_label.pack()

# Create a text entry box for the optimistic estimate
optimistic_entry = tk.Entry(root)
optimistic_entry.pack()

# Create a label for the most likely estimate
most_likely_label = tk.Label(root, text="Most Likely Estimate:")
most_likely_label.pack()

# Create a text entry box for the most likely estimate
most_likely_entry = tk.Entry(root)
most_likely_entry.pack()

# Create a label for the pessimistic estimate
pessimistic_label = tk.Label(root, text="Pessimistic Estimate:")
pessimistic_label.pack()

# Create a text entry box for the pessimistic estimate
pessimistic_entry = tk.Entry(root)
pessimistic_entry.pack()

# Create a button to calculate the PERT estimate when clicked
calculate_button = tk.Button(root, text="Calculate PERT", command=calculate_pert)
calculate_button.pack()

# Create a label to display the PERT estimate
pert_label = tk.Label(root, text="")
pert_label.pack()

# Start the main event loop to display the window
root.mainloop()
#created by SS95