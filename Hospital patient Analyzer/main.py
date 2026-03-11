import numpy as np
import pandas as pd
from customtkinter import *
import os
import csv
from tkinter import messagebox,ttk,filedialog
def show_risk_patient():
    high_risk_window = CTk()
    high_risk_window.title("High Risk Patient")
    df = pd.read_csv("Patient_Data.csv")
    high_risk = df[(df["Heart Rate"]>100) &
                    (df["Cholestrol Level"]>240) & 
                    (df["Sugar Level"]>180) & 
                    (df["Blood Pressure"]>140)]
    columns = list(high_risk.columns)

    tree = ttk.Treeview(high_risk_window, columns=columns, show="headings")

    # create headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.pack(fill="both", expand=True)

    # insert filtered data
    for index, row in high_risk.iterrows():
        tree.insert("", "end", values=list(row))
    
    high_risk_window.mainloop()



def view():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files","*.csv")])
    if not file_path:
        return
    view_app = CTk()
    view_app.title(file_path)
    tree = ttk.Treeview(view_app, show="headings")
    tree.pack(expand=True, fill="both", padx=20, pady=20)
    for item in tree.get_children():
        tree.delete(item)

    # 3. Read and insert data
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Get first row as header
        
        # Configure columns based on CSV header
        tree["columns"] = header
        for col in header:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Insert rows
        for row in reader:
            tree.insert("", "end", values=row)

    view_app.mainloop()





def contact():
    contact_window = CTk()
    contact_window.title("Contact Info")
    contact_window.geometry("400x145")
    contact_window.resizable(False,False)
    CTkLabel(contact_window,text="Contact :",font=("Times", 20 , "bold")).grid(row=0,column=0,padx=20,pady=10)
    CTkLabel(contact_window,text="+923416594987",font=("Times", 20 )).grid(row=0,column=1,padx=20,pady=10)
    CTkLabel(contact_window,text="Email :",font=("Times", 20 , "bold")).grid(row=1,column=0,padx=20,pady=10)
    CTkLabel(contact_window,text="zubairtahir064@gmail.com",font=("Times", 20 )).grid(row=1,column=1,padx=20,pady=10)

    contact_window.mainloop()



def about():
    about_window = CTk()
    about_window.title("About Software")

    CTkLabel(about_window,text='''
 About Patient Analyzation System

Patient Analyzation System is a software application developed to assist in organizing, analyzing, and managing patient-related data efficiently.
 The system is designed to help users process patient records, perform data analysis, 
and generate useful insights that can support better understanding and management of healthcare information.

The software focuses on simplicity, accuracy, and ease of use, allowing users to work with patient data in a structured and reliable manner.

Software Name: Patient Analyzation System
Author: M Zubair Tahir
Copyright © 2026 M Zubair Tahir. All rights reserved.

No part of this software may be reproduced, modified, or distributed without the permission of the author.
 The software may receive updates and improvements in future versions to enhance features, performance, and reliability.           
''',font=("arial",15)).pack(padx=10)



    about_window.mainloop()
