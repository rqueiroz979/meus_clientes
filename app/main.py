from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from app.screens.login import LoginScreen
from app.screens.home import HomeScreen
from app.screens.cadastro import CadastroScreen
from app.screens.lista import ListaScreen
from app.screens.import_export import ImportExportScreen
from app.database.db import init_db


class MeusClientesApp(App):
    def build(self):
        init_db()
        Builder.load_file("main.kv")

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CadastroScreen(name="cadastro"))
        sm.add_widget(ListaScreen(name="lista"))
        sm.add_widget(ImportExportScreen(name="import_export"))

        return sm


if __name__ == "__main__":
    MeusClientesApp().run()
