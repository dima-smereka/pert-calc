import tkinter as tk

# Define a function to calculate the PERT estimate
def calculate_pert():
    # Get the values from the text entry boxes and convert them to floats
    optimistic = float(optimistic_entry.get())
    most_likely = float(most_likely_entry.get())
    pessimistic = float(pessimistic_entry.get())
    qa_percentage = float(qa_percentage_var.get())
    risk_percentage = float(risk_percentage_var.get())
    
    # Calculate the PERT estimate using the formula: (optimistic + 4 * most_likely + pessimistic) / 6
    pert_estimate = (optimistic + 4 * most_likely + pessimistic) / 6
    
    # Calculate the QA value using the formula: pert_estimate * (qa_percentage / 100)
    qa_value = pert_estimate * (qa_percentage / 100)
    
    # Calculate the risk value using the formula: pert_estimate * (risk_percentage / 100)
    risk_value = pert_estimate * (risk_percentage / 100)
    
    # Calculate the final PERT estimate by adding the QA value and risk value to the PERT estimate
    final_pert_estimate = pert_estimate + qa_value + risk_value
    
    # Update the label to display the final PERT estimate with two decimal places
    pert_label.config(text=f"Final PERT Estimate: {final_pert_estimate:.2f}")

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

# Create a label for the QA percentage
qa_percentage_label = tk.Label(root, text="QA Percentage:")
qa_percentage_label.pack()

# Create a dropdown menu for the QA percentage
qa_percentage_var = tk.StringVar(root)
qa_percentage_var.set("12")
qa_percentage_dropdown = tk.OptionMenu(root, qa_percentage_var, "10", "15", "20", "25", "30")
qa_percentage_dropdown.pack()

# Create a label for the risk percentage
risk_percentage_label = tk.Label(root, text="Risk Percentage:")
risk_percentage_label.pack()

# Create a dropdown menu for the risk percentage
risk_percentage_var = tk.StringVar(root)
risk_percentage_var.set("10")
risk_percentage_dropdown = tk.OptionMenu(root, risk_percentage_var, "10", "15", "20", "25", "30")
risk_percentage_dropdown.pack()

# Create a button to calculate the PERT estimate when clicked
calculate_button = tk.Button(root, text="Calculate PERT", command=calculate_pert)
calculate_button.pack()

# Create a label to display the final PERT estimate
pert_label = tk.Label(root, text="")
pert_label.pack()

# Start the main event loop to display the window
root.mainloop()
