import tkinter as tk
from tkinter import font
import requests
HEIGHT=500
WIDTH=600

def test_function(entry):
    print("button clicked  ",entry)

#2db94bf59f9168b21cec03984c57f083
# api.openweathermap.org/data/2.5/forecast?id={city ID}
def format_response(weather):
    try:
        q=weather['name']
        z=weather['weather'][0]['description']
        e=weather['main']['temp']
        r=weather['wind']['speed']
        #r= weather['main']['temp_max']
        finall='City: %s \nDescription: %s \nTemperature(ͦF): %s \nWind Speed(mph): %s' %(q,z,e,r)
    except:
        finall='Problem Retrieving Data'
    return finall 
def get_weather(city):
    weather_key='2db94bf59f9168b21cec03984c57f083'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params=params)
    weather=response.json()
    
    label['text']=format_response(weather)
root=tk.Tk() 
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame =tk.Frame(root,bg='#91a8ee',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get weather",font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame =tk.Frame(root,bg='#91a8ee',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.5,anchor='n')

label=tk.Label(lower_frame,font=("courier",18))
label.place(relwidth=1,relheight=1)

root.mainloop()
