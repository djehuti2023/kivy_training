# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.widget import Widget
# Cet import nous permet d'utiliser le Builder
from kivy.lang import Builder
#from kivy.properties import ObjectProperty
from kivy.core.window import Window
# Cet import nous permet d'utiliser le fichier .kv
from kivy.properties import ObjectProperty

# Definir les dimension de l'application
Window.size = (500,700)

# Nous designons notre fichier de design .kv
Builder.load_file('calc1.kv')

# Ici nous allons utiliser Widget a la place de GridLayout
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
    # creons une fonction pour l'appui des boutons
    def button_press(self, button):
        # creons une variable pour contenir ce qu'il 
        # y a deja dans bouton
        prior = self.ids.calc_input.text

        #Si zero est dans la variable
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    
    # La fonction de l'addition
    def add(self):
        prior = self.ids.calc_input.text

        # Ajouter le signe plus au text box
        self.ids.calc_input.text = f'{prior}+'
    
        # La fonction de l'addition
    def subtract(self):
        prior = self.ids.calc_input.text

        # Ajouter le signe plus au text box
        self.ids.calc_input.text = f'{prior}-'
    
        # La fonction de l'addition
    def multiply(self):
        prior = self.ids.calc_input.text

        # Ajouter le signe plus au text box
        self.ids.calc_input.text = f'{prior}*'
    
        # La fonction de l'addition
    def divide(self):
        prior = self.ids.calc_input.text

        # Ajouter le signe plus au text box
        self.ids.calc_input.text = f'{prior}/'

# L'applilcation principal qui sera execute
class CalculatorApp(App):

    # La fonction qui construit l'application
    def build(self):
        return MyLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    CalculatorApp().run()