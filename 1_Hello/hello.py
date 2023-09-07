# les imports relatifs a la librairie Kivy
import kivy
from kivy.app import App
# Cet import permet d'utiliser le " Label " de kivy
from kivy.uix.label import Label

# L'applilcation principal qui sera execute
class MyApp(App):

    # La fonction qui construit l'application
    def build(self):
        return Label(text="Salut le monde", font_size=69)

# Execution de l'application principal  
if __name__ == "__main__":
    MyApp().run()