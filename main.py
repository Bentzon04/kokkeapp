from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button

class OpskirftsApp(App):
        Brændenekærlighed= {
            'Ingredienser': [{'navn':'kartofler', 'mængde': 2, 'enhed':'kg'},
                             {'navn':'løg','mængde':1, 'enhed':'antal' },
                             {'navn':'mælk','mængde':1, 'enhed':'L'},
                             {'navn':'salt','mængde':0.5, 'enhed':'tsk'},
                             {'navn':'smør','mængde':10, 'enhed':'g'},
                             {'navn':'bacon','mængde':1, 'enhed':'kg'}];

            'Vejledning': [{'tekst':"Skræl kartoflerne", 'tid':240, 'skalere':True},
                           {'tekst':"Hak kartofler i små firkanter", 'tid':240, 'skalere':True},
                           {'tekst':"Kog kartoflerne", 'tid':600, 'skalere':False},
                           {'tekst':"Hak løg i tern", 'tid':240, 'skalere':True},
                           {'tekst':"Steg løg", 'tid':300, 'skalere':False},
                           {'tekst':"Hæld vand fra kartofflerne", 'tid':60, 'skalere':False},
                           {'tekst':"Hæld mælk salt og smør til kartoflerne imens du røre rundt", 'tid':120, 'skalere':False},
                           {'tekst':"Pisk indtil tykt", 'tid':240, 'skalere':True},
                           {'tekst':"Steg bacon", 'tid':360, 'skalere':False}];

        };
