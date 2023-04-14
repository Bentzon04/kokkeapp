import self as self
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    Recipes = [
        {'navn': 'BK', 'opskrift':{
                'Ingredienser': [{'navn':'kartofler', 'mængde': 1, 'enhed':'kg'},
                            {'navn':'løg','mængde':1, 'enhed':'antal' },
                            {'navn':'mælk','mængde':1, 'enhed':'L'},
                            {'navn':'salt','mængde':2, 'enhed':'tsk'},
                            {'navn':'smør','mængde':20, 'enhed':'g'},
                            {'navn':'bacon','mængde':2, 'enhed':'kg'}],

                'Vejledning': [{'tekst':"Skræl kartoflerne", 'tid':240, 'skalere':True},
                            {'tekst':"Hak kartofler i små firkanter", 'tid':240, 'skalere':True},
                            {'tekst':"Kog kartoflerne", 'tid':600, 'skalere':False},
                            {'tekst':"Hak løg i tern", 'tid':240, 'skalere':True},
                            {'tekst':"Steg løg", 'tid':300, 'skalere':False},
                            {'tekst':"Hæld vand fra kartofflerne", 'tid':60, 'skalere':False},
                            {'tekst':"Hæld mælk salt og smør til kartoflerne imens du røre rundt", 'tid':120, 'skalere':False},
                            {'tekst':"Pisk indtil tykt", 'tid':240, 'skalere':True},
                            {'tekst':"Steg bacon", 'tid':360, 'skalere':False}]

            }
        },
        {'navn': 'PB', 'opskrift':{
        'Ingredienser':[{'navn':'Spaghetti', 'mængde': 1, 'enhed':'kg'},
                        {'navn':'Oksekød', 'mængde': 500, 'enhed':'g'},
                        {'navn':'Tomatsovs', 'mængde': 0.5, 'enhed':'L'},
                        {'navn':'Tomatpure', 'mængde': 1, 'enhed':'stk'},
                        {'navn':'Bullion', 'mængde': 1, 'enhed':'stk'},
                        {'navn':'Salt', 'mængde': 3, 'enhed':'tsk'},
                        {'navn':'Peber', 'mængde': 3, 'enhed':'tsk'},
                        {'navn':'Oregano', 'mængde': 2, 'enhed':'tsk'},
                        {'navn':'Cayennepeber', 'mængde': 5, 'enhed':'tsk'},
                        {'navn':'Hvidløgspulver', 'mængde': 2, 'enhed':'tsk'},
                        {'navn':'Paprika', 'mængde': 3, 'enhed':'tsk'},
                        {'navn':'Parmesanost', 'mængde': 600, 'enhed':'g'},
                        {'navn':'Jomfruolie', 'mængde': 1, 'enhed':'spk'}],

        'Vejledning': [{'tekst':"Kog vand og tilsæt salt", 'tid':300, 'skalere':False},
                       {'tekst':"Tilsæt pasta til vandet", 'tid':480, 'skalere':False},
                       {'tekst':"Tilsæt olie til en ny gryde", 'tid':3, 'skalere':False},
                       {'tekst':"Tilsæt kød til gryden og brun det", 'tid':300, 'skalere':True},
                       {'tekst':"Tilsæt tomatsovs og rør", 'tid':60, 'skalere':True},
                       {'tekst':"Tilsæt tomatpure og rør", 'tid':60, 'skalere':True},
                       {'tekst':"Tilsæt alle kryderierne i kødet", 'tid':60, 'skalere':False},
                       {'tekst':"Server pastaen og kødsovsen hver for sig og parmesan ost", 'tid':60, 'skalere':False}]
            }
        }
    ]
    def build(self):
        layout = GridLayout(cols=2)
        self.add_widget(layout)
        layout.add_widget(Label(id:1))
        layout.add_widget(Button(text='Se Opskrift', on_press=self.change_screen))



    def change_screen(self, caller):
        self.manager.current = 'recipe_screen'

class RecipeScreen(Screen):

    def build(self):
        layout = GridLayout(cols=2)
        #opskriftsLayout = BoxLayout(orientation='vertical')

        layout.add_widget(Label())
        layout.add_widget(Button(text='Tilbage', on_press=self.change_screen))
        self.add_widget(layout)
    def change_screen(self, caller):
            self.manager.current = 'main_screen'




class OpskirftsApp(App):
    def build(self):
        screen_manager = ScreenManager()

        main_screen = MainScreen(name='main_screen')
        main_screen.build()
        screen_manager.add_widget(main_screen)

        recipe_screen = RecipeScreen(name='recipe_screen')
        recipe_screen.build()
        screen_manager.add_widget(recipe_screen)

        return screen_manager


if __name__ == '__main__':
        OpskirftsApp().run()
