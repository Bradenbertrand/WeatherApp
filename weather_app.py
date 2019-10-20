import tkinter as tk
import requests


HEIGHT = 500
WIDTH = 600

# 8f8793b76b65834fefbb7567e11bae7c
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
    try:
        city_name = weather['name']
        city_description = weather['weather'][0]['description']
        city_temp = weather['main']['temp']
        return city_name + " " + city_description + " " + str(city_temp)
    except:
        print("This city is invalid")

def get_weather(city):
    weather_key = '8f8793b76b65834fefbb7567e11bae7c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

entry_frame = tk.Frame(root, bg='#80c1ff', bd=5)
entry_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') 

entry = tk.Entry(entry_frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(entry_frame, text="Pull Information", bg='#3366cc', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

output_frame = tk.Frame(root, bg ='#80c1ff', bd=10)
output_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(output_frame)
label.place(relwidth=1, relheight=1)



root.mainloop()