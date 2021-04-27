#Credit to Derrick Sherrill on Youtube 
from tkinter import *
import pandas as pd

def submit_fields():
    path = 'Final_Project.csv'
    df1 = pd.read_csv(path)
    SeriesA = df1['Name']
    SeriesB = df1['Calories_Burnt']
    SeriesC = df1['Workout_Length']
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)
    df2 = pd.DataFrame({"Name":SeriesA, "Calories_Burnt":SeriesB, 'Workout_Length':SeriesC})
    df2.to_csv(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

master = Tk()

Label(master, text="Name").grid(row=0)
Label(master, text="Calories_Burnt").grid(row=1)
Label(master, text="Workout_Length").grid(row=2)

entry1 = Entry(master)
entry2 = Entry(master)
entry3 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3,column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=3,column=1, pady=4)

mainloop()