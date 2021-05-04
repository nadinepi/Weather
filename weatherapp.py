from tkinter import *
import requests

root = Tk()

root.title('Weather')


l1 = Label(root, text='Enter city: ', anchor=W)
l1.grid(row=0,column=0)

city = StringVar()
e1 = Entry(root, textvariable=city)
e1.grid(row=0,column=1)
city.set('Toronto')

x = StringVar()
y = StringVar()


def getinfo():
    global x
    global y 
    
    api = 'https://api.openweathermap.org/data/2.5/weather?APPID=8a121984404e1bbc8ac8ade851eb6b91&q='
    url = api + city.get()
    json = requests.get(url).json()
    
    
    conditions = json['weather'][0]['description']
    temp = json['main']['temp']
    
    celctemp = float(temp) - 273
    
    
    x.set(conditions)
    y.set(round(celctemp, 2))
    

b1 = Button(root, text='Get weather info', command=getinfo)
b1.grid(row=2, column=1)

space = Label(root, text='')
space.grid(row=3, column=0)

l2 = Label(root, text = 'Conditions: ', anchor=W)
l2.grid(row=4, column=0)

l3 = Label(root, textvariable = x)
l3.grid(row=4, column=1)

l6 = Label(root, text= "°C")
l6.grid(row=5, column=2)

l4 = Label(root, text = 'Temperature: ', anchor=W)
l4.grid(row=5, column=0)

l5 = Label(root, textvariable = y)
l5.grid(row=5, column=1)

root.mainloop()