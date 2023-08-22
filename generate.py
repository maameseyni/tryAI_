from flask import Flask, render_template, url_for
import tkinter as tk
import random


def on_button_click_poisson():
    responses_1= ["Riz au poisson!", "Poissons braisés", "Poissons grillés plus frites"]
    response1 = random.choice(responses_1)
    label.config(text=response1)

def on_button_click_viande():
    responses_2= ["Sauce viande plus frite", "Soupe de viande", "Viande grilléé"]
    response2 = random.choice(responses_2)
    label.config(text=response2)

root = tk.Tk()
root.title("tryAI")

button1 = tk.Button(root,text="Poisson",command=on_button_click_poisson)
button2 = tk.Button(root,text="Viande", command=on_button_click_viande)
button1.pack()
button2.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()