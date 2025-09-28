from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class LoginScreen(Screen):
    info = StringProperty("")

    def do_login(self):
        usuario = self.ids.email.text.strip()
        senha = self.ids.password.text.strip()

        if usuario == "admin" and senha == "273010":
            self.manager.current = "home"
            self.ids.email.text = ""
            self.ids.password.text = ""
            self.info = ""
        else:
            self.info = "Usuário ou senha incorretos!"
