# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.widget import Widget
# Cet import nous permet d'utiliser le Builder
from kivy.lang import Builder
from kivy.properties import ObjectProperty
# Nous designons notre fichier de design .kv
Builder.load_file('update_label.kv')

# Ici nous allons utiliser Widget a la place de GridLayout
class MyLayout(Widget):
        
    def press(self):
        #creer des variables pour les gadgets
        name = self.ids.name_input.text
        print(name)
        
        # Mettre a jour le Label
        self.ids.name_label.text = f'Salut {name}'

        # Nettoyer la zone de saisie
        self.ids.name_input.text = ''

# L'applilcation principal qui sera execute
class AwesomeApp(App):

    # La fonction qui construit l'application
    def build(self):
        return MyLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    AwesomeApp().run()