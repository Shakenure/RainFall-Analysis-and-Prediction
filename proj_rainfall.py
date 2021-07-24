# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:04:24 2018

@author: Lenovo
"""

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
import tkinter as tk
from tkinter import ttk

from tkinter import *
import pyqtgraph as pg
#Source Serif Pro
LARGE_FONT = ("Source Serif Pro bold",14,'bold')
BUTTON_FONT=("Frutiger", 10,"bold")
from mini import *
import mini as mi


from PIL import *


class RianApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        photo = PhotoImage(file="img1.png")
        
        tk.Tk.wm_title(self, "RainFall Analysis and Prediction")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photo = PhotoImage(file="img1.png")

        img=Label(self,image=photo)
        img.image =photo
        img.place(x=0,y=0)
        
        label = tk.Label(self, text="RAINFALL ANALYSIS AND PREDICTION",bg='#98D8D8')
        label.config(font=("courier",20,"bold"))
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self, text="MENU", bg='#5DBCD2',font=BUTTON_FONT)

        label1.pack(pady=20, padx=10)

        button1 = tk.Button(self,bg="#0072ed",highlightbackground="#0072ed", text="Analysis Of Rainfall",
                             command=lambda: controller.show_frame(Page1),font=BUTTON_FONT)

        button1.pack(pady=20, padx=10)

        button2 = tk.Button(self, text="Prediction",bg="#0072ed",highlightbackground="#0072ed",
                             command=lambda: controller.show_frame(PageTwo),font=BUTTON_FONT)
        button2.pack(pady=20, padx=10)

        b3 = tk.Button(self, text="Exit",bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT, command=lambda: self.quit())
        b3.pack(pady=10, padx=10)
        ### exit not working


class Page1(tk.Frame):  # analysis page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background='#5DBCD2')

        self.label = tk.Label(self, text="Welcome to rainfall analysis ", font=LARGE_FONT, bg='#5DBCD2')
        self.label.grid(row=0, column=int(self.label.winfo_width() / 2 + 0.5), padx=40, pady=40)

        self.button1 = tk.Button(self, text ='Seasonal',bg="#0072ed",highlightbackground="#0072ed" ,font=BUTTON_FONT,command= monthly_subdivision )
        self.button1.grid(row=2, column=0, sticky=E, padx=200, pady=40)

        self.button2 = tk.Button(self, text='Total rainfall',bg="#0072ed",highlightbackground="#0072ed", command=yearly_subdivision,font=BUTTON_FONT)
        self.button2.grid(row=2, column=1,pady=40)

        self.button3 = tk.Button(self, text='Seasonal Bar plot',bg="#0072ed",highlightbackground="#0072ed" ,command= lambda:hbar(),font=BUTTON_FONT)
        self.button3.grid(row=2, column=2, sticky=E, padx=220, pady=40)
        #upper monthly button:-
        self.button4 = tk.Button(self, text='Avrage Annual Rainfall',bg="#0072ed",highlightbackground="#0072ed", command=annual_subdivision,font=BUTTON_FONT)
        self.button4.grid(row=1, column=int(self.label.winfo_width() / 2 + 0.5), padx=40)

        # Create a Tkinter variable
        self.tkvar = StringVar(self)

        text = Label(self, text='select subdivision', bg='#5DBCD2')
        text.config(font=("courier", 12,"bold"))
        optionmenu = ttk.OptionMenu(self, self.tkvar, *subs1)

        self.button4 = tk.Button(self, text='Rainy season', command=lambda: self.pr(),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.button5 = tk.Button(self, text='Annual Rainfall and Rainy seasonal',command=lambda: self.ans(),highlightbackground="#27bfeb",bg="#0072ed",font=BUTTON_FONT)
        self.button7 = tk.Button(self, text="Seasonal Subdivision", command=lambda: self.ps(),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.button6 = tk.Button(self, text='Highest Rainfall', command=lambda: self.highest(),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.button8 = tk.Button(self, text='Lowest Raindall', command=lambda: self.lowest(),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.button9 = tk.Button(self, text='Mean Rainfall', command=lambda: self.mean(),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.bback = tk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage),bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)
        self.button55 = tk.Button(self, text='Monthly subdivision', command=self.ff,bg="#0072ed",highlightbackground="#0072ed",font=BUTTON_FONT)

        text.grid(row=4, column=int(self.label.winfo_width() / 2 + 0.5))
        optionmenu.grid(row=6, column=int(self.label.winfo_width() / 2 + 0.5))
        self.button4.grid(row=8, column=0, padx=40, pady=40)
        self.button5.grid(row=8, column=1, pady=40)
        self.button7.grid(row=8, column=2, padx=40, pady=40)
        #self.button55.grid(row=8, column=3, pady=40)
        self.button6.grid(row=9, column=0, padx=40, pady=20)
        self.button8.grid(row=9, column=1, pady=20)
        self.button9.grid(row=9, column=2, padx=40, pady=20)
        self.button55.grid(row=10, column=int(self.label.winfo_width() / 2 + 0.5), padx=40, pady=20)
        self.bback.grid(row=11, column=int(self.label.winfo_width() / 2 + 0.5), padx=40, pady=40)

    def ff(self):
            num = subs1[self.tkvar.get()]
            monthlysub(num)
            return()
        
    def highest(self):
        
        num = subs1[self.tkvar.get()]
        high = sub_data[num].ANNUAL.max()
        year = sub_data[num].YEAR.loc[sub_data[num]['ANNUAL'] == high].values

        str1 = "highest rainfall in " + str(subs[num]) + " is " + str(high) + " mm. In the year " + str(year[0])

        messagebox.showinfo("heighest rainfall is", str1)

        return ()

    def lowest(self):
        num = subs1[self.tkvar.get()]
        low = sub_data[num].ANNUAL.min()
        year = sub_data[num].YEAR.loc[sub_data[num]['ANNUAL'] == low].values

        str1 = "The lowest rainfall recorded in " + str(subs[num]) + " is " + str(low) + " mm. In the year " + str(
            year[0])

        messagebox.showinfo("The lowest rainfall", str1)

        return ()

    def mean(self):
        num = subs1[self.tkvar.get()]
        mean1 = sub_data[num].ANNUAL.mean()
        str1 = "The average rainfall  in " + str(subs[num]) + " is " + str(mean1)
        messagebox.showinfo("The average rainfall", str1)
        return ()

    def pr(self):
        num = subs1[self.tkvar.get()]
        plotrainy(num)
        return

    def ans(self):
        num = subs1[self.tkvar.get()]
        plotannual(num)
        return

    def ps(self):
        num = subs1[self.tkvar.get()]
        plotseason_wise(num)
        return


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background='#5DBCD2')
        label = tk.Label(self, text="PREDICTION OF ANNUAL RAINFALL", font=LARGE_FONT, bg='#5DBCD2', padx=50, pady=50)
        label.pack(padx=30)
        self.tkvar = StringVar(self)
        text = Label(self, text='select subdivision', bg='#5DBCD2')
        text.config(font=("courier", 12,"bold"))
        optionmenu = ttk.OptionMenu(self, self.tkvar,*dictmp1)
        text.pack(padx=30)
        optionmenu.pack(padx=30, pady=30)
        text1 = Label(self, text='Enter monsoon rainfall (in mm) ', bg='#5DBCD2')
        text1.config(font=("courier", 12,"bold"))
        text1.pack()
        self.entry = Entry(self)
        self.entry.pack(padx=30, pady=30)
        button1 = Button(self, text="Show Train Graph", command=lambda: self.pred1(),font=BUTTON_FONT,bg="#0072ed",highlightbackground="#0072ed")
        button1.pack(padx=30)
        
        button4=Button(self, text="Show test Graph", command=lambda: self.pred3(),font=BUTTON_FONT,bg="#0072ed",highlightbackground="#0072ed")
        button4.pack(padx=30, pady=30)
        
        button3 = Button(self, text="Predict Annual Rainfall", command=lambda: self.pred2(),font=BUTTON_FONT,bg="#0072ed",highlightbackground="#0072ed")
        button3.pack(padx=30, pady=30)

        button2 = tk.Button(self, text="back",
                             command=lambda: controller.show_frame(StartPage),font=BUTTON_FONT,bg="#0072ed",highlightbackground="#0072ed")
        button2.pack()
        
        
    def pred1(self):
        num = subs1[self.tkvar.get()]
        pred(num)
        return

    def pred2(self):
        num = subs1[self.tkvar.get()]
        val = self.entry.get()
        c = mpred(num, int(val))
        messagebox.showinfo("Rainfall Prediction", str(c))
        return
    def pred3(self):
        num = subs1[self.tkvar.get()]
        pred22(num)
        return
    

app = RianApp()
app.mainloop()



