# AnkiCardCreator
A simple program to quickly create Anki cards, using AI to help generate and prepare the card data.

## What do we need to 
Python:
- requests
- random
- typing

Anki:
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159)

## How does it work?
The program is structured around custom Python classes that correspond to specific Anki note types (templates):
- In note_templates.py, you’ll find classes that represent different card types.
- Each class contains:
    - An __init__ method that builds a list of cards ready to send to Anki.
    - A to_card method that generates individual cards based on the Anki template.
    - A prompt method that helps you generate data using an AI tool (e.g., ChatGPT), based on your input material.

Once the cards are created, you can use the main.py file to send them directly to Anki via AnkiConnect.


Program automaticly adds flashcards into our decks. Based on the data in *spanish.py* I was able to introduce all data into my anki folder:
![spanish_anki](/spanish.png)