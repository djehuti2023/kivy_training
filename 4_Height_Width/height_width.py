# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialisons mot cle infini
    def __init__(self,**kwargs):
        # Appeler le constructeur de grid layout
        super(MyGridLayout, self).__init__(**kwargs)

        # Pour faire un grid layout nous avons besoin de
        # definir le nombre de colonne et de ligne que va
        # contenir notre grid
        #
        # definissons les colonnes
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100

        # Creons un second GridLayout
        # Celui ci sera imbrique dans le premier
        # 
        # Nous pouvons ici definir des valeur par defaut
        #  pour tous les colonnes et lignes de layout
        #  
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100)
        # DEfinissons le nombre de colonnes que
        # va contenir le Layout
        self.top_grid.cols = 2
        
        # Ajoutons les gadgets(widget) a top_grid
        # La plus part des elements de kivy sont 
        # des gadgets(les boutons, les textes, les inputs ...)
        #  
        self.top_grid.add_widget(Label(text="Nom: "))        
        # Ajoutons une zone de saisie
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)
        #  
        self.top_grid.add_widget(Label(text="Plat prefere: "))        
        # Ajoutons une zone de saisie
        self.food = TextInput(multiline=False)
        self.top_grid.add_widget(self.food)
        #  
        self.top_grid.add_widget(Label(text="Couleur prefere: "))        
        # Ajoutons une zone de saisie
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Ajoutons notre top_grid a notre application
        self.add_widget(self.top_grid)

        # Creons un bouton de soumission puis attachons le 
        # a une action specifique 
        self.submit = Button(text="Soumettre",
                              font_size=32,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=200
                              )
        # Attachons le bouton a une action
        self.submit.bind(on_press=self.press)
        #Le bouton sera dans le premier layout de une colonne
        self.add_widget(self.submit)
    
    # Nous definissons la fonction press
    # Puis nous definissons une instance qui le defini lui meme
    # 
    def press(self, instance):
        # le .text defini ce qu'il y a dans la zone de saisie(TextInput).
        name = self.name.text
        food = self.food.text
        color = self.color.text
        print(f'Salut {name}, tu aime {food} et ta couleur prefere est {color}')
        
        #Afficher le a l'ecran dans l'application
        # 
        self.add_widget(Label(text=f'Salut {name}, tu aime {food} et ta couleur prefere est {color}'))

# L'applilcation principal qui sera execute
class MyApp(App):

    # La fonction qui construit l'application
    def build(self):
        return MyGridLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    MyApp().run()