def analyze():
    # load CSV File
    age = np.genfromtxt("Patient_Data.csv",delimiter=",",skip_header=1,usecols=(2))
    heart_rate = np.genfromtxt("Patient_Data.csv",delimiter=",",skip_header=1,usecols=(4))
    Blood_pressure = np.genfromtxt("Patient_Data.csv",delimiter=",",skip_header=1,usecols=(5))
    chol = np.genfromtxt("Patient_Data.csv",delimiter=",",skip_header=1,usecols=(6))
    sugar = np.genfromtxt("Patient_Data.csv",delimiter=",",skip_header=1,usecols=(7))
    total_p = age.shape[0]
    avg_age = np.mean(age)
    max_age = np.max(age)
    min_age = np.min(age)
    avg_hr = np.mean(heart_rate)
    max_hr = np.max(heart_rate)
    min_hr = np.min(heart_rate)
    avg_chol = np.mean(chol)
    max_chol = np.max(chol)
    min_chol = np.min(chol)
    avg_sugar = np.mean(sugar)
    max_sugar = np.max(sugar)
    min_sugar = np.min(sugar)
    # avg_bp = np.max(Blood_pressure)


    analyze_window = CTk()
    analyze_window.title("Data Analyztion Window of Patients")
    analyze_window.resizable(False,False)

    f1 = CTkFrame(analyze_window, width=900, fg_color="#3B82F6")
    f1.pack(padx=30,pady=10)
    CTkLabel(f1,text="Analyzation of CSV File 📂", font=("arial", 28, "bold"),width=500,height=50,text_color="white").pack()


    f = CTkFrame(analyze_window)
    f.pack()
    CTkLabel(f,text=f"Total Patients: {total_p}",font=("Times", 15, "bold")).grid(row= 0, column= 0,padx=20,pady=5)
    CTkLabel(f,text=f"Average Age: {avg_age:.0f}",font=("Times", 15, "bold")).grid(row= 1, column= 0,padx=20,pady=5)
    CTkLabel(f,text=f"Maximum Age: {max_age:.0f}",font=("Times", 15, "bold")).grid(row= 2, column= 0,padx=20,pady=5)
    CTkLabel(f,text=f"Minimum Age: {min_age:.0f}",font=("Times", 15, "bold")).grid(row= 3, column= 0,padx=20,pady=5)
    CTkLabel(f,text=f"Average Heart Rate: {avg_hr:.0f}",font=("Times", 15, "bold")).grid(row= 4, column=0, padx=20,pady=5)
    CTkLabel(f,text=f"Maximum Heart Rate: {max_hr:.0f}",font=("Times", 15, "bold")).grid(row= 5, column=0, padx=20,pady=5)
    CTkLabel(f,text=f"Minimum Heart Rate: {min_hr:.0f}",font=("Times", 15, "bold")).grid(row=0 , column=1, padx=20,pady=5)
    CTkLabel(f,text=f"Average Cholestrol: {avg_chol:.0f}",font=("Times", 15, "bold")).grid(row=1 , column=1, padx=20,pady=5)
    CTkLabel(f,text=f"Maximum Cholestrol: {max_chol:.0f}",font=("Times", 15, "bold")).grid(row= 2, column=1, padx=20,pady=5)
    CTkLabel(f,text=f"Minimum Cholestrol: {min_chol:.0f}",font=("Times", 15, "bold")).grid(row= 3, column= 1,padx=20,pady=5)
    CTkLabel(f,text=f"Average Sugar: {avg_sugar:.0f}",font=("Times", 15, "bold")).grid(row= 4, column=1, padx=20,pady=5)
    CTkLabel(f,text=f"Maximum Sugar: {max_sugar:.0f}",font=("Times", 15, "bold")).grid(row=5 , column=1, padx=20,pady=5)
    CTkLabel(f,text=f"Minimum Sugar: {min_sugar:.0f}",font=("Times", 15, "bold")).grid(row= 6, column= 0,padx=20,pady=5)
    analyze_window.mainloop()
  

def clear_entry():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    disease_entry.delete(0,END)
    heart_entry.delete(0,END)
    bp_entry.delete(0,END)
    chol_entry.delete(0,END)
    sugar_entry.delete(0,END)


def add_data():
    filename = "Patient_Data.csv"
    if os.path.isfile(filename):
        new_row = [id_var.get(),name_var.get(),age_var.get(),disease_var.get()
                   ,heart_var.get(),bp_var.get(),chol_var.get(),sugar_var.get()]
        with open(filename,'a+',newline="") as f:
            w = csv.writer(f)
            w.writerow(new_row)
        messagebox.showinfo('','Information Saved!')
        clear_entry()
    else:
        data = {
            'ID' : [id_var.get()],
            'Name' : [name_var.get()],
            'Age' : [age_var.get()],
            'Disease' : [disease_var.get()],
            'Heart Rate' : [heart_var.get()],
            'Blood Pressure' : [bp_var.get()],
            'Cholestrol Level' : [chol_var.get()],
            'Sugar Level' : [sugar_var.get()]
        }
        df = pd.DataFrame(data)
        df.to_csv(filename,index=False)
        messagebox.showinfo('','Information Saved!')
        clear_entry()
        print(df)




# ====================== Window ======================

window = CTk()
window.title("Hospital Patient Analyzer")
window.geometry("1000x750")
window.resizable(False, False)

set_appearance_mode("light")

# ====================== Variables ======================

heart_var = StringVar()
bp_var = StringVar()
chol_var = StringVar()
sugar_var = StringVar()

id_var = StringVar()
name_var = StringVar()
age_var = StringVar()
disease_var = StringVar()

# ====================== Heading Frame ======================

heading_frame = CTkFrame(window, width=900, height=70, fg_color="#3B82F6")
heading_frame.pack(pady=10)

