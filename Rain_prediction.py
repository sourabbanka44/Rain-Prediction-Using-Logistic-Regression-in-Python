import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

HEIGHT = 500
WIDTH = 850

weatherDataset = pd.read_csv("weather.csv")
weatherDataset.head()

X = weatherDataset[['MinTemp','MaxTemp','Rainfall','WindSpeed','Humidity','Pressure','Cloud','RainToday']]
y = weatherDataset['RainTomorrow']

X_train = X

y_train = y

logreg = LogisticRegression()

logreg.fit(X_train,y_train)

def logistic(X_testInstance):
	y_pred=logreg.predict(X_testInstance)

	if y_pred==0:
		label['text'] = "Sunny Day"
	elif y_pred==1:
		label['text'] = "Rainy Day"



root = tk.Tk()
root.resizable(width=False, height=False)
# Code to add widgets...

#Creating a rectangular area
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#attaching a background image
background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#creating a frame for labels,entrys and button
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.3, anchor='n')


#creating 8 labels
label1 = tk.Label(frame,text="MinTemp")
label1.grid(row=0,column=0)

label2 = tk.Label(frame,text="MaxTemp")
label2.grid(row=0,column=2)

label3 = tk.Label(frame,text="Rainfall")
label3.grid(row=0,column=4)

label4 = tk.Label(frame,text="WindSpeed")
label4.grid(row=0,column=6)

label5 = tk.Label(frame,text="Humidity")
label5.grid(row=3,column=0)

label6 = tk.Label(frame,text="Pressure")
label6.grid(row=3,column=2)

label7 = tk.Label(frame,text="Cloud")
label7.grid(row=3,column=4)

label8 = tk.Label(frame,text="RainToday")
label8.grid(row=3,column=6)

label9 = tk.Label(frame,bg='#80c1ff',text="	")
label9.grid(row=6,column=1)

label10 = tk.Label(frame,bg='#80c1ff',text="	")
label10.grid(row=6,column=5)



#creating 8 entry widgets
entry = tk.Entry(frame, font=40,width=15)
entry.grid(row=1,column=0)

entry2 = tk.Entry(frame, font=40,width=15)
entry2.grid(row=1,column=2)

entry3 = tk.Entry(frame, font=40,width=15)
entry3.grid(row=1,column=4)

entry4 = tk.Entry(frame, font=40,width=15)
entry4.grid(row=1,column=6)

entry5 = tk.Entry(frame, font=40,width=15)
entry5.grid(row=4,column=0)

entry6 = tk.Entry(frame, font=40,width=15)
entry6.grid(row=4,column=2)

entry7 = tk.Entry(frame, font=40,width=15)
entry7.grid(row=4,column=4)

entry8 = tk.Entry(frame, font=40,width=15)
entry8.grid(row=4,column=6)



button = tk.Button(frame, text="Predict", font=40,command=lambda: logistic(pd.DataFrame([[float(entry.get()),float(entry2.get()),float(entry3.get()),float(entry4.get()),float(entry5.get()),float(entry6.get()),float(entry7.get()),float(entry8.get())]])))
button.grid(row=6,column=3)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.75, relwidth=0.65, relheight=0.25, anchor='n')

#label for printing the predicted result
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#END
root.mainloop()