import tkinter
from tkinter import *
import serial, time 
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font, ttk

from firebase import firebase 

firebase= firebase.FirebaseApplication("https://sensor-de-temperatura-eadea-default-rtdb.firebaseio.com/",None)


arduino=serial.Serial("COM3", 9600)
time.sleep(2)
string=arduino.readline()
string2=arduino.readline()
print(string)


ventana = tkinter.Tk()

image=Image.open("anime.png")
ventana.config(bg="dodger blue")
ventana.title("Datos de Temperatura y Humedad")
ventana.geometry("600x400")
image=image.resize((600, 400))
img=ImageTk.PhotoImage(image)
imagen=Label(ventana, image=img).place(x=0, y=0, relwidth=1.0, relheight=1.0)


def traer():
	

	string=arduino.readline()
	stringS=string.decode("utf-8") 
	temp=stringS[0:4:1]
	hum=stringS[5:9:1]
	
	print(stringS)
	print(hum)
	print(temp)
	r.set(temp)
	r2.set(hum)


	stringS= ''

	datos={
	'Temperatura':temp,
	'Humedad':hum
	}


	resultado=firebase.post('/tuto/datos',datos)



r = StringVar()
r2= StringVar()

etiqueta3=Label(ventana, text="Temperatura", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=85, y=10)
Entry(ventana, justify=CENTER, state=DISABLED, textvariable=r,font=font.Font(family="Times", size=14)).place(x=210, y=10)
etiqueta4=Label(ventana, text="Humedad", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=85, y=80)
Entry(ventana, justify=CENTER, state=DISABLED, textvariable=r2, font=font.Font(family="Times", size=14)).place(x=210, y=80)
boton= Button(ventana, command=traer, text="Actualizar").place(x=268, y=180)
medida=Label(ventana, text="Celsius", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=402, y=10)
porcentaje=Label(ventana, text="%", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=402, y=80)
exit_button = Button(ventana, text="Salir", command=ventana.destroy).place(x=283,y=230)


ventana.mainloop()