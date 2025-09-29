# app/screens/login_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_string("")  # no need but garante carregamento

class LoginScreen(BoxLayout):
    info = StringProperty("")

    def do_login(self):
        user = self.ids.email.text.strip()
        pwd = self.ids.password.text.strip()
        if user == "admin" and pwd == "273010":
            # navegar para lista
            self.parent.current = "lista"
            self.ids.email.text = ""
            self.ids.password.text = ""
            self.info = ""
        else:
            self.info = "Usuário ou senha incorretos"
