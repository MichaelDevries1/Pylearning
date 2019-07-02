import tkinter as tk
from PIL import ImageTk, Image
import requests

FONT = 30
IMAGE_NAME = 'landscape.jpeg'

# Current weather: api.openweathermap.org/data/2.5/weather?q={city name}
# 5 day weather: api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# API key: ca2b89c6af0d2220dd8ab6b4dfcdd439



def get_weather(city):
    try:
        weather_api_key = 'ca2b89c6af0d2220dd8ab6b4dfcdd439'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_api_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()

        result_label['text'] = format(weather)
    except:
        result_label['text'] = "Can't connect to the server."


def format(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_string = 'City: %s\nCondition: %s\nTemp (°F): %s°' %(name, description, str(temp))
    except:
        final_string = 'We are unable to retrieve this information.'

    return final_string


root = tk.Tk()
root.title('Weather App')
root.geometry('600x500')
root.config(bg='black')

# Background
bg_image = Image.open(IMAGE_NAME).resize((600, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# City find box
input_frame = tk.Frame(root, bd=5, bg='#80c1ff')
city_input = tk.Entry(input_frame, font=FONT)
find_button = tk.Button(input_frame, text='Find', font=FONT, command=lambda: get_weather(city_input.get()))

# root.bind('<Return>', get_weather(city_input.get))

input_frame.place(anchor='n', relx=.5, rely=.1, relwidth=.75, relheight=.07)
city_input.place(relwidth=.65, relheight=1)
find_button.place(relx=.7, relwidth=.3, relheight=1)

# Results box
lower_frame = tk.Frame(root, bd=5, bg='#80c1ff')
result_label = tk.Label(lower_frame, font=('Arial', 15), anchor='nw', justify='left', bg='white')

lower_frame.place(anchor='n', relx=.5, rely=.22, relwidth=.75, relheight=.7)
result_label.place(relwidth=1, relheight=1)

root.mainloop()
