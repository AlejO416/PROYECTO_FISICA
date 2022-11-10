#se importan las librerias necesarias para realizar el trabajo.
import tkinter
from tkinter import *
import serial, time 
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font, ttk

from firebase import firebase 
#agregamos la direccion de la base de datos 
firebase= firebase.FirebaseApplication("https://sensor-de-temperatura-eadea-default-rtdb.firebaseio.com/",None)


arduino=serial.Serial("COM3", 9600)#leemos los datos en el puerto serial
time.sleep(2)#el tiempo entre cada lectura
string=arduino.readline()#linea que lee la temperatura
string2=arduino.readline()#linea que lee la hummedad
print(string)

#creamos la interfaz con tkinter
ventana = tkinter.Tk()

image=Image.open("anime.png")#agragamos una imagen a la interfaz 
ventana.config(bg="dodger blue")
ventana.title("Datos de Temperatura y Humedad")#titulo de la ventana 
ventana.geometry("600x400")#tamaño de la ventana 
image=image.resize((600, 400))
img=ImageTk.PhotoImage(image)
imagen=Label(ventana, image=img).place(x=0, y=0, relwidth=1.0, relheight=1.0)#tamaño de la imagen 


def traer():
	

	string=arduino.readline()#leemos nuevamente la temperatura y la humeadad enuna sola linea
	stringS=string.decode("utf-8")#convertimos los datos de bytes a string 
	temp=stringS[0:4:1]#separamos en una variable temp los primeros cinco caracteres de la linea leida para la temperatura de 0 a 4 en pasos de 1
	hum=stringS[5:9:1]#separamos en una variable hum los segundos cinco caracteres de la linea leida para la humedad de 5 a 9 en pasos de 1
	
	print(stringS)
	print(hum)
	print(temp)
	r.set(temp)#agregamos los datos de la variable temp a una variable r
	r2.set(hum)


	stringS= '' #variable de tipo caracter donde se almacena la lectura del sensor
	
	
	#creamos una variable datos donde almacenamos la temperatura y la humedad
	datos={
	'Temperatura':temp,
	'Humedad':hum
	}


	resultado=firebase.post('/tuto/datos',datos)#con la variable resultados posteamos en la base de datos (firebase) en una carpeta llamada tuto y le enviamos una variable datos.



r = StringVar()#pasamos los datos a tipo stringvar
r2= StringVar()

#creamos los widgets de la interfaz grafica
etiqueta3=Label(ventana, text="Temperatura", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=85, y=10)
Entry(ventana, justify=CENTER, state=DISABLED, textvariable=r,font=font.Font(family="Times", size=14)).place(x=210, y=10)
etiqueta4=Label(ventana, text="Humedad", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=85, y=80)
Entry(ventana, justify=CENTER, state=DISABLED, textvariable=r2, font=font.Font(family="Times", size=14)).place(x=210, y=80)
boton= Button(ventana, command=traer, text="Actualizar").place(x=268, y=180)
medida=Label(ventana, text="Celsius", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=402, y=10)
porcentaje=Label(ventana, text="%", bg="RoyalBlue4",fg="DarkOliveGreen1", font=0).place(x=402, y=80)
exit_button = Button(ventana, text="Salir", command=ventana.destroy).place(x=283,y=230)


ventana.mainloop()