heading = CTkLabel(
    heading_frame,
    text="Hospital Patient Analyzer",
    font=("Arial", 28, "bold"),
    text_color="white",
    width=1000
)

heading.pack(pady=15)

# ====================== Button Frame ======================

btn_frame = CTkFrame(window, fg_color="#E5E7EB")
btn_frame.pack(pady=10)

view_btn = CTkButton(
    btn_frame,
    text="View Data",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8"
    ,command=view
)

view_btn.grid(row=0, column=2, padx=30)

analyze_btn = CTkButton(
    btn_frame,
    text="Analyze Data",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8",
    command=analyze
)

analyze_btn.grid(row=0, column=1, padx=30)

add_btn = CTkButton(
    btn_frame,
    text="Add Data",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8",command=add_data
)

add_btn.grid(row=0, column=0, padx=30)

risk_btn = CTkButton(
    btn_frame,
    text="Show Risk Report",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8",
    command=show_risk_patient
)

risk_btn.grid(row=1, column=0, padx=30,pady=10)

contact_btn = CTkButton(
    btn_frame,
    text="Contact",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8",
    command = contact
)

contact_btn.grid(row=1, column=1, padx=30,pady=10)

about_btn = CTkButton(
    btn_frame,
    text="About",
    width=160,
    height=40,
    font=("Arial", 14, "bold"),
    corner_radius=8,
    hover_color="#1D4ED8",
    command=about
    
)

about_btn.grid(row=1, column=2, padx=30,pady=10)
# ====================== Information Title ======================

risk_title = CTkLabel(
    window,
    text="Personal Information",
    font=("Arial", 18, "bold"),
    text_color="#1F2937"
)

risk_title.pack(pady=(20, 5))

# ====================== Information Frame ======================

risk_frame = CTkFrame(
    window,
    width=900,
    height=160,
    border_color="#D1D5DB",
    border_width=1,
    corner_radius=10
)

risk_frame.pack(pady=10)

# ====================== information Labels ======================

CTkLabel(risk_frame, text="Patient ID :", font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=10)
CTkLabel(risk_frame, text="Patient Name :", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10)
CTkLabel(risk_frame, text="Patient Age :", font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=10)
CTkLabel(risk_frame, text="Disease :", font=("Arial", 16)).grid(row=3, column=0, padx=20, pady=10)

# ====================== Information Entries ======================
id_entry = CTkEntry(risk_frame, textvariable=id_var, width=150)
id_entry.grid(row=0, column=1, padx=20)

name_entry = CTkEntry(risk_frame, textvariable=name_var, width=150)
name_entry.grid(row=1, column=1, padx=20)

age_entry = CTkEntry(risk_frame, textvariable=age_var, width=150)
age_entry.grid(row=2, column=1, padx=20)

disease_entry = CTkEntry(risk_frame, textvariable=disease_var, width=150)
disease_entry.grid(row=3, column=1, padx=20)


# ====================== Patient Statistics Title ======================

title = CTkLabel(
    window,
    text="Patient Statistics",
    font=("Arial", 18, "bold"),
    text_color="#1F2937"
)

title.pack(pady=(20, 5))

# ====================== Patient Statistics Frame ======================

stats_frame = CTkFrame(
    window,
    width=900,
    height=180,
    border_color="#D1D5DB",
    border_width=1,
    corner_radius=10
)

stats_frame.pack(pady=10)

# ====================== Statistics Labels ======================

CTkLabel(stats_frame, text="Heart Rate:", font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=10)
CTkLabel(stats_frame, text="Blood Pressure :", font=("Arial", 16)).grid(row=1, column=0, padx=20, pady=10)
CTkLabel(stats_frame, text="Cholesterol :", font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=10)
CTkLabel(stats_frame, text="Sugar Level :", font=("Arial", 16)).grid(row=3, column=0, padx=20, pady=10)

# ====================== Statistics Entries ======================

heart_entry = CTkEntry(stats_frame, textvariable=heart_var, width=150)
heart_entry.grid(row=0, column=1, padx=20)

bp_entry = CTkEntry(stats_frame, textvariable=bp_var, width=150)
bp_entry.grid(row=1, column=1, padx=20)

chol_entry = CTkEntry(stats_frame, textvariable=chol_var, width=150)
chol_entry.grid(row=2, column=1, padx=20)

sugar_entry = CTkEntry(stats_frame, textvariable=sugar_var, width=150)
sugar_entry.grid(row=3, column=1, padx=20)


window.mainloop()