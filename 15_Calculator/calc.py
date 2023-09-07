# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.widget import Widget
# Cet import nous permet d'utiliser le Builder
from kivy.lang import Builder
#from kivy.properties import ObjectProperty
from kivy.core.window import Window

# Definir les dimension de l'application
Window.size = (500,700)

# Nous designons notre fichier de design .kv
Builder.load_file('calc.kv')

# Ici nous allons utiliser Widget a la place de GridLayout
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

# L'applilcation principal qui sera execute
class CalculatorApp(App):

    # La fonction qui construit l'application
    def build(self):
        return MyLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    CalculatorApp().run()