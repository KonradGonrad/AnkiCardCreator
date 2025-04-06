import json
from note_templates import AnkiCardCreator

ANKI_API_URL = "http://127.0.0.1:8765"

DECK_NAMES = ['Python - base',
              'Python - scrapy',
              'Spanishh',
              'test']

DECK_NAME = DECK_NAMES[-1]

cards = AnkiCardCreator.messengerCard(front=['Hola', 'Bueno'],
                                      back=['Hej', 'dobrze'],
                                      deck_name='test',
                                      type_card='T',
                                      ).cards

AnkiCardCreator.ImportToAnki(cards=cards, anki_url=ANKI_API_URL)