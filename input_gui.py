import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="Welcome to Texas PAV",
                                  prompt="Please report your incident")

USER_INP2 = simpledialog.askstring(title="Location",
                                   prompt="Please enter location: City,County")

# Print the user input
print(USER_INP, "Thank you for your report!")
print(USER_INP2, "Thank you, your information has been recorded.")
