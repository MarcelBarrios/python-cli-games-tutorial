# cli-games/asciiart.py
import requests
import random

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)

if font == "random":
    data = requests.get('http://artii.herokuapp.com/fonts_list')
    fontsArray = data.text.split('\n')

    for i in range(3):
        font = random.choice(fontsArray)
        getAsciiArt(text, font)
elif font:
    font = font
    getAsciiArt(text, font) 
elif font == "":
    getAsciiArt(text, font)