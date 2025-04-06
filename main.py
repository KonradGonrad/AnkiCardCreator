import json
from spanish import set_1, set_2, set_3, set_4
from note_templates import AnkiCardCreator

sets = [set_1, set_2, set_3, set_4]
ANKI_API_URL = "http://127.0.0.1:8765"

DECK_NAMES = ['Spanish-Polish']

DECK_NAME = DECK_NAMES[-1]



# for set in sets:
#     AnkiCardCreator.ImportToAnki(set, ANKI_API_URL)

for set in sets:
    for flashcards in set:
        AnkiCardCreator.ImportToAnki(cards=flashcards, anki_url=ANKI_API_URL)
