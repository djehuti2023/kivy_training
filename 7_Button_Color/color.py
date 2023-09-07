# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.widget import Widget
# Cet import nous permet d'utiliser les proprites du fichier .kv
from kivy.properties import ObjectProperty
# Cet import nous permet d'utiliser le Builder
from kivy.lang import Builder


Builder.load_file('color.kv')

# Ici nous allons utiliser Widget a la place de GridLayout
class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    food = ObjectProperty(None)
    color = ObjectProperty(None)

    # Nous definissons la fonction press
    # 
    def press(self):
        # le .text defini ce qu'il y a dans la zone de saisie(TextInput).
        name = self.name.text
        food = self.food.text
        color = self.color.text
        print(f'Salut {name}, tu aime {food} et ta couleur prefere est {color}')
        
        #Afficher le a l'ecran dans l'application
        # 
        #self.add_widget(Label(text=f'Salut {name}, tu aime {food} et ta couleur prefere est {color}'))
        self.name.text = ""
        self.food.text = ""
        self.color.text = ""

# L'applilcation principal qui sera execute
class AwesomeApp(App):

    # La fonction qui construit l'application
    def build(self):
        return MyGridLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    AwesomeApp().run()