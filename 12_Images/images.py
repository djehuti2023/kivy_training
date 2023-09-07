# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.widget import Widget
# Cet import nous permet d'utiliser le Builder
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('images.kv')

# Ici nous allons utiliser Widget a la place de GridLayout
class MyLayout(Widget):
    pass

# L'applilcation principal qui sera execute
class AwesomeApp(App):

    # La fonction qui construit l'application
    def build(self):
        # Pour changer la couleur de font de l'application
        Window.clearcolor = (1, 1, 1, 1) # blanc
        return MyLayout()

# Execution de l'application principal  
if __name__ == "__main__":
    AwesomeApp().run()