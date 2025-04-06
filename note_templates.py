import requests
import random
from typing import Literal

class AnkiCardCreator:
    class BasicAndReversedCard:
        def __init__(self, front:list, back:list, deck_name:str, tags=None):
            if len(front) != len(back):
                raise ValueError("Lists must be the same length!")
            
            self.front = front
            self.back = back
            self.deck_name = deck_name
            self.model_name = "Basic (and reversed card)"
            self.tags = tags if tags else []
            self.cards = [self.to_card(front, back) for front, back in zip(self.front, self.back)]

        def to_card(self, front, back):
            return {
                "deckName": self.deck_name,
                "modelName": self.model_name,
                "fields": {"Front": front,
                           "Back": back},
                "options": {
                    "allowDuplicate": False
                },
                "tags": self.tags
            }
        
        def prompt(deck_name: str):
            return f"""
            Create Anki flashcards using the template:
            Each card should contain:
            \'Front\': the front of the card (e.g., 'Hola') — as a list[str]
            \'Back\': the back of the card (e.g., 'Hello') — as a list[str]

            Include:
            \'deck_name\' = \'{deck_name}\'
            Optional \'tags\' = list[str]

            Provide the output in the following format:
                front=[...],
                back=[...],
                deck_name='{deck_name}',
                tags=[...]

            Create that flashcards based on the following data:
            """
            
    class PokemonFightCard:
        def __init__(self, question: list[str], code: list[str], answer1: list[str], answer2: list[str], answer3: list[str], answer4: list[str], correct: list[str], deck_name: str, tags = None):
            length = len(question)
            if not all(len(lst) == length for lst in [code, answer1, answer2, answer3, answer4, correct]):
                raise ValueError("Lists are not the same length.")
            
            self.question, self.code, self.correct   = question, code, correct
            self.answer1, self.answer2, self.answer3, self.answer4 = answer1, answer2, answer3, answer4
            self.deck_name, self.model_name = deck_name, "Pokemon fight template"
            self.tags = tags if tags else []
            self.cards = [self.to_card(q, c, ans1, ans2, ans3, ans4, corr) 
                          for q, c, ans1, ans2, ans3, ans4, corr in zip(self.question, self.code, self.answer1, self.answer2, self.answer3, self.answer4, self.correct)]


        def to_card(self, question, code, ans1, ans2, ans3, ans4, corr):
            return {
                "deckName": self.deck_name,
                "modelName": self.model_name,
                "fields": {"Question": question,
                           "Code": code,
                           "Answer 1": ans1,
                           "Answer 2": ans2,
                           "Answer 3": ans3,
                           "Answer 4": ans4,
                           "Correct Answer": corr
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": self.tags
            }
        
        def prompt(deck_name):
            return f"""
                Create Anki flashcards using the template:
                Each card should contain:
	            \'Question\': The question (e.g., \'What is 5 + 1?\') as a list[str]
	            \'Code\': An optional code field (no code = empty string) as a list[str]
	            \'Answer 1\', \'Answer 2\', \'Answer 3\', \'Answer 4\': The possible answers (e.g., \'2\', \'4\', \'3\', \'6\') as a list[str]
	            \'Correct Answer\': The index of the correct answer (e.g., \'4\' for the correct answer being \'6\') as a list[str]
                include 'deck_name' = {deck_name} and optional tags.
                provide the answer in form:
                        question=[str],
                        code=[str], 
                        answer1=[str],
                        answer2=[str],
                        answer3=[str],
                        answer4=[str],
                        correct=[str],
                        deck_name={deck_name},
                        tags=[str]

                Create that flashcards based on the following data: 
            """
        
    class ProgrammingCard:
        def __init__(self, question: list, type_hint: list, answer: list, deck_name: str, tags: None):
            length = len(question)
            if not all(lst == length for lst in [type_hint, answer]):
                raise ValueError("Lists are not the same length.")
            
            self.question, self.type_hint, self.answer, self.deck_name, self.tags, self.model_name = question, type_hint, answer, deck_name, tags if tags else [], "programming_card"
            self.cards = [self.to_card(q=q, th=th, a=a) for q, th, a in zip(self.question, self.type_hint, self.answer)]

        def to_card(self, q, th, a):
            return {
                "deckName": self.deck_name,
                "modelName": self.model_name,
                "fields": {"Question": q,
                           "Type Hint": th,
                           "Answer": a,
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": self.tags
            }
    
        def prompt(deck_name):
            return """
            Create Anki flashcards using the template:
            Each card should contain:
                'Question': the question (e.g., 'How to define a dictionary in Python?') — as a list[str]
                'Type Hint': a hint about the expected type or syntax (e.g., 'my_dict: var', 'dict[str, int]') — as a list[str]
                'Answer': the correct answer (e.g., 'my_dict = {"a": 1}') — as a list[str]

            Include:
                'deck_name' = '{deck_name}'
                Optional 'tags' = list[str]

            Provide the output in the following format:
                question=[...],
                type_hint=[...],
                answer=[...],
                deck_name='{deck_name}',
                tags=[...]

            Create that flashcards based on the following data:
            """
        
    class messengerCard:
        def __init__(self, front: list, back: list, deck_name:str, type_card: Literal["T", "B"], tags = None):
            if len(front) != len(back):
                raise ValueError("Lists are not the same length.")
            
            self.front, self.back, self.deck_name, self.tags, self.model_name = front, back, deck_name, tags if tags else [], "messengerBasic" if type_card == "B" else "messengerT"
            # Reversed card
            self.cards = [card for fr, bk in zip(self.front, self.back) for card in (self.to_card(fr, bk), self.to_card(bk, fr))]
            
        def to_card(self, f, b):
            return {
                "deckName": self.deck_name,
                "modelName": self.model_name,
                "fields": {"Front": f,
                           "Back": b,
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": self.tags
            }
        
        def prompt(deck_name: str, type_card: Literal["T", "B"], categories: list[str] = None):
            return f"""
        Create Anki flashcards using the template:
        Each card should contain:
            'Front': the front of the card (e.g., 'Hi, how are you?') — as a list[str]
            'Back': the back of the card (e.g., 'I'm good, thanks!') — as a list[str]

        Note:
            Cards will be automatically generated in both directions (front→back and back→front).
            Important: All values must be grouped into single arrays. Do not separate each card as an individual dictionary or block. 
            {"(The only exception is grouping by categories, if there are any provided.)" if not categories == None else ""}

        Include:
            'deck_name' = '{deck_name}'
            Optional 'tags' = list[str]
            'type_card' = '{type_card}'

        Provide the output in the following format:
            front=[...],
            back=[...],
            deck_name='{deck_name}{"" if categories == None else "::category_name"}',
            tags=[...]
            type_card='{type_card}'

        Create that flashcards based on the following data {f"and if it is possible divide flashcards into categories {categories}" if not categories == None else ""}:
        """
        
    class ImportToAnki:
        def __init__(self, cards, anki_url):
            
            self.cards = cards
            self.anki_url = anki_url

            for card in cards:
                payload = {
                    "action": "addNote",
                    "version": 6,
                    "params": {
                        "note": card
                    }
                }
                response = requests.post(self.anki_url, json=payload)
            
                if response.status_code == 200:
                    result = response.json()

                    if result.get('error') is None:
                        print("Corectlly aded")
                    else:
                        print(f"error 1: {result['error']}")
                else:
                    print('error 2')